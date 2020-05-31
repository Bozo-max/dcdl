import unittest

import dcdl
import renarda, renardo

class TestRenardo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nums = [1,2,3,4]
        cls.obj = 13
        cls.res = renardo.solve(cls.nums, cls.obj)

    def test_bon_compte(self):
        self.assertEqual(self.res[1],13)

    def test_bonnes_op(self):
        self.assertEqual(len(self.res[0]),2)
    
    def test_compte_approchant(self):
        res = renardo.solve(self.nums, 29)
        self.assertEqual(res[1],30)

if __name__=='__main__':
    unittest.main()