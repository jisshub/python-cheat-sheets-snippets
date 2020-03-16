class Circle:
    def __init__(self, radius):
	# instance variable
        self.radius = radius
        self.pi = 3.14

class Area(Circle):
    def findArea(self):
        return f"Area: {round(self.pi * self.get_radius() * self.get_radius())}"


#
# s
class Circumference(Circle):
    def findCircum(self):
        return f"Circumference: {2 * self.pi * self.get_radius()}"


area = Area(6)
print(area.findArea())

peri = Circumference(7)
print(peri.findCircum())
