fruit = ["Apple","Orange","Pineaple"]

for i in fruit:
    print(i)


def findLargest(numbers):
    TheLargest = numbers[0]

    for number in numbers:
        if number > TheLargest:
            TheLargest = number
    return TheLargest


x = [10,20,30,40,15,120,21]
print(f"Biggest Number Is {findLargest(x)}")
