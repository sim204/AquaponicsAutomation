from . import Command
import time
import mariadb


class SendToDatabase(Command.Command):
    sendDelay = 1 #delay between database data in seconds
    def __init__(self, WaterSubsystem, LightSubsystem):
        super().__init__()
        self.connection = mariadb.connect(
            user="pi",
            password = "password",
            host = "127.0.0.1",
            port = 3306)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS SensorData;")
        self.cursor.execute("USE SensorData")
        try:
            self.cursor.execute("Select * From sensordata")
        except:
            self.cursor.execute("""CREATE TABLE `sensordata` (
                `TimeStamp` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'TimeStamp of Sensor Value',
                `WaterLevel` DOUBLE NULL DEFAULT '0' COMMENT 'Water Level in mm',
                `WaterVolume` DOUBLE NULL DEFAULT '0' COMMENT 'Water Level in mL',
                `Light` int NULL DEFAULT NULL COMMENT 'Light Level in Lux'
            )
            COLLATE='latin1_swedish_ci'
            ENGINE=InnoDB;""")
        self.waterSub = WaterSubsystem
        self.lightSub = LightSubsystem
    

    def initialise(self):
        self.lastSentTimeStamp = time.time()
        
    def execute(self):
        if time.time() > self.lastSentTimeStamp + SendToDatabase.sendDelay:
            print("sent")
            self.cursor.execute("INSERT INTO sensordata (TimeStamp,WaterLevel,WaterVolume,Light) VALUES(CURRENT_TIMESTAMP,?,?,?)",
            (self.waterSub.getLevel(),self.waterSub.getVolume(),self.lightSub.getLightLevel()))
            self.lastSentTimeStamp = time.time()
            self.connection.commit()
    
    def isFinish(self):
        return False

    def end(self,isInterrupt):
        self.connection.close()
        self.cursor.close()

