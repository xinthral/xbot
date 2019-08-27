def cnf(section, setting):
    import os
    from configparser import ConfigParser

    ConfigFile = os.getcwd() + "\\settings.config"

    config = ConfigParser()
    config.read(ConfigFile)
    value = config.get(section, setting)
    if value.lower() == 'true':
        return(True)
    elif value.lower() == 'false':
        return(False)
    else:
        return(value)

def Logr(orig_func, logFile = 'master.log'):
    """
    Logger Function: boilerplate wrapper to log function
     - only works on main function
     - logs into loggrs directory as {functionName}.log
    """
    import datetime
    import logging, os
    try:
        logging.basicConfig(
            filename = 'loggrs\\master.log',
            level = logging.INFO,
            format = '%(asctime)s %(message)s',
            datefmt = '[%B %d, %Y] %H:%M:%S'
        )
    except FileNotFoundError:
        newPath = os.getcwd() + "\\logr\\"
        if not os.path.exists(newPath):
            print("{} Creating missing directory: {}".format(timeStamp(), newPath))
            os.makedirs(newPath)
        if not os.path.exists("{}{}".format(newPath, logFile)):
            print("Creating missing file: 'logr\\{}'".format(logFile))
            open(os.path.join(newPath, logFile), 'w').close()
    finally:
        def wrapper(*args, **kwargs):
            logging.info(
                ':: {} ran with args: {}, and kwargs: {}'.format(
                    orig_func.__name__, args, kwargs
                )
            )
            return(orig_func(*args, **kwargs))
        return(wrapper)

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
    from datetime import datetime
    now = datetime.now()
    response = now - dtime
    return(response)

def timeDelta(dtime):
    """
    TimeDelta Function: Returns time elapsed as formatted string
    """
    from datetime import datetime
    now = datetime.now()
    changeTime = now - dtime
    minutes = changeTime.total_seconds() / 60
    seconds = changeTime.total_seconds() % 60
    return('{}:{:.2f}'.format(int(minutes), seconds))

def randomRoll(inputList):
    from time import perf_counter
    from random import choice, seed
    seed(perf_counter())
    return(choice(inputList))
