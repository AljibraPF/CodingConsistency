class Book():
    def __init__(self,title,author,year,is_checked_out = False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def check_out(self):
        self.is_checked_out = True
        print("Check out is\n", self.is_checked_out)
    
    def return_book(self):
        self.is_checked_out = False
        print("Returning! Check out is!\n", self.is_checked_out)

    def display_info(self):
        print("The Title = ", self.title)
        print("The Author = ", self.author)
        print("The Year = ", self.year)
        print("Is Check Out = ", self.is_checked_out)


obj = Book("The Eepy!","Joe",2024)
obj.return_book()
obj.display_info()

# This OOP Practice is for checking on how to use other data types in OOP