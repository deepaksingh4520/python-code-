class Circle:
    def _init_(self,radius,pi):
        self.radius = radius
        self.pi = pi
    def calc_circumference(self):
        return 2*self.radius*self.pi

c = Circle(4,3.14)
c1 = circle(5,3.14)
print(c.calc_circumference())
