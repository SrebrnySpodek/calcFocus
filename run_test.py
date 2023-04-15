import unittest
import os
from calcFocus import calc_focus as cf

class TestStringMethods(unittest.TestCase):

    def test_path_dir(self):
        path = "./focus1"
        cf.calculate(path)

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
        list_with_fits = [os.path.join(path, f) for f in os.listdir(path) if ".fits" in f]
        focus_list = ['15760', '15512', '15712', '15662', '15462', '15612', '15312', '15409', '15561', '15611', '15812', '15359', '15512', '15663', '15593']
        cf.calculate(list_with_fits, focus_list=focus_list)

    def test_rms_method(self):
        path = "./focus1"
        list_with_fits = [os.path.join(path, f) for f in os.listdir(path) if ".fits" in f]
        focus_list = ['15760', '15512', '15712']
        with self.assertRaises(ValueError):
            cf.calculate(list_with_fits, method="rms", focus_list=focus_list)

    def test_fit_focus_list_need_have_the_same_len(self):
        path = "./focus1"
        list_with_fits = [os.path.join(path, f) for f in os.listdir(path) if ".fits" in f]
        focus_list = ['15760', '15512', '15712', '15662', '15462', '15612', '15312', '15409', '15561', '15611', '15812', '15359', '15512', '15663', '15593']
        with self.assertRaises(ValueError):
            cf.calculate(list_with_fits, focus_list=focus_list[:8])


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