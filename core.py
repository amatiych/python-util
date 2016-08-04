import sys
import logging

def capture_ex(fun):
    """
        decorator to put try catch around a function call and print exception message
    """
    def wrapper(*args, **kwargs):
        try:
            return fun(*args,**kwargs)
        except Exception as ex:
            log.error("exception at {0} msg: {1}", fun, str(ex))
    return wrapper

def setup_logging(*,name,fileName, levelName=None):
	root = logging.getLogger()
	root.handlers = []

	log_fmt = name + ' %(asctime)s %(levelname)s:%(message)s'

	levels = {'info':logging.INFO, 'debug':logging.DEBUG, 
		 'error':logging.ERROR, 'warn':logging.WARNING}

	if (levelName in levels):
		loglevel = levels[levelName]
	else:
		loglevel = logging.INFO

	fmt = logging.Formatter(log_fmt)
	ch = logging.StreamHandler(sys.stdout)
	ch.setFormatter(fmt)
	root.addHandler(ch)

	if fileName:
		handler = logging.FileHandler(fileName)
		handler.setFormatter(fmt)
		handler.setLevel(loglevel)
		root.addHandler(handler)

	root.level = loglevel
	return root
		
			

if __name__ == '__main__':
	log = setup_logging(fileName='/home/pi/Documents/python/test.log', name='test')
	log.info("Hello There ")

