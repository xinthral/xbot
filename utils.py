import datetime
import logging
import os
import wrapt

from configparser import ConfigParser
from random import choice, seed
from time import perf_counter

logging.basicConfig(
    filename = 'logs/master.log',
    level = logging.INFO,
    format = '%(asctime)s %(message)s',
    datefmt = '[%B %d, %Y] %H:%M:%S'
)

def cnf(section, setting):
    ConfigFile = os.getcwd() + "/settings.config"

    config = ConfigParser()
    config.read(ConfigFile)
    value = config.get(section, setting)
    if value.lower() == 'true':
        return(True)
    elif value.lower() == 'false':
        return(False)
    else:
        return(value)

@wrapt.decorator
def LogParam(orig_func, instance, *args):
    """
    Logger Function: boilerplate wrapper to log function
     - Instance method for variable argument functions
     - logs into loggrs directory as {functionName}.log
    """
    logging.info(f":: {orig_func.__name__} ran with args: {args}")
    return(orig_func(*args[1:]))

# @wrapt.decorator
# def ExceptIt(orig_func, instance, *args, **kwargs):
#     """
#     Logger Function: boilerplate wrapper to log function
#     """
#     typ, err, errno = sys.exc_info()
#     logging.warning(f":: {orig_func.__name__} experienced an {typ} exception: {err}.")
#     return(orig_func(*args, *kwargs))

def timeStamp():
    """
    TimeStamp Function: generates formated timestamp
    """
    from time import strftime, localtime
    now = strftime("[%B %d, %Y] %H:%M:%S", localtime())
    return(now)

def timer(dtime):
    """
    Timer Function: Returns time elapsed as datetime.deltatime object
    """
    now = datetime.now()
    response = now - dtime
    return(response)

def timeDelta(dtime):
    """
    TimeDelta Function: Returns time elapsed as formatted string
    """
    now = datetime.now()
    changeTime = now - dtime
    minutes = changeTime.total_seconds() / 60
    seconds = changeTime.total_seconds() % 60
    return('{}:{:.2f}'.format(int(minutes), seconds))

def randomRoll(inputList):
    """
    Returns a random element from the given list
    """
    seed(perf_counter())
    return(choice(inputList))

""" Deprecated """

# def setupLogging(fileName):
#     logDir = '\\log\\'
#     # logFile = f"{orig_func.__name__}.log"
#     logFile = fileName
#     # print(f"Checking Log {logFile}...")
#     try:
#         logging.basicConfig(
#         filename = logFile,
#         level = logging.INFO,
#         format = '%(asctime)s %(message)s',
#         datefmt = '[%B %d, %Y] %H:%M:%S'
#         )
#     except FileNotFoundError:
#         newPath = os.path.abspath(os.getcwd() + logDir)
#         print(f"New Path: {newPath}")
#         if not os.path.exists(newPath):
#             print(f"{timeStamp()} Creating missing directory: {newPath}")
#             os.makedirs(newPath)
#         if not os.path.exists(f"{newPath}{logFile}"):
#             print(f"Creating missing file: '{logFile}'")
#             open(os.path.join(newPath, logFile), 'w').close()
