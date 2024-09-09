from datetime import date

today = date.today()

x = today.year

print(x)




'''
from datetime import date

class Human:
    def __init__(self,name,country,doy): #doy is date of year
        self.name = name
        self.country = country
        self.doy = doy

    def currentAge(self):
        return self.currentYear - self.doy

    
obj = Human("Alif","Indonesia", 2021)
'''