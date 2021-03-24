from django.test import TestCase

from users.models import CustomUser


class CustomUserModelTest(TestCase):

    def test_create_user(self):
        user = CustomUser(username='test_user')
        self.assertIs(user.username, 'test_user')
