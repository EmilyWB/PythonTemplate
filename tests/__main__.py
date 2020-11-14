"""=============================================================================
                                    IMPORTS
============================================================================="""
# Python package imports
import logging
from datetime import datetime

# Import the logging module from the app
from app import configLog

# Import test modules
import test_anothermodule
import test_cffi_demo


"""=============================================================================
                            MODULE-LEVEL VARIABLES
============================================================================="""
# Module logger
logger = logging.getLogger("testmain")
# File name of the unittest logs
# Note that the individual test filefiles in the actual file name
testLogName = "logs/%s.logs"

"""=============================================================================
                                    MAIN
============================================================================="""
if __name__ == "__main__":


    configLog.config("test")

    logger.info('Tests started')

    test_cffi_demo.runTest(testLogName)
    test_anothermodule.runTest(testLogName)

    logger.info('Tests finished')
