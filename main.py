#Imports
import rectangles
import paralelogram
import triangle
import circle

#Maths
import matplotlib.pyplot as plt
from numpy import *

#Data
R = 9
a = 13
b = 9
k = pi/6

#Shapes
r2 = rectangles.Rectangle(a, b)#rectangle
s2 = rectangles.Square(a)#square
p2 = paralelogram.Parallelogram(a, b, k)#parallelogram
d2 = paralelogram.Dimond(a, k)##dimond
t2 = triangle.Triangle(a, b, k)#triangle
c2 = circle.Circle(R)#circle

print( p2, p2.summary(), "\n", d2, d2.summary(),"\n" ,t2, t2.summary(),"\n", c2, c2.summary(),"\n", s2, s2.summary(),"\n", r2, r2.summary())

#pictures

#circle
i = arange(0, 2 * pi, .01)
x = R * sin(i)
y = R * cos(i)
plt.plot(x, y)
plt.title("Circle")
plt.show()

#rectangle
plt.plot([0,b],[0,0])
plt.plot([0,b],[a,a])
plt.plot([0,0],[0,a])
plt.plot([b,b],[0,a])
plt.title("Rectangle")
plt.show()

#square
plt.plot([0,a],[0,0])
plt.plot([0,a],[a,a])
plt.plot([0,0],[0,a])
plt.plot([a,a],[0,a])
plt.title("Square")
plt.show()

#parallelogram
plt.plot([0,b], [0,0])
plt.plot([cos(k)*a, b+cos(k)*a], [sin(k)*a, sin(k)*a])
plt.plot([0, cos(k)*a],[0,sin(k)*a])
plt.plot([b, b+cos(k)*a], [0, sin(k)*a])
plt.title("Parallelogram")
plt.show()

#triangle
plt.plot([0,a * cos(k)], [0, a * sin(k)])
plt.plot([0, b], [0,0])
plt.plot([a*cos(k), b], [a * sin(k), 0])
plt.title("Triangle")
plt.show()

