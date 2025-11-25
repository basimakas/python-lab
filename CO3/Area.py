from graphics.RectFunctions import*
from graphics.CirFunctions import*
from graphics.Dgraphics.SphereFunctions import*
from graphics.Dgraphics.CuboidFunctions import*
l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))

r=int(input("enter radius of the circle:"))
print("CircleArea=",CirArea(r))
print("Circle perimeter=",CirPerimeter(r))

r=int(input("enter radius of the sphere:"))
print("Sphere Area=",SpArea(r))
print("Sphere volume=",SpPerimeter(r))


l=int(input("enter cuboid length:"))
b=int(input("enter  cuboid breadth:"))
h=int(input("enter cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid perimeter=",CubPerimeter(l,b,h))
