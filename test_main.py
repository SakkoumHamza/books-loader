import unittest
import json


class TestJSONLoaderMethods(unittest.TestCase):
    books = []

    @classmethod
    def setUpClass(cls):
        with open('books.json') as json_file:
            cls.books = json.load(json_file)

    def test_author(self):
        self.assertEqual(self.books[0]['author'], 'Daniel Defoe')
    
    def test_title(self):
        self.assertEqual(self.books[0]['title'], 'Robinson Crusoe')
    
    def test_id(self):
        self.assertEqual(self.books[0]['id'], '0')

if __name__ == '__main__':
    unittest.main()