import matplotlib.pyplot as plt
#Matplotlib Temperatures
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 24, 19, 23, 25, 27, 20]

plt.plot(days, temperatures, marker='o', color='blue', linestyle='-', linewidth=2, markersize=6)
plt.title('Temperature Over a Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.show()
