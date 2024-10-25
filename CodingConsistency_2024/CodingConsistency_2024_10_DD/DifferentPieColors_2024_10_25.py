import matplotlib.pyplot as plt
import random
#Random Pie Colors with Random Assigned Labels!
labels = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
sizes = [random.randint(5, 25) for _ in range(len(labels))]
colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in labels]  

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})

plt.title('Fruit Distribution')

plt.show()
