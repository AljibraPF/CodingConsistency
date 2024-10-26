import matplotlib.pyplot as plt

#Monthly Expenses in matplotlib
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
expenses = [500, 450, 700, 550, 600, 650, 700, 750, 800, 650, 600, 500]

plt.figure(figsize=(10, 6))
plt.plot(months, expenses, marker='o', color='teal', linestyle='-', linewidth=2, markersize=6)

plt.title('Monthly Expenses in 2023')
plt.xlabel('Month')
plt.ylabel('Expenses ($)')
plt.grid(True, linestyle='--', alpha=0.5)  

plt.show()
