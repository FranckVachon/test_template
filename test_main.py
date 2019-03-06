"""" .py contenant les tests à effectuer"""

import unittest                         # our test lib
import numpy as np                      # if we want to test numpy arrays
## importation du code @ tester
from class_to_test import SomeClass


class SomeTests(unittest.TestCase):     # on doit hériter de TestCase

    @classmethod
    def setUpClass(cls):
        """
        this runs only once. Set stuff that's useful for ALL test
        Like common values you want to reuse, loading a text file etc.
        """

        cls.valid_test_shapes = [(3, 4, 2), (3, 2, 4), (1, 24), (24, 1), (2, 12), (12, 2)]
        cls.invalid_test_shapes = [(1, 2), (5, 12), (3, 4)]

    @classmethod
    def tearDownClass(cls):
        "cleanup after all the tests are done. Like freeing a resources, cleaning a temporary repo etc."
        pass


    def setUp(self):
        """ Runs after EACH test. Here we instantiate a new instance
         each test because we don't want the values modified by a previous test to influence the results of the next one"""
        self.obj = SomeClass()

    def tearDown(self):
        """
        Runs after each test. Similar to class teardown
        """

    ################################################ tests

    def test_base_demo(self):                           # you MUST prefix all the methods with test_*******
        """ A typical test method in unittest"""

        expected = 42                                   # what we expect the result will be
        actual = self.obj.some_attribute                # actual result from the test

        self.assertEqual(expected, actual)

    def test_metho1(self):

        obj = self.obj
        expected = 42
        for i in range(1,10):                           # testing more cases
            obj.some_method()
            expected = expected*2
            actual = obj.some_attribute
            self.assertEqual(expected, actual)

    def test_assert_error(self):                        # a test that expects an error to be raised - the test passes if the error happens

        expected = "a wrong value"
        actual = self.obj.some_attribute

        with self.assertRaises(TypeError):              # e.g. trying to add string & int should raise a TypeError
            ans = expected + actual

    def test_using_numpy_array(self):

        arr = np.arange(24)
        for shp in self.valid_test_shapes:

            expected = np.reshape(arr, shp)
            actual = self.obj.reshape_array(shp)
            np.testing.assert_array_equal(expected, actual)   # to do test on numpy array, the best is to use np.testing

    def test_invalid_numpy(self):                           # same as previously but with invalid reshapes, expect errors raised

        for shp in self.invalid_test_shapes:                # all shapes are invalid, all should raise errors for the test to succeed
            with self.assertRaises(ValueError):
                self.obj.reshape_array(shp)


    def test_this_test_fails(self):
        # a test that fails

        self.assertIsInstance(self.obj, int)



if __name__ == '__main__':
    unittest.main()
