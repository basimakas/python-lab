square_area=lambda a:a**2
rectangle_area=lambda l,b:l*b
triangle_area=lambda ba, h: 0.5 * ba * h
a=int(input("enter the length"))
print("Area of the square :",square_area(a))
l=int(input("enter the length"))
b=int(input("enter the breadth"))
print("Area of the rectangle :",rectangle_area(l,b))
ba=int(input("enter the base "))
h=int(input("enter the height"))
print("Area of the triangle :",triangle_area(ba,h))
