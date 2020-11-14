"""=============================================================================
                                    IMPORTS
============================================================================="""
# Python package imports
import logging
import unittest

# Import module under test
from cext.build.cffi_demo import lib as demo


"""=============================================================================
                            MODULE-LEVEL VARIABLES
============================================================================="""
# Module logger
logger = logging.getLogger(__name__)


"""=============================================================================
                                TEST CASES
============================================================================="""
class GetHighNibble_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Correct(self):
        self.assertEqual(
            demo.GetHighNibble(90),
            5)

    def test_Incorrect(self):
        # ((156 & 0xf0) >> 4) = 9
        self.assertNotEqual(
            demo.GetHighNibble(156),
            5)

    # Expects a uint8
    def test_OverFlow(self):
        with self.assertRaises(OverflowError):
            demo.GetHighNibble(654)

    def test_Negative(self):
        with self.assertRaises(OverflowError):
            demo.GetHighNibble(-6)

    def test_Float(self):
        with self.assertRaises(TypeError):
            demo.GetHighNibble(12.6)


class LeftShift_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Correct(self):
        self.assertEqual(
            demo.LeftShift(2,2),
            8)

    def test_Incorrect(self):
        # 7 << 2 = 28
        self.assertNotEqual(
            demo.LeftShift(7,2),
            12)

    def test_OverFlow_1(self):
        with self.assertRaises(OverflowError):
            demo.LeftShift(0x1ffffffff, 2)

    def test_OverFlow_2(self):
        with self.assertRaises(OverflowError):
            demo.LeftShift(2, 0x1ffffffff)

    def test_Negative_1(self):
        with self.assertRaises(OverflowError):
            demo.LeftShift(-2, 6)

    def test_Negative_2(self):
        with self.assertRaises(OverflowError):
            demo.LeftShift(2, -6)

    def test_Float_1(self):
        with self.assertRaises(TypeError):
            demo.LeftShift(1.5, 53)

    def test_Float_2(self):
        with self.assertRaises(TypeError):
            demo.LeftShift(6, 6.8)


"""=============================================================================
                                    FUNCTIONS
============================================================================="""
def runTest(testLogName):
    logger.info("Starting tests in "+__name__)

    log_file = testLogName % __name__
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=6)
        unittest.main(
            module=__name__, 
            verbosity=3, 
            exit=False, 
            testRunner= runner)

    logger.info("Finished tests in "+__name__)
