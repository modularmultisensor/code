__author__ = 'ShayanRezaie,MattyCFireMixes,JDuece1994@hotmail.com'

from Sensor import Sensor
from TemperatureSensor import TemperatureSensor
import Adafruit_BBIO.GPIO as GPIO
from Database import Database
import commands
from ast import literal_eval
SENSOR_PINS = {0:[1,2,3,4,5,6,7,8],1:[9,10,11,12,13,14,15]}
POWER_PINS = {0:'P8_7', 1:'P8_8', 2:'P8_9', 3:'P8_10'}
CONNECTED_PINS = {0:'P9_12', 1:'P9_15', 2:'P9_23', 3:'P0_25'}
class MainChassis():
    def __init__(self):

        self.isConnected = dict()
        self.sensors = dict()
        self._configurationSensors = dict()
        self._setupPins()
        self._initPeripherals()
        self._setupDB()

    def _setupDB(self):
        #TODO: populate unitInfo kwargs
        unitInfo = dict()
        self._internalDB = Database(**unitInfo)

    def _setupPins(self):
        # set pins to GPIO.OUT and High
        for pin in POWER_PINS.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        # set Connected_pins as inputs
        for pin in CONNECTED_PINS.values():
            GPIO.setup(pin, GPIO.IN)
    #Detects if a peripheral is connected to a port or not
    def _detectPeripherals(self):
        for channelNumber,pin in CONNECTED_PINS.items():
            if GPIO.input(pin):
                # identify the p
                self.isConnected[channelNumber]= True
            else:
                self.isConnected[channelNumber]= False
    #return the number of peripherals connected
    def _initPeripherals(self):
        self._detectPeripherals()
        for channelNumber,valid in self.isConnected.items():
            if(valid):
                self._powerOffAllChannels()
                self._powerChannel(channelNumber)
                addreses = self._detectI2CBus()
                address = addreses[0] #should only be one address in this case
                self.sensors[channelNumber] = self._getSensorType(address,channelNumber)
    def _countPeripherals(self):
        return sum(self.isConnected.values())

    def _getSensorType(self,address,channelNumber):
        #TODO: actually pull what type of sensor this
        #for now lets just assume a thermocouple
        return TemperatureSensor(address,channelNumber)

    def _powerOffAllChannels(self):
        for channelNumber, powerPin in POWER_PINS.items():
            GPIO.output(powerPin,GPIO.LOW)

    def _powerChannel(self,channelNumber):
        GPIO.output(POWER_PINS[channelNumber],GPIO.HIGH)

    def _powerOnAllChannels(self):
        for channelNumber, powerPin in POWER_PINS.items():
            GPIO.output(powerPin,GPIO.HIGH)
    def _detectI2CBus(self):
        #TODO: implement way to detect I2C bus, parse output and return an array of detected addresses
        '''
        resultString = commands.getstatusoutput('i2cdetect -i 1 -l')

        foundAddresses = []
        lines = resultString.split('\n')[1:] #remove row header
        for l in lines:
            l = l.strip() #remove white space on ends
            spots = l.split(' ')[1:] #remove column header
            for s in spots:
                s = s.strip()
                if(s != 'UU' and s != '--' and s != ''):
                    foundAddresses.append(literal_eval('0x' + s))
        print(foundAddresses)
        return foundAddresses
        '''
        return [0x48]
    def read(self,channelNumber):
        if(not self.isConnected[channelNumber]):
            print('invalid...channel is not connected..returning none')
            return None
        return self.sensors[channelNumber].getData()
    def writeRawDict(self,collectionKey,jsonDocument):
        self._internalDB._insert(collectionKey,jsonDocument)
    def getSensorData(self):
        sensorData = []
        for channelNumber,sensorObj in self.sensors.items():
            if(self.isConnected[channelNumber]):
                sensorData.append(sensorObj.getData())
        return sensorData
    def getAndPushSensorData(self):
        for channelNumber,sensorObj in self.sensors.items():
            if(self.isConnected[channelNumber]):
                print('pushing data ;)')
                self._internalDB.updateData(sensorObj.getData(),channelNumber)
        #self._internalDB.pushData(self.getSensorData())
    def updateSensorMetaData(self):
        sensorInfo = []
        for channelNumber,sensorObj in self.sensors.items():
            if(self.isConnected[channelNumber]):
                print('pushing meta data')
                self._internalDB.updateSensorMetaData(sensorObj.getMetaDataInfo(),channelNumber)
        #self._internalDB.updateSensorMetaData(sensorInfo)