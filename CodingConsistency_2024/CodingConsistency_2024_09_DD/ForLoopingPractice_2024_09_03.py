n = 40
x = 0
y = 10


print("Stops at specific Number")

for i in range(1,n):
    print(i)
    if i == 8:
        break

print("\nEndSection\n")


print("Sums Up Every Odd Number")
for i in range(n):
    if i % 2 != 0:
        x += i

print(x)


print("A Multiplacation table")
for i in range(y):
    print("5 x ",i,"=",(i*5))