'''
1.Write a Python to implement a class named BookStore with following specifications : 
The class should contain two instance var:
    Name(Book Name)
    Author(Book Author)
The class should contain one class variable : 
    NoOfBooks(initialize it to 0)
Define a constuctor(__init__) that accepts Name and Author and initializes inst var.
Inside the constructor, increment class variable NoOfBooks by 1 wherever a new object is 
created.
Implement and instance method : 
    Display() - should display book details in format:
    <BookName> by <Authod>.No of books : <NoOfBooks>
Example usage:

obj1 = BookStore("Linux system programming","Robert Love")
obj1.Dsiplay()   #Linux system programming by Robert Love. No of books: 1

obj2 = BookStore("C programming","Dennis Ritchie")
obj2.Dsiplay()   #C programming by Dennis Ritchie. No of books: 2
'''

class BookStore:

    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author

        BookStore.NoOfBooks += 1
    
    def Display(self):
        print(self.Name, "by" , self.Author, ". No of books: ",BookStore.NoOfBooks)


obj1 = BookStore("Linux system programming","Robert Love")
obj1.Display()   #Linux system programming by Robert Love. No of books: 1

obj2 = BookStore("C programming","Dennis Ritchie")
obj2.Display()   #C programming by Dennis Ritchie. No of books: 2