import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.figure(figsize=(8, 5))  # Set the size of the figure
plt.plot(xpoints, ypoints, color='blue', linestyle='--', marker='o', markersize=8, label='Data Line')  # Customizing line and markers

plt.title('Simple Data Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.legend()

plt.show()

#Basics of Matplotlib, basics of basic! Doesn't cover everything though