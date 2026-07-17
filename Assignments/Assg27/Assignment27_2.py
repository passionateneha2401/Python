'''
2.Write a Python to implement a class named BookAccount with following specifications : 
The class should contain two instance var:
    Name(Account holder Name)
    Author(Account balance)
The class should contain one class variable : 
    ROI(Rate of Intrest)initialize it to 10.5
Define a constuctor(__init__) that accepts Name and Amount.
Implement the following instance mthods:
    Display() - displays account holder name and current balance.
    Deposit() - accepts and amount from the user and adds it toblanace
    Withdraw() - accepts an amount from user and subtracts it from balance
    (Ensure withdrawl is allwed oy=ly if sufficient balance exists)
    CalculateIntrest() - cal and returns intrest using formula:
    Intrest = (Amount * ROI) / 100
Create multiple objects and demonstrate all methods.
'''

class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.balance = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.balance)

    def Deposit(self):
        amount = float(input("Enter amount to deposit : "))
        self.balance += amount
        print("Deposit Successful")

    def Withdraw(self):
        amount = float(input("Enter amount to withdraw : "))

        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.balance * BankAccount.ROI) / 100
        return interest


obj1 = BankAccount("Neha", 50000)

obj1.Display()

obj1.Deposit()
obj1.Display()

obj1.Withdraw()
obj1.Display()

print("Interest :", obj1.CalculateInterest())