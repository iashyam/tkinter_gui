from math import pi, sin, cos, tan, atan

class polar:
    def __init__(self, radius, theta):
        self.radius = radius
        self.theta = theta

    def tk_coor(self, x, y):
        self.x_tk = x + 250
        self.y_tk = y - 250

    def polar(self):
        x = self.radius * cos(pi/2 -self.theta)
        y = self.radius * sin(pi/2 - self.theta)
        return 250, 350, x + 250, y -250


