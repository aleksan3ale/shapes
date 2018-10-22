import matplotlib.pyplot as plt
from numpy import *

a = 13
b = 9
#k = pi/2 jest ok
k = pi/6
#triangle
plt.plot([0,a*cos(k)], [0, a*sin(k)])
plt.plot([0, b], [0,0])
plt.plot([a*cos(k),b ], [a*sin(k), 0])
plt.show()
# repr - czytelnejszy obiekt dla programisty
# str - ładnie dla urzytkownika
#print(type(square2))
#print(isinstance(square2, rectangles.Rectangle))#sprawdza czy obiekt jest obiektem tej klasy prawda lub fałsz