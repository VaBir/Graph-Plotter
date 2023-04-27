import matplotlib.pyplot as plt

x1 = [2, 4, 5, 6, 8]
y1 = [2, 3, 6, 7, 9]



plt.plot(x1, y1, color = 'green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor='blue', markersize=12, label= 'line 1')

x2 = [1, 2, 4, 6, 12]
y2 = [0, 1, 4, 6, 11]

plt.plot(x2, y2, label= 'line 2')

plt.ylim(1,10)
plt.xlim(1,10)


plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph')
plt.legend()

plt.show()