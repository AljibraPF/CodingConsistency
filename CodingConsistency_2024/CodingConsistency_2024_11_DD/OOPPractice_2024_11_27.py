#Practicing Classes 

class Registering:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def descriptioning(self):
        print(f"My name is {self.name} and my age is {self.age}")


obj = Registering("Al","17")
obj.descriptioning()