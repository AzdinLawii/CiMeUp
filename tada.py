

import unittest
# import nose


class TestProgram(unittest.TestCase):

    # no
    def test_no(self):
        self.assertEqual(1,0)
    # yes
    def test_yes(self):
        self.assertEqual(1,1)
        
if __name__ == '__main__':
    unittest.main()