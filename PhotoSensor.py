__author__ = 'MattyC #1 programmer 2016'
from Sensor import Sensor
from Adafruit_I2C import Adafruit_I2C
import time
from PlotType import PlotType
class PhotoSensor(Sensor):
    def __init__(self,hexAddress,channelNumber):
        #super(PhotoSensor, self).__init__(hexAddress,channelNumber)
        self._address = hexAddress
        self.channelNumber = channelNumber
        self._internalDevice = Adafruit_I2C(hexAddress)
        self.sensorName = 'Photo Sensor V1.01'
        self.sensorReadingType = 'LIGHT'
        self.plotType = PlotType.TimeSeries
    def getData(self):
        value = self._internalDevice.readS8(self._address)
        return {'_id':self.channelNumber,'type':self.sensorReadingType,'timestamp':time.time(),'value':value}
    def getMetaDataInfo(self):
        return {'_id':self.channelNumber,'sensorName':self.sensorName,
                'sensorReadingType':self.sensorReadingType,
                'plotType':self.plotType,'lastSyncTime':time.time()}
