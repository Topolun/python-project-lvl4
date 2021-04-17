from django.test import TestCase

from users.models import CustomUser
from users.forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


class CustomUserModelTest(TestCase):

    def test_create_user(self):
        user = CustomUser(username='test_user')
        self.assertIs(user.username, 'test_user')


class CustomUserCreationFormTest(TestCase):

    def test_create_user_form(self):
        user_data = {
            'username': 'test_user',
            'password1': 'something',
            'password2': 'something'
            }
        user_form = CustomUserCreationForm(user_data)
        self.assertIs(user_form.is_valid(), True)

    def test_create_wrong_user_form(self):
        user_data = {
            'username': 'test_user',
            'password1': 'something',
            'password2': 'something_else'
            }
        user_form = CustomUserCreationForm(user_data)
        self.assertIs(user_form.is_valid(), False)

    def test_create_empty_password_user_form(self):
        user_data = {
            'username': 'test_user',
            'password1': '',
            'password2': ''
            }
        user_form = CustomUserCreationForm(user_data)
        self.assertIs(user_form.is_valid(), False)

    def test_create_empty_username_user_form(self):
        user_data = {
            'username': '',
            'password1': 'something',
            'password2': 'something'
            }
        user_form = CustomUserCreationForm(user_data)
        self.assertIs(user_form.is_valid(), False)


class SigninTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='123456',
            )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='123456')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class LoginTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='123456',
            )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_success(self):
        response = self.client.login(username='test', password='123456')
        self.assertTrue(response)

    def test_login_fail(self):
        response = self.client.login(username='test', password='wrong')
        self.assertFalse(response)


class UserDataCangesTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='123456',
            )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        self.client.login(username='test', password='123456')
        newName = 'NewName'
        self.client.post('/users/1/update/', {'username': newName})
        resp = self.client.get('/users/1/update/')
        self.assertEqual(str(resp.context['user']), newName)
