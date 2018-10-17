# coding: utf8
import rectangles
import paralelogram

#square2 = rectangles.Square(2)
p2 = paralelogram.Parallelogram(2, 2, 45)
d2 = paralelogram.Dimond(2, 45)

#print(square2.summary())
#print(type(square2))
#print(isinstance(square2, rectangles.Rectangle))#sprawdza czy obiekt jest obiektem tej klasy prawda lub fałsz

print(p2.summary())
print(p2)
print(d2.summary())
print(d2)

