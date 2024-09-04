class CircleRadius:
    def __init__(self,circum,pi=3.14): #Remember you can put pi as a default parameter
        self.circum = circum
        self.pi = pi
    
    def radiusOfCircle(self):
        return self.circum / (2 * self.pi)

radiusinput = CircleRadius(30)
print(radiusinput.radiusOfCircle())


#Hm is this unnefficient? im practicing OOP as of right now so...
#Ack! Should probably get someone to review this for me, feedback is always important!