import unittest
from src.models.user import User

class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.

    Tests:
        - Attribute initialization
        - Password verification
        - Salted password generation
    """

    def setUp(self):
        """
        Set up a User instance for testing.
        """
        self.user = User("Alice", 30, "secure123")

    def test_password_verification(self):
        """
        Test that password verification works correctly.
        """
        self.assertTrue(self.user.verify_password("secure123"), "Password should be verified correctly.")
        self.assertFalse(self.user.verify_password("wrongpass"), "Incorrect password should not be verified.")

    def test_salted_password(self):
        """
        Test that salted password is a string and differs from the original hash.
        """
        salted = self.user.salt_password("mysalt")
        self.assertIsInstance(salted, str, "Salted password should be a string.")
        self.assertNotEqual(salted, self.user._password_hash, "Salted password should differ from original hash.")

    def test_attributes(self):
        """
        Test that user attributes are correctly assigned.
        """
        self.assertEqual(self.user.name, "Alice", "Name should be 'Alice'.")
        self.assertEqual(self.user.age, 30, "Age should be 30.")
