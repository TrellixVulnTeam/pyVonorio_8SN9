
import layoutV
from pointV import *
from lineV import *
class ReadFile:
    def __init__(self, path):
        self.path = path
        self.data = ''
        self.dataArray = []
        self.pointArray = []
        self.P_array = []
        self.L_array = []
    def print_PL_data(self):
        with open(self.path, 'r') as f:
            for line in f:
                item = line.strip().split(' ')
                if item[0] == 'P':
                    p1 = PointV(item[1],item[2])
                    self.P_array.append(p1)
                elif item[0] == 'E' :
                    p1 = PointV(item[1],item[2])
                    p2 = PointV(item[3],item[4])
                    l1 = lineV(p1,p2)
                    self.L_array.append(l1)
    def print_data(self):
        NumPoint = False
        with open(self.path, 'r') as f:
            for line in f:
                if  line[0] == '#' or line[0] == '\n':
                    continue
                item = line.strip().split(' ')
                if len(item) == 1 :
                    if item[0] == '0':
                        break
                    self.dataArray.append(item)
                else :
                    self.pointArray.append(item)
    def get_dataArray(self):
        return self.dataArray
    def get_pointArray(self):
        return self.pointArray
    def get_P_array(self):
        return self.P_array
    def get_L_array(self):
        return self.L_array
if __name__ == "__main__":
    reader = ReadFile("test1.txt")
    reader.print_data()
    print(reader.get_dataArray())
    print(reader.get_pointArray())