class AppendingLists:
    def __init__(self) -> None:
        self.Lists = []
    
    def appendingLists(self,items):
        self.Lists.append(items)
    
    def returningData(self):
        return self.Lists


myList = AppendingLists()
myList.appendingLists("Wrench")
myList.appendingLists("Toolbox")
x = myList.returningData()
print(x)

# OOP Paradigm to append an item to a lists