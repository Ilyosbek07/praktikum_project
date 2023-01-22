from django.test import TestCase
from django.urls import reverse

from books.models import Book, Author, BookAuthor
from users.models import CustomUser


# class BooksTestCase(TestCase):
#     # def test_no_books(self):
#     #     response = self.client.get(reverse('books:list'))
#     #     self.assertContains(response, 'No books found.')
#     #
#     def test_books_list(self):
#         Book.objects.create(title='1', description='1', isbn='1')
#         Book.objects.create(title='2', description='2', isbn='2')
#
#         response = self.client.get(reverse('books:list'))
#         books = Book.objects.all()
#
#         for book in books:
#             self.assertContains(response, book.title)
#
#     def test_detail_page(self):
#         book = Book.objects.create(title='1', description='text', isbn='1')
#
#         response = self.client.get(reverse('books:detail', kwargs={'id': book.id}))
#
#         self.assertContains(response, book.title)
#
#     #
#     def test_search_books(self):
#         book1 = Book.objects.create(title='1', description='1', isbn='1')
#         book2 = Book.objects.create(title='2', description='2', isbn='2')
#
#         response = self.client.get(reverse('books:list') + '?q=1')
#
#         self.assertContains(response, book1.title)
#         # self.assertNotContains(response, book2.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book1 = Book.objects.create(title='Book', description='description', isbn='3')
        user = CustomUser.objects.create(
            username='Ilyyos',
            password='asdasdasd'
        )
        user.set_password('asdasdasd')
        user.save()
        self.client.login(username='Ilyyos', password='asdasdasd')

        self.client.post(
            reverse('books:reviews', kwargs={'id': book1.id}), data={
                'stars_given': 3,
                'comment': 'comment'
            }
        )
        book_review = book1.book
        self.assertEqual(book_review.count(), 1)

    def test_book_author(self):
        book1 = Book.objects.create(title='Book', description='description', isbn='3')
        author = Author.objects.create(
            first_name='Ilyosbek', last_name='Karshiboyev', email='karshiboyevilyosbek@gmail.com',
            bio='Text bio'
        )
        book_author = BookAuthor.objects.create(book='Book', author='Ilyosbek')
        print(book_author)
