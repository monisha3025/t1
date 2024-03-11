import unittest

from graobj import Grades


class TestcalculatorMethods(unittest.TestCase):
    r=Grades()

    def testaddition(self):
        # self.r = Grades()
        self.assertEqual(self.r.calGra(90), 'Grade A')

    def testaddition(self):
        self.assertEqual(self.r.calGra(80), 'Grade B')

    def testaddition(self):
        self.assertEqual(self.r.calGra(70), 'Grade C')

    def testaddition(self):
        self.assertEqual(self.r.calGra(60), 'FAIL')




if __name__ == '__main__':
    unittest.main()
