# M083140008
# 黃警鋒

from layoutV import *
from pointV import *
from ConvexHull import *


class Voronoi:
    def __init__(self, _dataArray, _pointArray):
        self.data_num_Array = _dataArray
        self.data_pointArray = _pointArray
        # print(self.data_num_Array)

        self.pointNum =
        self.midlineArray = []
        self.lineArray = []
        self.drawlineArray = []
        self.pointArray = []  # 放每個排序過的點
        self.sortedPointArray = []
        self.commonPoint = 0

        self.CH_Draw = []

    def getCommonPoint(self):
        return self.commonPoint

    def getandline(self):
        return self.sortedPointArray, self.lineArray

    def getDraw_point_and_line(self):  # 回傳要畫的圖跟線
        return self.sortedPointArray, self.drawlineArray

    def printArrayPoint(self, array):
        for i in array:
            print(i.getXY())

    def lexical_order_Point(self):  # 排序
        self.sortedPointArray = self.pointArray
        self.pointArray.sort(key=lambda x: (x.getX(), x.getY()))
        self.sortedPointArray.sort(key=lambda x: (x.getX(), x.getY()))
        self.printArrayPoint(self.sortedPointArray)

    def lexical_order_Line(self):
        self.drawlineArray.sort(key=lambda x: (x.getp1().getX(), x.getp1().getY(), x.getp2().getX(), x.getp2().getY()))

    @staticmethod
    def check_common_point(self, _point):
        if _point in self.pointArray:
            self.commonPoint += 1
            return True
        return False

    def run(self):
        print('run')
        pointNum = int(self.data_num_Array[0][0])
        print(pointNum)
        for i in range(int(self.data_num_Array[0][0])):
            p = PointV(self.data_pointArray[0][0], self.data_pointArray[0][1])
            self.data_pointArray.remove(self.data_pointArray[0])
            if self.check_common_point(p):
                print("{0:d}共點".format(self.commonPoint))
                pointNum -= 1
            else:
                self.pointArray.append(p)
        # for i in self.pointArray:
        #     print(i.getXY())
        self.data_num_Array.remove(self.data_num_Array[0])

        self.lexical_order_Point()
        if pointNum == 2:
            p1 = self.pointArray[0]
            p2 = self.pointArray[1]
            l1 = lineV(p1, p2)
            l1_V = l1.Vertical_line()  # 找出中垂線
            self.midlineArray.append(l1_V)
            self.drawlineArray.append(l1_V)
            # print('11')
        elif pointNum == 3:
            # CH_test = ConvexHull(self.pointArray)
            # CH_test.convexHull(0,pointNum)
            self.point_Three(0)
        else:
            # point > 3 做divide
            self.divide(0, int(pointNum - 1))
            print("divided")
            CH_test = ConvexHull(self.pointArray)
            CH_test.convexHull(pointNum)
            self.CH_Draw.extend(CH_test.lineDraw)
        self.lexical_order_Line()

        self.reset()

    def point_Three(self, left):
        p1 = self.pointArray[left]
        p2 = self.pointArray[left + 1]
        p3 = self.pointArray[left + 2]
        l1 = lineV(p1, p2)
        l1_r = lineV(p2, p1)
        l2 = lineV(p1, p3)
        l3 = lineV(p2, p3)
        self.lineArray.append(l1)
        self.lineArray.append(l2)
        self.lineArray.append(l3)
        angle1 = l1.angle(l1, l2)
        angle2 = l1.angle(l1_r, l3)
        angle3 = l2.angle(l2, l3)
        # print("angle1")
        # print(angle1)
        # print("angle2")
        # print(angle2)
        # print("angle3")
        # print(angle3)
        l1_V = l1.Vertical_line()
        l2_V = l2.Vertical_line()
        l3_V = l3.Vertical_line()
        self.midlineArray.append(l1_V)
        self.midlineArray.append(l2_V)
        self.midlineArray.append(l3_V)
        # print("l1")
        p1_2 = l1_V.calulate_corss_lines_point(l2_V)
        # print("l2")
        p1_3 = l1_V.calulate_corss_lines_point(l3_V)
        # print("l3")
        p2_3 = l2_V.calulate_corss_lines_point(l3_V)
        if p1_2 is not None:
            line_Vector_midpoint = lineV(p1_2, l1.getMidPoint())
            line_Vector_midLine_p1 = lineV(p1_2, l1_V.getp1())
            line_Vector_midLine_p2 = lineV(p1_2, l1_V.getp2())
            a = line_Vector_midpoint.Vector_cross_Inner(line_Vector_midLine_p1)
            b = line_Vector_midpoint.Vector_cross_Inner(line_Vector_midLine_p2)
            # print(a)
            # print(b)
            if angle3 < 90:
                if a < 0:
                    l1_V.setp1(p1_2)
                else:
                    l1_V.setp2(p1_2)
            else:
                if a <= 0:
                    l1_V.setp2(p1_2)
                else:
                    l1_V.setp1(p1_2)
            line_Vector_midpoint = lineV(p1_2, l2.getMidPoint())
            line_Vector_midLine_p1 = lineV(p1_2, l2_V.getp1())
            line_Vector_midLine_p2 = lineV(p1_2, l2_V.getp2())
            a = line_Vector_midpoint.Vector_cross_Inner(line_Vector_midLine_p1)
            b = line_Vector_midpoint.Vector_cross_Inner(line_Vector_midLine_p2)
            # print(a)
            # print(b)
            if angle2 < 90:
                if a < 0:
                    l2_V.setp1(p1_2)
                else:
                    l2_V.setp2(p1_2)
            else:
                if a <= 0:
                    l2_V.setp2(p1_2)
                else:
                    l2_V.setp1(p1_2)
            line_Vector_midpoint = lineV(p1_2, l3.getMidPoint())
            line_Vector_midLine_p1 = lineV(p1_2, l3_V.getp1())
            line_Vector_midLine_p2 = lineV(p1_2, l3_V.getp2())
            a = line_Vector_midpoint.Vector_cross_Inner(line_Vector_midLine_p1)
            b = line_Vector_midpoint.Vector_cross_Inner(line_Vector_midLine_p2)
            # print(a)
            # print(b)
            if angle1 < 90:
                if a < 0:
                    l3_V.setp1(p1_2)
                else:
                    l3_V.setp2(p1_2)
            else:
                if a <= 0:
                    l3_V.setp2(p1_2)
                else:
                    l3_V.setp1(p1_2)
        self.drawlineArray.append(l1_V)
        # if angle2 > 180 :
        #     self.drawlineArray.append(l2_V)
        if angle2 < 179:
            self.drawlineArray.append(l2_V)
        #     if p1_2 is not None :
        #         if not ( p1_2.getX() > 600 or p1_2.getX() < 0 or p1_2.getY() > 600 or p1_2.getY() < 0 ) :
        #             self.drawlineArray.append(l2_V)
        self.drawlineArray.append(l3_V)

    def divide(self, left, right):
        print("left={:d}".format(left))
        print("right={:d}".format(right))

        pointNum = right - left
        print("pointNUM = {:d}".format(pointNum))
        if pointNum <= 2:
            print(pointNum)
            if pointNum == 1:
                p1 = self.pointArray[left]
                p2 = self.pointArray[right]
                l1 = lineV(p1, p2)
                l1_V = l1.Vertical_line()  # 找出中垂線
                self.lineArray.append(l1)
                self.midlineArray.append(l1_V)
                self.drawlineArray.append(l1_V)
            else:
                self.point_Three(left)
                # CH_test = ConvexHull(self.pointArray)
                # CH_test.convexHull(pointNum)
                # self.CH_Draw.extend(CH_test.lineDraw)
            print("zero")
        else:
            self.divide(int(left), int((left + right) / 2))
            self.divide(int((left + right) / 2 + 1), int(right))
            # CH_test = ConvexHull(self.pointArray)
            # CH_test.convexHull(left, right)
            # self.CH_Draw.extend(CH_test.lineDraw)
            print("merge")

    def reset(self):
        self.pointArray = []


if __name__ == '__main__':
    print('0.0')
