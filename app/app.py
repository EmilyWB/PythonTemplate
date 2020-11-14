"""=============================================================================
                                    IMPORTS
============================================================================="""
# Python package imports
import sys
import os
import configparser
import logging
from datetime import datetime

# Load local CFFI extensions
from cext.build.cffi_demo import lib as demo

# Local module import
import anothermodule
import configLog

"""=============================================================================
                            MODULE-LEVEL VARIABLES
============================================================================="""
# Our config file name for the app
IniFileName = "config.ini"

# Module Logger
Logger = logging.getLogger(__name__)


"""=============================================================================
                                    FUNCTIONS
============================================================================="""
def main():
    """
    The main function call of the application. From here we configure the 
    logger, load our config file, and demonstrate using the C extension modules
    """
    
    configLog.config(__name__)

    # Logger levels: debug, info, warning, error, critical
    Logger.info('App started')
    
    # Grab the config file
    config = configparser.ConfigParser()
    if config.read(IniFileName):
        Logger.info('%s loaded successfully' % (IniFileName))
    else:
        Logger.error('%s failed to load' % (IniFileName))
        raise Exception ("Cannot load %s"%IniFileName)

    # Show we have loaded our config, and we can grab bits from it
    Logger.debug(config["section1"]["pi"])
    Logger.debug(config["trans"]["human"])

    # Demonstrate left bit-shift with our C extension
    Logger.debug(demo.LeftShift(74, 2))

    # Get some nibbles, we hungry
    Logger.debug(demo.GetHighNibble(90))

    # Use some code in another module
    anothermodule.afunctionname()

    Logger.info('App finished')
