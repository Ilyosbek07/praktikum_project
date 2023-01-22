from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Review, Book
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        # DRY - don't repeat yourself
        self.user = CustomUser.objects.create(username='test_user', first_name='test', last_name='user')
        self.user.set_password('test_password')
        self.user.save()
        self.client.login(username='test_user', password='test_password')
        self.book1 = Book.objects.create(title='Book', description='description', isbn='3')
        self.book_review = Review.objects.create(book=self.book1,
                                                 user=self.user, stars_given=3,
                                                 comment='My comment')

    def test_book_review_detail(self):
        book1 = Book.objects.create(title='Book', description='description', isbn='3')
        book_review = Review.objects.create(book=book1, user=self.user, stars_given=3, comment='My comment')

        response = self.client.get(reverse('api:review-detail', kwargs={'id': book_review.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], book_review.id)
        self.assertEqual(response.data['stars_given'], 3)
        self.assertEqual(response.data['comment'], 'My comment')
        self.assertEqual(response.data['book']['id'], book_review.book.id)
        self.assertEqual(response.data['book']['title'], 'Book')
        self.assertEqual(response.data['book']['description'], 'description')
        self.assertEqual(response.data['book']['isbn'], '3')
        self.assertEqual(response.data['user']['id'], self.user.id)

    def test_update_review(self):
        # book1 = Book.objects.create(title='Book', description='description', isbn='3')
        # book_review = Review.objects.create(book=book1, user=self.user, stars_given=3, comment='My comment')
        #
        # response = self.client.patch(reverse(
        #     'api:review-detail', kwargs={'id': book_review.id}),
        #     data={'stars_given': 4, 'comment': 'test_comment_updated'}
        # )
        # print(response)
        # self.assertEqual(response.status_code, 206)
        # self.assertEqual(book_review.stars_given, 4)
        # self.assertEqual(book_review.comment, 'test_comment_updated')
        book = Book.objects.create(title='test_book', description='test_descrption', isbn='1234')
        br = Review.objects.create(stars_given=5, comment='test_comment', book=book, user=self.user)
        response = self.client.patch(reverse(
            'api:review-detail', kwargs={'id': br.id}), data={'stars_given': 4, 'comment': 'test_comment_updated'})
        br.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(br.stars_given, 4)

    def test_review_put(self):
        book = Book.objects.create(title='test_book', description='test_descrption', isbn='1234')
        br = Review.objects.create(stars_given=5, comment='test_comment', book=book, user=self.user)
        response = self.client.patch(reverse(
            'api:review-detail', kwargs={'id': br.id}),
            data={'stars_given': 4, 'comment': 'test_comment_updated','book_id': book.id, 'user_id': self.user.id})
        br.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(br.stars_given, 4)
        self.assertEqual(br.comment, 'test_comment_updated')
