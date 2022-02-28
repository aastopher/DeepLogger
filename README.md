# EZLogger Usage

## Installing the package

`pip3 install EZLogger`

## Configuring a logger object for a MODULE

`import EZLogger`

# Instantiate loggers
EZ = EZLogger('module_name',['function_1','function_2','function_n'])
F1Logger = logging.getLogger('function_1')
F2Logger = logging.getLogger('function_2')
FNLogger = logging.getLogger('function_n')
`

# How to use your new function loggers

* To create a new info level log line in one of your function loggers use the following pattern. (see below for additional log level options)
* `F1Logger.info('log message')`
* Each EZLogger object contains it's own StreamHandler which will allow you to print to console based on the above configuration as follows
* `EZ.console_logger('log message')`

# Log levels

* NOTSET = 0: This is the initial default setting of a log when it is created. It is not really relevant and most developers will not even take notice of this category. In many circles, it has already become nonessential. The root log is usually created with level WARNING.
* DEBUG = 10: This level gives detailed information, useful only when a problem is being diagnosed.
* INFO = 20: This is used to confirm that everything is working as it should.
* WARNING = 30: This level indicates that something unexpected has happened or some problem is about to happen in the near future.
* ERROR = 40: As it implies, an error has occurred. The software was unable to perform some function.
* CRITICAL = 50: A serious error has occurred. The program itself may shut down or not be able to continue running properly.
