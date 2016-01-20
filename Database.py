__author__ = 'Matt Cordoba'
from pymongo import MongoClient
class Database():
    def __init__(self,**unitInfo):
        self._connect()
        self._setAPIKey()
        self._setupCollections()
    def _setAPIKey(self):
        self._apiKey = 1234
        self._userDBHash = '123'
        pass
    def _sqlConnect(self):
        pass
    def _setupCollections(self):
        MONGO_DB_COLLECTIONS = {
            'currentDataCollection':'currentData_',
            'sensorDataCollection':'sensorData_'
        }
        self.collections = {}
        self.collections['DATA'] = self.db[MONGO_DB_COLLECTIONS['currentDataCollection'] + self._userDBHash]
        self.collections['SENSOR_INFO'] = self.db[MONGO_DB_COLLECTIONS['sensorDataCollection'] + self._userDBHash]
    def _connect(self):
        #TODO: make this secret
        MONGO_DB_CREDENTIALS = {
            'ENGINE': 'mongodb',
            'NAME': 'lewis',
            'USER': 'co_jsm',
            'PASSWORD': 'kushmobile',
            'HOST': 'ds039073.mongolab.com',   # Or an IP Address that your DB is hosted on
            'PORT': '39073'
        }
        URI = 'mongodb://' + MONGO_DB_CREDENTIALS['USER'] + ':' + MONGO_DB_CREDENTIALS['PASSWORD'] + \
              '@' + MONGO_DB_CREDENTIALS['HOST'] + ':' + MONGO_DB_CREDENTIALS['PORT'] +'/' + MONGO_DB_CREDENTIALS['NAME']
        self.client = MongoClient(URI)
        self.db = self.client[MONGO_DB_CREDENTIALS['NAME']]
    def _insert(self,collectionKey,dataDictArray):
        self.collections[collectionKey].insert(dataDictArray)
    def _update(self,collectionKey,query,updateDoc):
        self.collections[collectionKey].update(query,{'$set':updateDoc})
    def pushData(self,dataDictArray):
        self._insert('DATA',dataDictArray)
    def insertSensorMetaData(self,metaDataDictArray):
        self._insert('SENSOR_INFO',metaDataDictArray)
    def updateSensorMetaData(self,jsonDoc,channelNumber):
        self._update('SENSOR_INFO',{'_id':channelNumber},jsonDoc)
    def updateData(self,jsonDoc,channelNumber):
        self._update('DATA',{'_id':channelNumber},jsonDoc)
