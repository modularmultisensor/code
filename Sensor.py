__author__ = 'mcordoba'
__author__ = 'SRezaie'
#base class for all peripheral sensors
from threading import Thread,Lock
import time
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C
class Sensor():
    def __init__(self,hexAddress,channelNumber):
        self.isConnected = None
        self.channelNumber = channelNumber
        self._address = hexAddress
    """
    this function gets the ID of the peripheral connected
    :param freqPinNumber: The frequency pin number used to identify the peripheral
    """
    def getID(self):
        return self._address


    def getData(self, freqPinNumber):
        raise NotImplementedError
    def getMetaDataInfo(self):
        raise NotImplementedError
    '''
    def _startInternalLogThread(self):
        self._currentValuesDict = dict()
        self._currentValuesLock = Lock()
        activeMessagesThread = Thread(target=self._internalLogThread)
        activeMessagesThread.daemon = True
        activeMessagesThread.start()

    def _internalLogThread(self):
       while True:
            t0 = time.clock()
            self._currentValuesLock.acquire()
            self._currentValuesDict = self._getData()
            self._currentValuesLock.release()
            timeLeft = t0 + self.LOG_SPEED - time.clock()
            if(timeLeft > 0):
                time.sleep(timeLeft)
    '''