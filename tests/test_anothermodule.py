"""=============================================================================
                                    IMPORTS
============================================================================="""
# Python package imports
import logging
import unittest

# Import module under test
from app import anothermodule

"""=============================================================================
                            MODULE-LEVEL VARIABLES
============================================================================="""
# Module logger
logger = logging.getLogger(__name__)

"""=============================================================================
                                TEST CASES
============================================================================="""
class afunctionname_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Correct(self):
        self.assertTrue(anothermodule.afunctionname())


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
