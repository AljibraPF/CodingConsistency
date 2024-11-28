#Classes with string
class PrintSomething:
    def __init__(self, this_string):
        self.this_string = this_string
    
    def Thisisastring(self):
        print(f"This is {self.this_string}")

    def __str__(self):
        return f"This is {self.this_string}"


obj = PrintSomething("A String")
print(obj) 
