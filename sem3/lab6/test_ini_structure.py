import unittest

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.opened_file = open('main.ini')
        cls.tested_file = cls.opened_file.read()
        print('Файл открыт и прочитан')

    def test_key_availability(self):
        self.assertIn("precision", MyTestCase.tested_file)
        self.assertIn("outfile", MyTestCase.tested_file)

    def test_value_key(self):
        precision = None
        outfile = None
        for line in MyTestCase.tested_file.splitlines():
            line = line.strip()
            if line.startswith("precision"):
                precision = line.split("=")[1].strip()
            elif line.startswith("outfile"):
                outfile = line.split("=")[1].strip()
        self.assertEqual(precision, '0.0001')
        self.assertEqual(outfile, 'out.txt')

    @classmethod
    def tearDownClass(cls):
        cls.opened_file.close()
        print('Файл закрыт')


if __name__ == '__main__':
    unittest.main()
