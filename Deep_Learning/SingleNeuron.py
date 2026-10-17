import numpy as np

# Step 1 : Define input fetures ie X
#                  [x1,x2,x3]
input = np.array([2.0,3.0,4.0])
print("X : ",input)

# Step 2 : Define weights ie w
#                    [w1,w2,w3]
weights = np.array([0.5,0.3,0.2])
print("W : ",weights)

# Step 3 : Define bias ie b
#       b
bias = 1.0
print("b : ",bias)

# Step 4 : Calculate weighted sum ie Z
# z = x1w1 + x2w2 + x3w3 + b
# z = (2.0*0.5) + (3.0*0.3) + (4.0*0.2) + 1.0

z = np.dot(input,weights) + bias
print("z : ",z)

# Step 5 : Actication function (ReLU)
def ReLU(x):
    return max(0,x)

# Step 6 : Final output
Y = ReLU(z)
print("Y : ",Y)