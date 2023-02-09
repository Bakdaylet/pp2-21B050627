class Shape:
     def find_area(self):
         return 0
class Rectangle(Shape):
     def __init__(self, length, width):
          self.length = length
          self.width = width
     def find_area(self):
              return self.length * self.width
l, w = map(int, input().split())
rec = Rectangle(l, w)
print(rec.find_area())