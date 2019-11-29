
# M083140008
# 黃警鋒

from layoutV import *
from pointV import *
from ConvexHull import *
class Voronoi:
    def __init__(self,pointN,_pointArray):
        # self.data_pointArray = _pointArray
        # print(self.data_num_Array)

        self.pointArray =  _pointArray # 放每個點  之後會排序
        self.pointNum = pointN
        self.midlineArray = []
        self.lineArray = []
        self.drawlineArray = []
        self.sortedPointArray = []
        self.CH_Draw = []
        self.CH_Point = []

        self.combine_pointArray = []
        self.combine_drawlineArray = []
        self.combine_sortedPointArray = []
        self.combine_lineArray = []
        self.combine_CH_Draw = []
    def set_self(self,VD):
        self.pointArray = VD.pointArray
        self.drawlineArray = VD.drawlineArray
        self.sortedPointArray = VD.sortedPointArray
        self.lineArray = VD.lineArray
        self.CH_Draw = VD.CH_Draw
        self.CH_Point = VD.CH_Point
        self.combine_pointArray = VD.combine_pointArray
        self.combine_drawlineArray = VD.combine_drawlineArray
        self.combine_sortedPointArray = VD.combine_sortedPointArray
        self.combine_lineArray = VD.combine_lineArray
        self.combine_CH_Draw = VD.combine_CH_Draw
    def getandline(self):
        return self.sortedPointArray, self.lineArray
    def getPointArray(self):
        return self.pointArray
    def getDraw_line(self):
        return self.drawlineArray
    def getDraw_point_and_line(self): # 回傳要畫的圖跟線
        return self.sortedPointArray,self.drawlineArray
    def printArrayPoint(self,array):
        for i in array :
            print(i.getXY())
    def lexical_order_Point(self): # 排序
        self.pointArray.sort(key=lambda x: (x.getX(), x.getY()))
        self.sortedPointArray = self.pointArray
        # self.sortedPointArray.sort(key =lambda x:(x.getX(),x.getY()))
        # self.printArrayPoint(self.sortedPointArray)
    def lexical_order_Line(self):
        self.drawlineArray.sort(key = lambda x:(x.getp1().getX(),x.getp1().getY(),x.getp2().getX(),x.getp2().getY()))


    def run(self):
        self.lexical_order_Point()
        # print(self.pointArray)
        if self.pointNum == 1 :
            p1 = self.pointArray[0]
        elif self.pointNum == 2 :
            p1 = self.pointArray[0]
            p2 = self.pointArray[1]
            l1 = lineV(p1, p2)
            l1_V = l1.Vertical_line() # 找出中垂線
            self.midlineArray.append(l1_V)
            self.drawlineArray.append(l1_V)
            # print(self.pointArray)
            CH_test = ConvexHull(self.pointArray)
            CH_test.convexHull(self.pointNum)
            self.CH_Draw = CH_test.lineDraw
            self.CH_Point = CH_test.convexPoint
            # print('11')
        elif self.pointNum == 3 :
            CH_test = ConvexHull(self.pointArray)
            CH_test.convexHull(self.pointNum )
            self.CH_Draw = CH_test.lineDraw
            self.CH_Point = CH_test.convexPoint
            self.point_Three(0)
        else :
            # point > 3 做divide
            # self.divide(0,int(self.pointNum-1))
            print("divided")
            self.set_self(self.divide_and_merge(self))
            CH_test = ConvexHull(self.pointArray)
            CH_test.convexHull(self.pointNum)
            self.CH_Draw = CH_test.lineDraw
            self.CH_Point = CH_test.convexPoint
        self.lexical_order_Line()
        # self.reset()
    def point_Three(self,left):
        p1 = self.pointArray[left]
        p2 = self.pointArray[left+1]
        p3 = self.pointArray[left+2]
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
        l1_V = l1.Vertical_line()
        l2_V = l2.Vertical_line()
        l3_V = l3.Vertical_line()
        self.midlineArray.append(l1_V)
        self.midlineArray.append(l2_V)
        self.midlineArray.append(l3_V)
        p1_2 = l1_V.calulate_corss_lines_point(l2_V)
        p1_3 = l1_V.calulate_corss_lines_point(l3_V)
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
    def divide_and_merge(self,VD):

        print("divide_and_merge")
        print("VD, pointNUM = {:d}".format(VD.pointNum))
        if VD.pointNum <= 3 :
            VD.run()
            print("run if point < 3 ")
            return VD
        else :
            VDL_Array = []
            VDR_Array = []
            for i in range(int(VD.pointNum/2)):
                VDL_Array.append(VD.pointArray[i])
            for i in range(int(VD.pointNum/2),int(VD.pointNum)) :
                VDR_Array.append(VD.pointArray[i])
            VDLL = self.divide_and_merge(Voronoi(len(VDL_Array),VDL_Array))
            VDRR = self.divide_and_merge(Voronoi(len(VDR_Array), VDR_Array))
            return self.merge( VDLL, VDRR)
    ## merge to one VD
    def merge(self,VDL,VDR):
        print("merge")
        print("VDL pointNum = {:d}".format(VDL.pointNum))
        print("VDR pointNum = {:d}".format(VDR.pointNum))

        Merge_pointArray = []
        for i in VDL.pointArray :
            Merge_pointArray.append(i)
        for i in VDR.pointArray :
            Merge_pointArray.append(i)
        Merge_pointNum = VDL.pointNum + VDR.pointNum
        MergeV = Voronoi(Merge_pointNum,Merge_pointArray)
        MergeV.drawlineArray = VDL.drawlineArray + VDR.drawlineArray
        MergeV.sortedPointArray = VDL.sortedPointArray + VDR.sortedPointArray
        MergeV.lineArray = VDL.lineArray + VDR.lineArray
        MergeV.CH_Draw = VDL.CH_Draw + VDR.CH_Draw
        CH_test = ConvexHull(MergeV.pointArray)
        CH_test.convexHull(MergeV.pointNum)
        MergeV.CH_Point = CH_test.convexPoint
        # MergeV.pointArray = VDL.pointArray.extend(VDR.pointArray)
        # left convex
        leftConvex = VDL.CH_Point
        rightConvex = VDR.CH_Point
        ## get convexhull start and stop  where y is min and y is max
        leftminN = leftConvex.index(min(leftConvex, key=lambda x: x.getY()))
        RightminN = rightConvex.index(min(rightConvex, key=lambda x: x.getY()))
        leftmaxN = leftConvex.index(max(leftConvex, key=lambda x: x.getY()))
        RightmaxN = rightConvex.index(max(rightConvex,key = lambda x:x.getY()))
        print("leftMinN = ", leftminN)
        print("leftMaxN = " , leftmaxN )
        print("RightminN = ", RightminN)
        print("RightmaxN = ", RightmaxN )
        print("left : ")
        for i in leftConvex:
            print(i.printP())
        print ("right : " )
        for i in rightConvex:
            print(i.printP())
        back_point = None
        while True :
            leftminNext = leftminN
            RightminNext = RightminN
            if leftminN != leftmaxN : leftminNext = leftminN + 1
            if  RightminN !=  RightmaxN : RightminNext = RightminN - 1
            if leftminN == leftmaxN and RightminN ==  RightmaxN :
                break
            if leftminNext == len(leftConvex) : leftminNext = 0
            if RightminNext == -1 :RightminNext = len(rightConvex) -1
            print("leftMinN = ", leftminN)
            print("RightminN = ", RightminN)
            print("leftMinNext = ", leftminNext)
            print("RightminNext = ", RightminNext)
            midline = lineV(leftConvex[leftminN], rightConvex[RightminN]).Vertical_line()
            lineleft = lineV(leftConvex[leftminN], leftConvex[leftminNext]).Vertical_line()
            lineright = lineV(rightConvex[RightminN], rightConvex[RightminNext]).Vertical_line()
            left_p = lineleft.calulate_corss_lines_point(midline)
            right_p = lineright.calulate_corss_lines_point(midline)
            mid_p = midline.getMidPoint()
            if left_p is None :
                print("mid to right point = ", mid_p.lenlong(right_p))
                midline.setp1(right_p)
                RightminN = RightminNext
            elif right_p is None :
                print("mid to left point = ", mid_p.lenlong(left_p))
                midline.setp1(left_p)
                leftminN = leftminNext
            elif left_p is not None and right_p is not None :
                print("mid to left point = ", mid_p.lenlong(left_p))
                print("mid to right point = ", mid_p.lenlong(right_p))
                if mid_p.lenlong(left_p) < mid_p.lenlong(right_p) :
                    midline.setp1(left_p)
                    leftminN = leftminNext
                    # RightminN = RightminNext
                else :
                    midline.setp1(right_p)
                    RightminN = RightminNext
            else :
                break
            MergeV.drawlineArray.append(midline)

        return MergeV
    @staticmethod
    def next_point(max,now):
        if now == max : now = 0
        return now
    def find_line(self,VD,line):
        a = 0
        for i in VD.drawlineArray:
            if i.parent_p1 == line.parent_p1 and i.parent_p2 == line.parent_p2   :
                return a
            a += 1
        return -1
    def reset(self):
        self.pointArray = []


if __name__ == '__main__':
    print('0.0')
