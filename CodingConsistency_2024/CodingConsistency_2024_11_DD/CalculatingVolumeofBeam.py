#Calculating Volume of Beam

class BeamVolume:
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
    def Calculating(self):
        return self.length * self.width * self.height


obj = BeamVolume(20,20,30)
print(obj.Calculating())