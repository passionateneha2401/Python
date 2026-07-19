'''
Design a Python application that creates two threads.
Thread 1 should compute the sum of elements from list.
Thread 2 shloud  compute the product of elements from the same list.
Return the results to main thread and display them.
'''
import threading

def Sum(no):
    total = 0
    for i in no:
        total = total + i
    print("Addition of all elements in list is : ",total)

def Product(no):
    product = 1
    for i in no:
        product = i * product
    print("Product of all elements in list is : ",product)

def main():
    value = int(input("Enter number of elements : "))
    lst = []

    for i in range(value):
        num = int(input("Enter number : "))
        lst.append(num)
    print("List of numbers is : ",lst)

    t1 = threading.Thread(target=Sum,name="Sum of elements in list",args=(lst,))
    t2 = threading.Thread(target=Product,name="Product of elements in list",args=(lst,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()