"""=============================================================================
                                    IMPORTS
============================================================================="""
# Python package imports
import logging
from datetime import datetime


"""=============================================================================
                            MODULE-LEVEL VARIABLES
============================================================================="""
# Module logger
logger = logging.getLogger(__name__)


"""=============================================================================
                                    FUNCTIONS
============================================================================="""
def config(namePrefix):
    """ Configures the logging for the application.
    By running logging.basicConfig, we are configuring the loggers for all
    other modules using the logging package.
    """

    if False == isinstance(namePrefix, str) :
        raise TypeError("Log file name must be a string")

    # We will name the log files using date and time, so we will generate a 
    # new one when the application is run
    now = datetime.now() 
    date_time = now.strftime("%d%m%Y_%H%M%S")
    logFilename="logs/"+namePrefix+"_"+date_time+".log"

    logging.basicConfig(format='%(asctime)-24.24s: %(name)-16.16s: '+ \
                        '%(levelname)-6.6s: %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        level=logging.DEBUG,
                        handlers=[
                            logging.FileHandler(logFilename),
                            logging.StreamHandler()
                        ])

    logger.info('Logger configured')
