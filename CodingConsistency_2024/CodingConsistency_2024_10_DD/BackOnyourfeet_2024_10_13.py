#Forgot to code yesterday, i need to try and revise again

class SimplePrint():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def printingVariables(self):
        print(f"This is x = {self.x}\nThis is y = {self.y}")

obj = SimplePrint("Text1","Text2")
obj.printingVariables()

