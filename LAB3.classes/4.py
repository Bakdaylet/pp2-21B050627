from math import*
class Point:
     def __init__(self, x1, y1):
          self.x1 = x1
          self.y1 = y1
     def show(self):
         print(f'{self.x1, self.y1}')    
     def move(self, x2, y2):
         self.x1 += x2
         self.y1 += y2 
     def dist(self, x2, y2):
         return sqrt((x2 - self.x1)**2 + (y2 - self.y1)**2)
x1, y1 = map(int, input().split())
p2 = Point(x1, y1)
p2.show()
x2, y2 = map(int, input().split())
p2.move(x2, y2)
p2.show()
print(p2.dist(x2, y2))