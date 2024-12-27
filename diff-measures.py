def areaTriangle(b, h):
    return 0.5 * b * h

base = int(input("Enter the value of triangle's base: "))
height = int(input("Enter the value of triangle's height: "))
print('Area of triangle = ', (areaTriangle(base, height)))

def areaSquare(l):
    return l*l

length= int(input("Enter the length of square: "))
print('Area of square = ', (areaSquare(length)))

def areaRectangle(l,b):
    return l*b

lengthRec= int(input("Enter the length of the rectangle: "))
breadthRec= int(input("Enter the breadth of the rectangle: "))
print('Area of rectangle = ', (areaRectangle(lengthRec,breadthRec)))

def areaCube(c):
    return c*c*c

cu= int(input("Enter the value to calculate the cube: "))
print('Cube = ', areaCube(cu))

def areaCircle(r):
    return 3.14*r*r

cir= int(input("Enter the radius of cirlce: "))
print('Area of circle = ', areaCircle(cir))