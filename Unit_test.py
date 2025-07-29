import unittest
import os

class mockObj():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, mockObj) and self.name == other.name and self.age == other.age


class ExampleTestCases(unittest.TestCase):
    def test_str(self):
        self.assertEqual("string is the same", "string is the same", "strs are not equal")

    def test_object(self):
        obj1 = mockObj("Chris", 20)
        obj2 = mockObj("Chris", 20)
        self.assertEqual(obj1, obj2, "Given Objects are not equal")

    def test_file_existing(self):
        self.assertTrue(os.path.exists("./test_file.txt"), "File doesn't exist")

if __name__ == '__main__':
    unittest.main()
