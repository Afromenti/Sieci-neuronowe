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
def derivative_sig(x):
    sig_x = sig(x)
    return sig_x * (1 - sig_x)


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
 
def train(first, second, thrid, last,outPutAnswers):
    for i in range(0,3):
        if i==0:
            createLayer(first,second)
        elif i==1:
            createLayer(second,thrid)
        else:
            createLayer(thrid, last)
    last[0].n_value = sig(outPutLayer[0].n_value)
    if checkBinary(last[0].n_value) == 0:
            for w in range(0,len(last[0].ws)):
                last[0].ws[w] = outPutAnswers - last[0].n_value * derivative_sig(last[0].n_value) * last[0].ws[w]
            d = derivative_sig(last[0].n_value) * outPutAnswers - last[0].n_value
            if d < 0: d = d * -1
            moveBack(second,thrid,d,outPutAnswers)
            moveBack(first,second,d,outPutAnswers)
            
        
def moveBack(layer, layer2,d,outPutAnswers):
   index = 0
   for i in layer2:
        if checkBinary(i.n_value) == 0: 
            d = outPutAnswers - i.n_value
        for w in range(0,len(i.ws)):
                 i.ws[w] *= d
            
         
            
            
       
       
       
first_layer = [Neuron(0,0), Neuron(0,0), Neuron(0,0)]
second_layer = [Neuron(3,0), Neuron(3,0), Neuron(3,0), Neuron(3,0)]
thrid_layer = [Neuron(4,0), Neuron(4,0), Neuron(4,0), Neuron(4,0)]
outPutLayer = [Neuron(4,0)]
train(first_layer,second_layer,thrid_layer,outPutLayer,1)








    

    
    
    
