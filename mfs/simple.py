import unittest


class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.config = {}
    def test_simply_sort(self):
    
        a = {'a':'b', 'c':'d', 'e':'f'}
        sorted(a)
    def test_simply_sort_dict_key(self):
        a = {'a':'b', 'c':'d', 'e':'f'}
        sorted(a.keys())
