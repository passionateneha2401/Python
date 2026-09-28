def Marvellous_MSE(Y_True, Y_Pred):
    n = len(Y_Pred)
    total_error = 0

    for i in range(n):
        error = Y_True[i] - Y_Pred[i]
        total_error = total_error + (error**2)

    MSE = total_error / n
    return MSE

Y_True = [10,20,30]
Y_Pred = [12,18,33]

loss = Marvellous_MSE(Y_True, Y_Pred)

print("Loss is : ",loss)