# write a program to find the product of digits of a number.

    

def prod(n):
    s = 1
    #enter code here
    return s
import unittest

class Test(unittest.TestCase):
    def testsum1(self):
        actual = prod (123)
        expected = 6
        self.assertEqual(actual, expected)
    def testsum2(self):
        actual = prod (123456)
        expected = 720
        self.assertEqual(actual, expected)
    def testsum3(self):
        actual = prod (12)
        expected = 2
        self.assertEqual(actual, expected)
    def testsum4(self):
        actual = prod (1)
        expected = 1
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)