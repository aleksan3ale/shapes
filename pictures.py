import matplotlib.pyplot as plt
from numpy import *

#circle
R = 9
i = arange(0, 2 * pi, .01)
x = R * sin(i)
y = R * cos(i)

plt.plot(x, y)
plt.title("title")
plt.legend("legend")
plt.show()

#rectangle
a = 13
b = 9

plt.plot([0,b],[0,0])
plt.plot([0,b],[a,a])
plt.plot([0,0],[0,a])
plt.plot([b,b],[0,a])
plt.show()

#square
plt.plot([0,a],[0,0])
plt.plot([0,a],[a,a])
plt.plot([0,0],[0,a])
plt.plot([a,a],[0,a])
plt.show()

#parallelogram
k = pi/6
plt.plot([0,b], [0,0])
plt.plot([cos(k)*a, b+cos(k)*a], [sin(k)*a, sin(k)*a])
plt.plot([0, cos(k)*a],[0,sin(k)*a])
plt.plot([b, b+cos(k)*a], [0, sin(k)*a])
plt.show()

#triangle
plt.plot([0,a * cos(k)], [0, a * sin(k)])
plt.plot([0, b], [0,0])
plt.plot([a*cos(k), b], [a * sin(k), 0])
plt.show()