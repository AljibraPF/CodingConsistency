listHewan = []

def appendingList(x):
    listHewan.append(x)

while True:
    TestPa = input("InputData Here:")
    appendingList(TestPa)
    print(listHewan)
    Inputing = int(input("Continue? 1 Continue, 2 Exit: "))
    if Inputing == 1:
        print("Continue on then!")
        continue
    elif Inputing == 2:
        print("Alright bye bye!")
        break
    else:
        print("Thats not a number!")