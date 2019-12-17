import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,6,9],color='red',label='First Line')
plt.plot([1,2,3],[8,4,6],color='blue',label='Second Line')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()

