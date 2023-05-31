import numpy as np 
import matplotlib.pyplot as plt

class Neuron:  
    def __init__(self, n_inputs, n_value, bias = 0., weights = None):  
        self.b = bias
        self.n_value = n_value
        if weights == None: self.ws = np.random.rand(n_inputs)
  
    def _f(self, x): #activation function (here: leaky_relu)
        return max(x*.1, x)   
        
def createLayer(layer1, layer2):
    sum = 0
    indexOfWeight = 0
    for indexL2 in layer2:
       for indexL1 in layer1:
           sum = indexL1.n_value * indexL2.ws[indexOfWeight]
           indexOfWeight += 1
       indexL2.n_value = indexL2._f(sum + indexL2.b)    
       indexOfWeight = 0
       sum = 0
            
def sig(x):
    return 1/(1 + np.exp(-x))          

def checkBinary(x):
    if x > 0.5:
        return 1
    else:
        return 0

points = []
   
    
def printLayer(layer, typeOfLayer, x, y):
    subArray = []
    plt.text(x - 22.5,y + 15,typeOfLayer)
    for i in layer:
        plt.scatter(x,y, s=500, color="black")
        subArray.append((x,y))
        y -= 25
    points.append(subArray)
    
def makeLine(arr1, arr2):
    for i in arr1:
        for k in arr2:
            plt.plot([i[0],k[0]],[i[1],k[1]],color="red")
 

first_layer = [Neuron(0,1), Neuron(0,1), Neuron(0,1)]
second_layer = [Neuron(3,0), Neuron(3,0), Neuron(3,0), Neuron(3,0)]
createLayer(first_layer, second_layer)
thrid_layer = [Neuron(4,0), Neuron(4,0), Neuron(4,0), Neuron(4,0)]
createLayer(second_layer,thrid_layer)
outPutLayer = [Neuron(4,0)]
createLayer(thrid_layer, outPutLayer)
outPutLayer[0].n_value = sig(outPutLayer[0].n_value)
outPutAnswers = [1]

printLayer(first_layer,"Input Layer",25,160)
printLayer(second_layer, "Hidden layer - 1", 85, 175)
printLayer(thrid_layer,"Hidden layer - 2",145,175)
printLayer(outPutLayer,"output layer",205,135)
makeLine(points[0],points[1])
makeLine(points[1],points[2])
makeLine(points[2],points[3])


plt.xlim(0, 250)
plt.ylim(0, 250)

plt.show()




    

    
    
    

