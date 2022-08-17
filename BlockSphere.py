from cmath import pi


class Block:
    def __init__(self, li=[]):
        self.wid = li[0]
        self.leng = li[1]
        self.heig = li[2]

    def get_width(self):
        return self.wid

    def get_length(self):
        return self.leng

    def get_height(self):
        return self.heig

    def get_volume(self):
        return self.heig*self.leng*self.wid

    def get_surface_area(self):
        return (2*(self.leng*self.heig+self.leng*self.wid+self.wid*self.heig))


# bl = Block([2, 4, 6])
# print(bl.get_surface_area())
class Sphere(object):
    def __init__(self, r, m):
        self.radius = r
        self.mass = m

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        a = 4/3*pi*self.radius*self.radius*self.radius
        return float("%.5f" % a)

    def get_surface_area(self):
        a = 4*pi*self.radius*self.radius
        return float("%.5f" % a)

    def get_density(self):
        v = float(self.get_volume())
        a = self.mass/v
        return float("%.5f" % a)


ball = Sphere(2, 50)
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())
