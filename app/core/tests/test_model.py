
from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Tests creating a new user with email is successful """
        email = 'test@londonappdev.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(emailaddress=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):

        email = 'test@JOEL.COM'
        password = 'testpass123'
        user = get_user_model().objects.create_user(emailaddress=email, password=password)
        self.assertEqual(user.email, email.lower())

    def test_new_user_valid_email(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(emailaddress="jo@.co", password='password')

    def test_create_new_super_user(self):

        user = get_user_model().objects.create_superuser(emailaddress='joelvarm@sc.com', password='asdasd')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


