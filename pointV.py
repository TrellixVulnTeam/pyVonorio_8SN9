import math
class PointV :
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.cw = 0
        self.ccw = 0
    def getXY(self):
        return self.x, self.y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def printP(self):
        return "(" + str(self.x) + " "+ str(self.y) + ")"
    def __add__(self, other):
        return PointV(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return PointV(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        # print(type(other))
        return PointV(self.x / other, self.y / other)

    def __mul__(self, other):
        return PointV(self.x * other, self.y * other)
    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY() :
            return True
        return False
    def lenlong(self,other):
        a = abs(self.x - other.getX())
        b = abs(self.y - other.getY())
        c = math.sqrt(a*a + b*b)
        return c