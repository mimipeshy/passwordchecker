import unittest

from registration import check_password


class Test(unittest.TestCase):

    def test_regex(self):
        actual = 'ABd12341'
        expect = '((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,12})'
        self.assertRegex(actual, expect)

    def test_password(self):
        password = 'ABd1234@1'
        self.assertEqual('ABd1234@1', check_password(password))


if __name__ == '__main__':
    unittest.main()
