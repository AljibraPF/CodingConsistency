class NumbersOnumbers:
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    def additioningSum(self):
        return self.num1 + self.num2
    
    def subtractingSum(self):
        return self.num1 - self.num2
    
    def multiplyingSum(self):
        return self.num1 * self.num2
    
    def dividingSum(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("Can't Divide By 0")

    def calculate_all(self):
        return {
            "additioning" : self.additioningSum(),
            "subtracting" : self.subtractingSum(),
            "multiplying" : self.multiplyingSum(),
            "dividing" : self.dividingSum() 
        }

x = int(input("Input 1: "))
y = int(input("Input 2: "))

calc = NumbersOnumbers(x,y)
results = calc.calculate_all()
print(results)

# Code Seems too much of an overkill for an OOP 
# I Don't think Every Code should require an OOP paradigm..
# Perhaps i should continue with the functional and procedure paradigm?
