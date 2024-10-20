import matplotlib.pyplot as plt
#Simple matplotlib code but with input
x = input("Enter X value sep by comma (ex: 1,2,3): ")
y = input("Enter Y value sep by comma (ex: 1,2,3): ")

x = list(map(float, x.split(',')))
y = list(map(float, y.split(',')))

plt.plot(x, y, marker='o', linestyle="-", color='b')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot')

plt.show()