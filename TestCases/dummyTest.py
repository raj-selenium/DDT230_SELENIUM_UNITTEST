def add(a,b):
    return a+b


import unittest
from ddt import ddt, data, unpack

@ddt
class Test1(unittest.TestCase):
    data1 = 20

    @classmethod
    def setUpClass(cls):
        print("SetupClass ran before all test once")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass ran after all the test once")

    def setUp(self):
        print("Setup ran before each test")

    def tearDown(self):
        print("tearDown run after each test")

    @data((10,20,30),("custard","apple","custardapple"),(12.3,12.2,24.5))
    @unpack
    def test_2_add(self, param1, param2, expected_result):
        print("test case "+str(param1))
        self.assertEqual(add(param1,param2), expected_result)

    def test_1_add_list(self):
        print("i am the test case" + "list")
        self.assertListEqual(add([1,2],[2,3]), [1,2,2,3])

    @unittest.skip("waiting for developer")
    def test_dummy_1(self):
        pass

    @unittest.skipIf(data1 != 10, "data is not 10")
    def test_dummy_2(self):
        self.assertEqual(self.data1, 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)


# how to create test fixtures (setup and teardown)
    #  setUpClass  - class method, run only once before all the test
    #  setUp       - instance method, run before each test
    #  tearDown    - instance method, run after each test
    #  tearDownClass- class method, run only one after all test executionis completed

# how to create a test case
    # import unittest
    # inherit unittest.TestCase
    # create test methods - name should contain test_
    # TestCases will run based on alphabetical order
    # we can add numbers in TestCases to prioritize (test_1_)
# how to verify the test result
    # using asserts from unittest
# how to skip a test case
    # @unittest.skip or skipIf
# how to run a single test for multiple data (DDT)
    # install ddt (requirements.txt)
    # from ddt import ddt, data, unpack
    # @ddt, @data(()), @unpack
    # use parameters to receive the data in the test_method
# how to create a test suite
# how to create a test report

