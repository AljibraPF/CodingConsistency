import matplotlib.pyplot as plt

#Matplotlib Histograms

data = [12, 15, 14, 17, 19, 21, 18, 20, 22, 25, 24, 23, 18, 15, 16, 21, 23]

#Blue is the default color, changed it to green to see what it looks like
plt.hist(data, bins=5, color='green', edgecolor='black')

plt.title('Histogram')
plt.xlabel('Value X')
plt.ylabel('Value Y')

plt.show()