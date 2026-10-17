import numpy as np

def ReLU(z):
    return max(0,z)

def Marvellous_Neuron_Forword(inputs, weights, bias):
    print("Inputs are (X) : ",inputs)
    print("Weights are (W) : ",weights)
    print("bias (b): ",bias)

    z = 0

    for i in range(len(inputs)):
        z = z + (inputs[i] * weights[i])

    z = z + bias

    # z = sum(w * x for w, x in zip(weights,inputs)) + bias

    print("Wighted sum : ",z)

    y = ReLU(z)

    return y

def main():
    print("---- Marvellous Neural Network ----")

    inputs = [1.0,2.0,3.0]
    weights = [0.6,0.4,-0.2]
    bias = 0.5

    result = Marvellous_Neuron_Forword(inputs,weights,bias)

    print("Predicted result : ",result)
    
if __name__ == "__main__":
    main()