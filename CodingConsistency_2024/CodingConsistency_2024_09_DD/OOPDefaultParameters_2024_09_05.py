class DefaultParam:
    def __init__(self,x=0, is_true=30, num=125, num2=125 ):
        self.x = x
        self.is_true = is_true
        self.num = num
        self.num2 = num2

    def sumDefaultParam(self):
        return self.num + self.num2
    
    def isLooping(self):
        while self.x < self.is_true:
            self.x += 1
            print(self.x)



obj = DefaultParam()
print(obj.sumDefaultParam())
obj.isLooping()

#Coding Practice to play with default parameters