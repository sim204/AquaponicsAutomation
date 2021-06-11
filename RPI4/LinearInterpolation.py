
class LinearInterpolation():

    def __init__(self, xArray, yArray):
        self._xArray = xArray
        self._yArray = yArray
    
    def getY(self, x):
        y = 0
        if(x > self._xArray[0]):
            y = self.lerp(self._xArray[0],self._xArray[1],self._yArray[0],self._yArray[1],x)
        elif (x < self._xArray[len(self._xArray) - 1]):
            max = len(self._xArray)-1
            y = self.lerp(self._xArray[max-1],self._xArray[max],self._yArray[max-1],self._yArray[max],x)
        else:
            for i in range(0,len(self._xArray)-2,1):
                
                if self._xArray[i] > x and x > self._xArray[i+1]:
                    print(self._xArray[i] ," < ",x," < ", self._xArray[i+1])
                    y = self.lerp (self._xArray[i],self._xArray[i+1], self._yArray[i],self._yArray[i+1], x)
        return y
        
    def lerp(self,x1,x2,y1,y2,x):
        return (y2 - y1) / (x2 - x1) * (x - x1) + y1 

