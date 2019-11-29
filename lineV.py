from pointV import *

import numpy as np
import math

class lineV() :
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.parent_p1 = None
        self.parent_p2 = None
        self.len = 0
        self.l_slope = lineV.slope(self)
        self.midpoint = (self.p1 + self.p2) / 2
    def getp1(self):
        return self.p1
    def getp2(self):
        return self.p2
    def setp1(self,p1):
        self.p1 = p1
        self.l_slope = lineV.slope(self)
    def setp2(self,p2):
        self.p2 = p2
        self.l_slope = lineV.slope(self)
    def setParentP(self,p1,p2):
        self.parent_p1 = p1
        self.parent_p2 = p2
    def getl_slope(self):
        return self.l_slope
    def getMidPoint(self):
        return self.midpoint
    def getline_len(self):
        x1,y1 = self.p1.getXY()
        x2,y2 = self.p2.getXY()
        self.len = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
        # print(self.len)
        return str(self.len )
    # Get the linear equalition from p1 and p2
    def printL(self):
        return self.p1.printP() + self.p2.printP()

    def Vertical_line(self): ## 取得中垂線跟斜率
        self.midpoint = (self.p1 + self.p2) / 2 # 取得中心點
        SP = self.p2 - self.p1
        pVer = PointV(SP.getY()*-1,SP.getX())
        p1 = (pVer * (600)) + self.midpoint  ## 拿到絕對超出畫布的點
        p2 = (pVer * (-600)) + self.midpoint
        ll = lineV(p1, p2)
        ll.setParentP(self.p1,self.p2)
        return ll
    @staticmethod
    def slope(  o_line):
        # print(o_line.getp2().printP())
        # print(o_line.getp1().printP())
        slopeP = o_line.getp2() - o_line.getp1()
        if slopeP.getX() == 0 :
            return 601 # when Straighten
        return slopeP.getY() / slopeP.getX()

    def y_intercept(self, o_line,slope):
        return o_line.getp1().getY() - slope * o_line.getp1().getX()
    def intersection(self,other):
        slopeA = lineV.slope(self)
        slopeB = lineV.slope(other)
        if slopeA == slopeB and slopeA != 0 :
            print(slopeA)
            print(slopeB)
            print ( '不相交')
            return None
        y_i_A = self.y_intercept(self, slopeA)
        y_i_B = self.y_intercept(other, slopeB)
        if ( slopeA - slopeB ) != 0 :
            x = ( y_i_B -y_i_A ) / ( slopeA - slopeB )
        else :
            x = 0
        y =  slopeA * x + y_i_A
        return PointV(x,y)

    def angle(self,v1, v2):  #計算角度
        x1 = v1.getp2().getX() - v1.getp1().getX()
        y1 = v1.getp2().getY() - v1.getp1().getY()
        x2 = v2.getp2().getX() - v2.getp1().getX()
        y2 = v2.getp2().getY()  - v2.getp1().getY()
        angle1 = math.atan2(y1, x1)
        angle1 = int(angle1 * 180 / math.pi)
        angle2 = math.atan2(y2, x2)
        angle2 = int(angle2 * 180 / math.pi)
        if angle1 * angle2 >= 0:
            included_angle = abs(angle1 - angle2)
        else:
            included_angle = abs(angle1) + abs(angle2)
            if included_angle > 180:
                included_angle = 360 - included_angle
        return included_angle

    def calulate_corss_lines_point(self,other):
        l_0_a = self.getp1().getY() - self.getp2().getY()
        l_0_b = self.getp2().getX() - self.getp1().getX()
        l_0_c = self.getp1().getX() * self.getp2().getY() - self.getp2().getX() * self.getp1().getY()
        l_1_a = other.getp1().getY() - other.getp2().getY()
        l_1_b = other.getp2().getX() - other.getp1().getX()
        l_1_c = other.getp1().getX() * other.getp2().getY() -other.getp2().getX() * other.getp1().getY()
        d = l_0_a * l_1_b - l_1_a * l_0_b
        if d == 0:
            return None
        x = (l_0_b * l_1_c - l_1_b * l_0_c) * 1.0 / d
        y = (l_0_c * l_1_a - l_1_c * l_0_a) * 1.0 / d
        pointVV = PointV(x, y)
        if (pointVV.x - self.getp1().getX()) * (pointVV.x - self.getp2().getX()) <= 0 and (pointVV.x - other.getp1().getX()) * (
                pointVV.x - other.getp2().getX()) <= 0:
            return pointVV
        else:
            return None
    def Vector_cross_Inner(self,other):
        c1 = self.getp2() - self.getp1()
        c2 = other.getp2() - other.getp1()
        k = c1.getX() * c2.getX() + c1.getY() * c2.getY()
        return k
if __name__ == '__main__':
    # p1 = PointV(-2,14)
    # p2 = PointV(4,-4)
    # # p2.getXY()
    # l1 = lineV(p1,p2)
    # l1.getline_len()
    # l2 = l1.Vertical_line()
    # print(l2.getp1().getXY() )
    # print(l2.getp2().getXY() )
    p1 = PointV(1,1)
    p2 = PointV(3,3)
    p3 = PointV(1,3)
    p4 = PointV(3,1)
    l1 = lineV(p1,p2)
    l2 = lineV(p3,p4)
    p5 = l1.intersection(l2)
    p5.getXY()