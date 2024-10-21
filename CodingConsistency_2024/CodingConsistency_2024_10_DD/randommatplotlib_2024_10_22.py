import matplotlib.pyplot as plt
import random
#Uses Random module as input
x = list(range(10))
y = [random.randint(1,100) for _ in range(10)]

plt.plot(x,y, marker='o', linestyle='-', color='b', label='Random Data')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Line Plot Random Data')

plt.legend()
plt.show()