from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'kaylinthecoder@gmail.com'
        password = 'kyalinnn'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = 'kaylinthecoder@gmail.com'
        user = get_user_model().objects.create_user(email, 'kyalinnn')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """"Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'kyalinnn')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'kaylinthecoder@gmail.com',
            'kyalinnn'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
