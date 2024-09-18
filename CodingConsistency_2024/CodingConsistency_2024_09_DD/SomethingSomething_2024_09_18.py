class NameListing:
    def __init__(self,name_list) -> None:
        self.name_list = name_list

    def searchName(self,search):
        result = []
        for name in self.name_list:
            if search in name:
                result.append(name)
        return result

NameList = ["Alan", "Dylan","Archie","Aliph","Alray","Terry"]

searching_tool = NameListing(NameList)

searchName = input("Search: ")

matching_names = searching_tool.searchName(searchName)

if matching_names:
    for name in matching_names:
        print(name)
else:
    print("No matches found")


#Code to Find the start of a name in a list