class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

length = int(input("Please give the length of the rectangle:"))
width = int(input("Please give the width of the rectangle:"))
newRectangle = Rectangle(length, width)
print('the area of the input rectang is', newRectangle.area())