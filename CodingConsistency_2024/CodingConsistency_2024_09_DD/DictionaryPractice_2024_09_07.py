diction = {
    "Key": "Value",
    "Boolean": True,
    "integers": 2007,
    "Listings": ["List1","List2","List3"]
}

#Will print keys and values of diction
print(f"{diction}\n")

#Will Insert a key and a value to diction
diction["InsertKey"] = "InsertedValue"

#Will Show Updated dictionary because of inserted key
print(f"{diction} \n")

#Updates boolean key value
diction["Boolean"] = False

#Updated dictionary
print(f"{diction} \n")

#Removes the listings key and outputs Updated Dictionary
diction.pop("Listings")
print(diction)


