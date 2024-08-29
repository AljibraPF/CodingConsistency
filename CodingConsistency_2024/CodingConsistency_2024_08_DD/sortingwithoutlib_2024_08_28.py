def sortingFunction(Listsofnumbers):
    total = 0
    for i in Listsofnumbers:
        total += i
    return total

valuesSum = []

while True:
    listvalues = int(input("Input Nomor: "))
    valuesSum.append(listvalues)
    print(valuesSum)
    Choices = int(input("1 To Continue, 2 To Show all, Break, and sum: "))
    if Choices == 1:
        continue
    elif Choices == 2:
        tupleProblem = tuple(valuesSum)
        sortingFunction(tupleProblem)
        break
    else:
        print("Wrong Number!")

print(sortingFunction(tupleProblem))

