import matplotlib.pyplot as plt
import random
#PieChart!
categories = ['A','B', 'C', 'D']
values = [random.randint(10,100) for _ in range(len(categories))]

plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)

plt.axis('equal')

plt.title('Random Generated Pie')

plt.show()