import unittest
from asa import repeat, delete_repeat



class Tests(unittest.TestCase):
    def test_repeat(self):
        result = repeat([2,3,4,5,6],[2,3,4,7,7,7,7])
        self.assertTrue(result == {2,3,4})

    def test_delete_repeat(self):
        result = delete_repeat([2,2,2,3,4,5,5,5,6,7])
        self.assertTrue(result == [2,3,4,5,6,7])

    if __name__ == '__main__':
        unittest.main()

