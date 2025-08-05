# CICD_EXAMPLE/Unit_test.py
"""
Unit tests for basic string comparison, object equality using a custom class (mockObj),
and file existence check.

This test suite includes:\n
- A string equality test.\n
- A test for equality of two mockObj instances.\n
- A check for the existence of a specific file on disk.
"""
import os
import unittest

class mockObj():
    """
    A simple mock object class to demonstrate equality comparison.

    Attributes:
        name (str): The name of the object.
        age (int): The age associated with the object.
    """

    def __init__(self, name: str, age: int):
        """
        Initializes a mockObj instance with a name and age.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
        """
        self.name = name
        self.age = age

    def __eq__(self, other):
        """
        Checks equality between two mockObj instances.

        Examples:
            >>> mockObj1 == mockObj2
            true
            >>> mockObj1 == mockObj3
            false

        Args:
            other (mockObj): The object to compare with.

        Returns:
            bool: True if both objects have the same name and age, False otherwise.
        """
        return isinstance(other, mockObj) and self.name == other.name and self.age == other.age


class ExampleTestCases(unittest.TestCase):
    """
    A set of unit tests to validate string comparison, object equality, and file existence.
    """

    def test_str(self):
        """
        Tests whether two identical strings are equal.
        """
        self.assertEqual("string is the same", "string is the same", "strs are not equal")

    def test_object(self):
        """
        Tests whether two mockObj instances with the same attributes are considered equal.
        """
        obj1 = mockObj("Chris", 20)
        obj2 = mockObj("Chris", 20)
        self.assertEqual(obj1, obj2, "Given Objects are not equal")

    # def test_file_existing(self):
    #     """
    #     Tests whether a specific file exists in the current directory.
    #     """
    #     #print("Current dir:", os.getcwd())
    #     self.assertTrue(os.path.exists("test_file.txt"), "File doesn't exist")


# if __name__ == '__main__':
#     unittest.main()

