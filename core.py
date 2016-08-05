import sys
import os
from datetime import datetime
import logging


# Get available disk space
def free_space():
    st = os.statvfs(".")
    du = st.f_bavail * st.f_frsize
    return du

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

class Location:

    def __init__(self):
        self.lat = 0
        self.lng = 0
        self.alt = 0
        self.time = datetime.now()

    @capture_ex
    def update(self,gpsline):

        toks = gpsline.split(',')

        if toks[6] != "0":
            self.time = datetime.strptime(toks[1][:6],"%H%M%S")
            lng_s = 1 if toks[3] == 'N' else -1
            lat_s = 1 if toks[5] == 'E' else -1
            self.lat = parse_degrees(toks[2]) * lng_s
            self.lng = parse_degrees(toks[4]) * lat_s
            self.alt =float(toks[9])

    def __repr__(self):
        return str.format("{2}:{0},{1}", self.lat, self.lng,self.time)

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

