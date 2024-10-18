import matplotlib.pyplot as plt
#2 Plots
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [5, 15, 10, 20, 35]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

ax1.plot(x, y1, marker='o', linestyle='-', color='blue', label='Line Plot')
ax1.set_title('Line Plot')
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y1 Values')
ax1.grid(True)
ax1.legend()

ax2.bar(x, y2, color='green', label='Bar Plot')
ax2.set_title('Bar Plot')
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y2 Values')
ax2.grid(True, axis='y')
ax2.legend()

plt.tight_layout()
plt.show()
