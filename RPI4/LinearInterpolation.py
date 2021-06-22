#Cette classe permet d'approximer une fonction non-linéaire avec une méthode qui s'appelle l'interpolation linéaire
#Pour en savoir plus: https://en.wikipedia.org/wiki/Linear_interpolation
#Pour utiliser cette classe, l'interpolation linéaire requiert une liste de points (x,y) connus et valides d'un système qui n'est pas linéaire
#Pour savoir la valeur entre deux points (y = ? , x = "entre deux x connues"),
#On assume une relation linéaire entre ces deux points,
#on trouve la fonction linéaire entre les deux points et 
#on applique le x "entre deux x connue".
#Bref, ceci permet d'approximer une courbe non linéaire non connue à partir de données connues.
class LinearInterpolation():
    #Constructeur de la classe LinearInterpolation
    #La taille des tableaux xArray et yArray doivent être de même taille
    #@param xArray le tableau(List) des valeurs en x en ordre décroissant (x1>x2>x3>...>xn)
    #@param yArray le tableau(List) des valeurs en y dans l'ordre qui correspond au x
    def __init__(self, xArray, yArray):
        self._xArray = xArray
        self._yArray = yArray
    
    #@param x une valeur quelconque ou une valeur dont l'image (co-domaine) est inconnue
    #@return approximation de la valeur correspondant à x par interpolation linéaire 
    def getY(self, x):
        y = 0
        if(x > self._xArray[0]):
            y = self.lerp(self._xArray[0],self._xArray[1],self._yArray[0],self._yArray[1],x)
        elif (x < self._xArray[len(self._xArray) - 1]):
            max = len(self._xArray)-1
            y = self.lerp(self._xArray[max-1],self._xArray[max],self._yArray[max-1],self._yArray[max],x)
        else:
            for i in range(0,len(self._xArray)-2,1):
                
                if self._xArray[i] > x and x > self._xArray[i+1] or (self._xArray[i+1] ==x or x==self._xArray[i]):
                    #print(self._xArray[i] ," < ",x," < ", self._xArray[i+1])
                    y = self.lerp (self._xArray[i],self._xArray[i+1], self._yArray[i],self._yArray[i+1], x)
                    break
        if y ==0:
            print("y = 0")
        return y
    #@param x1 la valeur x du point 1
    #@param x2 la valeur x du point 2
    #@param y1 la valeur y du point 1
    #@param y2 la valeur y du point 2
    #@param x une valeur quelconque ou une valeur dont l'image (co-domaine) est inconnue
    #@return approximation de la valeur correspondant à x par interpolation linéaire à partir des deux points données
    def lerp(self,x1,x2,y1,y2,x):
        return float((y2 - y1) / (x2 - x1) * (x - x1) + y1)

