from django.test import TestCase

from users.models import CustomUser
from users.forms import CustomUserCreationForm


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
