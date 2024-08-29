import random

def WholeThing():
    def randomDigits(num):
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        return digits[::-1]

    Lists = randomDigits(random.randint(4342124,4343126))

    # Make for looping that finds the number 4
    def ForLooping(x):
        v = 0
        for i in Lists:
            if i == x:
                v += 1
                print("Counting To: ", v)

    print(Lists)
    Numberstofind = int(input("Number: "))
    ForLooping(Numberstofind)

WholeThing()