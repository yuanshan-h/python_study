class Rectangle:
    def area(self):
        return self.length * self.width

r = Rectangle()
r.length, r.width = 13, 8
area = r.area()
print(area)