__author__ = 'Shayan'
from Sensor import Sensor
from Adafruit_I2C import Adafruit_I2C
import time
from PlotType import PlotType
class TemperatureSensor(Sensor):
    def __init__(self,hexAddress,channelNumber):
        #super(TemperatureSensor, self).__init__(hexAddress,channelNumber)
        self._address = hexAddress
        self.channelNumber = channelNumber
        self._internalDevice = Adafruit_I2C(hexAddress)
        self.sensorName = 'Temperature Sensor V1'
        self.sensorReadingType = 'TEMPERATURE'
        self.plotType = PlotType.TimeSeries
    def getData(self):
        bytes = self._internalDevice.readList(self._address,2)
        value = float(bytes[0]) + float(bytes[1])/2**8
        return {'_id':self.channelNumber,'type':self.sensorReadingType,'timestamp':time.time(),'value':value}
    def getMetaDataInfo(self):
        return {'_id':self.channelNumber,'sensorName':self.sensorName,
                'sensorReadingType':self.sensorReadingType,
                'plotType':self.plotType,'lastSyncTime':time.time()}
