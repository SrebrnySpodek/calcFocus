import unittest
import os
from calcFocus import calc_focus as cf

class TestStringMethods(unittest.TestCase):

    def test_path_dir(self):
        path = "./focus1"
        cf.calculate(path, method="rms")

    def test_file_list(self):
        path = "./focus1"
        lista = [os.path.join(path, f) for f in os.listdir(path) if ".fits" in f]
        cf.calculate(lista)

    def test_file_list_error(self):
        with self.assertRaises(ValueError):
            lista = [".focus1/dupa.fits"]
            cf.calculate(lista)

    def test_file_list_error2(self):
        with self.assertRaises(ValueError):
            path = "./focus4"
            cf.calculate(path)
    def test_focus_list(self):
        path = "./focus1"
        focus_list = ['15760', '15512', '15712', '15662', '15462', '15612', '15312', '15409', '15561', '15611', '15812', '15359', '15512', '15663', '15593']
        cf.calculate(path, focus_list=focus_list)


if __name__ == '__main__':
    unittest.main()


"""
# to do :
hmmm? do it later :*

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_value_error'))
    unittest.TextTestRunner().run(suite)
"""