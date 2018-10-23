#Imports
import rectangles
import paralelogram
import triangle
import circle

#Maths
import matplotlib.pyplot as plt
import numpy as np

#Data
R = 1
a = 1
b = 2
k = np.pi/3

#Shapes
r2 = rectangles.Rectangle(a, b)#rectangle
s2 = rectangles.Square(a)#square
p2 = paralelogram.Parallelogram(a, b, k)#parallelogram
d2 = paralelogram.Dimond(a, k)##dimond
t2 = triangle.Triangle(a, b, k)#triangle
c2 = circle.Circle(R)#circle

if k > np.pi/2:
    print("There is no dimond, rectangle and square with such an angle")
    # parallelogram
    plt.plot([0, b], [0, 0])
    plt.plot([np.cos(k) * a, b + np.cos(k) * a], [np.sin(k) * a, np.sin(k) * a])
    plt.plot([0, np.cos(k) * a], [0, np.sin(k) * a])
    plt.plot([b, b + np.cos(k) * a], [0, np.sin(k) * a])
    plt.title("Parallelogram")
    plt.show()

    # circle
    i = np.arange(0, 2 * np.pi, .01)
    x = R * np.sin(i)
    y = R * np.cos(i)
    plt.plot(x, y)
    plt.title("Circle")
    plt.show()

    # triangle
    plt.plot([0, a * np.cos(k)], [0, a * np.sin(k)])
    plt.plot([0, b], [0, 0])
    plt.plot([a * np.cos(k), b], [a * np.sin(k), 0])
    plt.title("Triangle")
    plt.show()

    print(p2, p2.summary(), "\n", t2, t2.summary(), "\n", c2, c2.summary())

else:
    print( p2, p2.summary(), "\n", d2, d2.summary(),"\n" ,t2, t2.summary(),"\n", c2, c2.summary(),"\n", s2, s2.summary(),"\n", r2, r2.summary())

    #pictures

    #circle
    i = np.arange(0, 2 * np.pi, .01)
    x = R * np.sin(i)
    y = R * np.cos(i)
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
    plt.plot([np.cos(k)*a, b+np.cos(k)*a], [np.sin(k)*a, np.sin(k)*a])
    plt.plot([0, np.cos(k)*a],[0, np.sin(k)*a])
    plt.plot([b, b + np.cos(k)*a], [0, np.sin(k)*a])
    plt.title("Parallelogram")
    plt.show()

    #triangle
    plt.plot([0,a * np.cos(k)], [0, a * np.sin(k)])
    plt.plot([0, b], [0,0])
    plt.plot([a * np.cos(k), b], [a * np.sin(k), 0])
    plt.title("Triangle")
    plt.show()

