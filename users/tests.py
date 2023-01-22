from django.contrib.auth.middleware import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse('users:register'),
            data={
                'username': '@Ilyossbekkk',
                'first_name': 'Ilyosbek',
                'last_name': 'Karshiboyev',
                'email': 'karshiboyevilyosbekk@gmail.com',
                'password': 'Ilyosbbek#Dev001',
            }
        )

        user = CustomUser.objects.get(username='@Ilyossbekkk')

        self.assertEqual(user.first_name, 'Ilyosbek')
        self.assertEqual(user.last_name, 'Karshiboyev')
        self.assertEqual(user.email, 'karshiboyevilyosbekk@gmail.com')
        self.assertNotEqual(user.password, 'Ilyosbek#Deev001')
        # self.assertTrue(user.check_password('Ilyosbek#Dev001'))

    def test_is_required(self):
        self.client.post(
            reverse('users:register'),
            data={
                'username': '@Ilyossbekkk',
                'email': 'karshiboyevilyosbekk@gmail.com',
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)

    def test_unique_username(self):
        user = CustomUser.objects.create_user(username='abcd', password='ssasa')
        user.set_password('ssasa')
        user.save()

        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'abcd',
                'email': 'ssas@fas.a',
                'password': 'ssasa',
            }
        )
        # user = User.objects.get(username='admin')
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        # self.assertEqual(user.username, 'admin')
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')


class LoginTestCase(TestCase):
    def test_successful_login(self):
        db_user = CustomUser.objects.create_user(username='abcddd', password='ssssasa')
        db_user.set_password('ssssasa')
        db_user.save()

        self.client.post(
            reverse('users:login'),
            data={
                "username": 'abcddd',
                "password": 'ssssasa'
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_username(self):
        db_user = CustomUser.objects.create_user(username='abcddd', password='ssssasa')
        db_user.set_password('ssssasa')
        db_user.save()

        self.client.post(
            reverse('users:login'),
            data={
                "username": 'asdaw',
                "password": 'ssssasa'
            }
        )

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('users:login') + '?next=/users/profile/')

    def test_profile_detail(self):
        user = CustomUser.objects.create(
            username='Ilyyos',
            password='asdasdasd'
        )
        user.set_password('asdasdasd')
        user.save()
        self.client.login(username='Ilyyos', password='asdasdasd')

        response = self.client.get(reverse('users:profile'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
