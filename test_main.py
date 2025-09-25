import unittest
import json
import xmlrunner
import os


# ensure reports folder exists
os.makedirs('reports', exist_ok=True)

loader = unittest.TestLoader()
suite = loader.discover('.')  # discover all tests

with open('reports/results.xml', 'wb') as output:
    runner = xmlrunner.XMLTestRunner(output=output)
    runner.run(suite)


class TestJSONLoaderMethods(unittest.TestCase):
    books = []

    @classmethod
    def setUpClass(cls):
        with open('books.json') as json_file:
            cls.books = json.load(json_file)
    
    def test_title(self):
        self.assertEqual(self.books[0]['title'], 'To Kill a Mockingbird')

    def test_id(self):
        self.assertEqual(self.books[0]['id'],'1')


if __name__ == '__main__':
    unittest.main()