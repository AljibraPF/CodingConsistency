class ForLoop:
    def __init__(self,x=50):
        self.x = x
    
    def forLoop(self):
        for i in range(self.x):
            print(f"iteration {i + 1}")

a = ForLoop()
print(a.forLoop())

#OOP mixed with a for loop