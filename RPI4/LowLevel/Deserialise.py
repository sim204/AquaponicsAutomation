import serial
import time
ANALOGPORTS = 6

#Classe qui tranforme l'information du protocole Serial à des données que le code Python peut interpréter.
#Note important quant à la convertion du protocole Serial à des données Python: le délai par cycle doit être le même que celui de l'Arduino
#Ex: Si la période d'un cycle pour l'Arduino est 100ms, le PI doit avoir ce même période de cycle
#Ceci peut être vu dans le fichier main
class Deserialise:
    __instance = None
    #Contructeur de la classe Deserialise
    #Le constructeur établi la connection Serial entre l'Arduino et le PI
    def __init__(self):
        self.processedData = [None]*ANALOGPORTS
        try:
            self.arduino = serial.Serial('/dev/ttyACM0', 9600)
            print("Connected to port0, Connecté au port0")
        except serial.SerialException as e:
            try:
                self.arduino = serial.Serial('/dev/ttyACM1', 9600)
                print("Connected to port1")
            except serial.SerialException as e:
                print("Error! No serial connection. Please Check connection.")
                self.arduino = None
    #Méthode qui lit une ligne du protocole Serial 
    def readLine(self):
        if (self.arduino is None):
            return None
        else:
            return self.arduino.readline()
    #Mise à jour des données collectées du protocole Serial
    def update(self):

        rawdata = []
        #Puisque chaque ligne correspond à un port, on prend sept ligne pour être sûr que tout les ports sont couvert
        for i in range(0,ANALOGPORTS+1):
            rawdata.append(str(self.readLine()))
        
        #Traitement des lignes reçues
        for line in rawdata:
            #print(line)
            indexCharPos = line.find('a')+1
            startCharPos = line.find(' ')+1
            if indexCharPos != 0 and startCharPos != 0 and line[indexCharPos].isdigit() and line[startCharPos].isdigit():
                index = int(line[indexCharPos])
                num = 0
                j = startCharPos
                while line[j].isdigit():
                    num = num*10
                    num = num + int(line[j])
                    #print(int(line[j]), end="")
                    j = j + 1
                
                self.processedData[index] = num
    
    #affichages des données récoltées et traitées.
    def printAll(self):
        for i in self.processedData:
            print(i)
        #print(self.processedData[0])
   
    #Donne la valeur lu d'un port Analog
    #@param port le numéro du port voulu
    #@return la valeur du port entre 0 et 1023 (0 étant 0 V et 1023 étant 5V)
    def readPort(self, port):
        return self.processedData[port]

    #@return une instance de cette classe
    @staticmethod 
    def getInstance():
        if Deserialise.__instance is None:
            Deserialise.__instance = Deserialise()
        return Deserialise.__instance
#test/debug code
if False:            
    test = Deserialise.getInstance();

    while True:
        previousTime =  time.time()
        test.printAll()
        print("processingTime: "+ str(time.time()-previousTime))
        time.sleep(0.5) #delay has to be the same as the arduino
