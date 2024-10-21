import matplotlib.pyplot as plt

# Inputting matplotlib scatter data

x = [float(num) for num in input("Enter x values separated by spaces: ").split()]
y = [float(num) for num in input("Enter y values separated by spaces: ").split()]

plt.scatter(x, y, color='green', marker='x', s=100)  

plt.title("Modified Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)

plt.show()

