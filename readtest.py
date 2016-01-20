__author__ = 'Matt Cordoba'
from MainChassis import MainChassis
import time
SLEEP_TIME = 1
def main():
    m = MainChassis()
    m.updateSensorMetaData()
    while(True):
        #print(m.getSensorData())
        m.getAndPushSensorData()
        #uncomment after reading test is complete m.getAndPushSensorData()
        time.sleep(SLEEP_TIME)
if(__name__ == '__main__'): #for multiprocessing library in case we use it.
    main()