from datetime import date

class Human:
    def __init__(self,name,country,doy): #doy is date of year
        self.name = name
        self.country = country
        self.doy = doy

    def currentAge(self):
        today = date.today()
        current_year = today.year
        return current_year - self.doy

    
obj = Human("Alif","Indonesia", 2007)
print(obj.currentAge())



# Gets the current year
'''
from datetime import date

today = date.today()

x = today.year

print(x)
'''