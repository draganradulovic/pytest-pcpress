import unittest
from testing.order_tests import Order_tests

tc1= unittest.TestLoader().loadTestsFromTestCase(Order_tests)

ts= unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(ts)
