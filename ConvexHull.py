from lineV import *
class ConvexHull:
    def __init__(self,_pointArray):
        self.pointArray = _pointArray
        self.convexPoint = []
        self.lineDraw = []
    @staticmethod
    def cross(p,q,r): # 判斷旋轉方向
        return (q.y - p.y ) * (r.x - q.x) - (q.x - p.x) * (r.y-q.y)
        # return (pa.getX()-po.getX())*(pb.getY()-po.getY())-(pa.getY()-po.getY())*(pb.getX()-po.getX())
    def convexHull(self,right):
        print ( "ConvexHull")
        # self.pointArray.insert(left,PointV(0,0))
        l = 0
        for i in range(right):
            if self.pointArray[i].getX() < self.pointArray[l].getX() :
                l = i
        Start_P = l
        Swap_P = -1
        while  Swap_P != l  :
            self.convexPoint.append(self.pointArray[Start_P])
            # print("convexPoint={:d}".format(len(self.convexPoint)))
            Swap_P = (Start_P+1)%right
            for i in range(right):
                if ConvexHull.cross(self.pointArray[Start_P],self.pointArray[i],self.pointArray[Swap_P]) < 0 :
                    Swap_P = i
                    # print ("逆時針{:d}".format(i))
                #else
                    # print("順時針")
            Start_P = Swap_P
        # del self.convexPoint[0]
        for i in range(1,len(self.convexPoint),1):
            # print(self.convexPoint[i-1].printP())
            self.lineDraw.append(lineV(self.convexPoint[i-1], self.convexPoint[i]))
        self.lineDraw.append(lineV(self.convexPoint[len(self.convexPoint)-1], self.convexPoint[0]))
