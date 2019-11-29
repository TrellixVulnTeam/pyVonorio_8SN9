

import tkinter as tk  # 使用Tkinter前需要先匯入
import tkinter.messagebox
from tkinter import ttk
import pickle
import win32gui
from tkinter import *
import numpy as np
from pointV import *
from tkinter import filedialog as fd
from lineV import *
from readFile import *
import random
from Voronoi import *
class layout_Voronoi :
    def __init__(self):
        self.dataArray = []
        self.pointArray = []


        self.NOW_VD_pointArray = [] # now point array
        self.NOW_VD_pointNUM = 0  # now point nul
        self.draw_point = []
        self.draw_line = []
        self.draw_point_line = []

        self.clickP_Num = 0
        self.window = tk.Tk()
        self.window.title('Voronoi')
        self.window.geometry('800x800')
        self.canvas = Canvas(self.window, width=600, height=600, bg='white')
        self.canvas.pack()
        self.label = tk.Label(self.window, text="", font=("Helvetica", 24), fg="blue")
        self.label.pack()
        ttk.Button(self.window,text='clear',command=self.clear_draw).pack(side = tk.LEFT)
        ttk.Button(self.window, text="run", command=self.run).pack(side=tk.LEFT)
        ttk.Button(self.window, text="下一筆資料", command=self.next_data).pack(side=tk.LEFT)
        ttk.Button(self.window, text="開啟檔案", command=self.open_file).pack(side = tk.LEFT) #開啟檔案
        ttk.Button(self.window, text="儲存檔案", command=self.save_file).pack(side = tk.LEFT)
        ttk.Button(self.window, text="開啟點線檔", command=self.open_PL_file).pack(side=tk.LEFT)
        ttk.Button(self.window, text="step", command=self.step_by_step).pack(side=tk.LEFT)
        ttk.Button(self.window, text="reset", command=self.reset_all).pack(side=tk.LEFT)
        self.canvas.bind('<Button-1>', self.motion)  # 滑鼠點擊

        self.canvas.create_rectangle(0,0,600,600 )

    def motion(self,event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.pointArray.append([event.x,event.y])
        self.clickP_Num += 1

        self.canvas.create_oval(x1, y1, x2, y2, fill='black') # 畫點點
        self.label.configure(text="(x, y) = (" + str(event.x) + ", " + str(event.y) + ")")

    #
    # 產生隨機顏色
    #
    def randomcolor(self):
        colorArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colorArray[random.randint(0, 14)]
        return "#" + color

    def hit_point(self,common_Point):
        m = "{0:d}點共點".format(common_Point)
        tk.messagebox.showinfo(title='Hi', message=m)
    def drawPoint(self,p1):
        x1, y1 = (p1.getX() - 1), (p1.getY() - 1)
        x2, y2 = (p1.getX() + 1), (p1.getY() + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black')  # 畫點點
    def drawlineV(self,lineV):
        self.canvas.create_line(lineV.getp1().getX(), lineV.getp1().getY(), lineV.getp2().getX(), lineV.getp2().getY(),
                                fill=self.randomcolor())
        self.canvas.pack()
    def reset_all(self):
        self.canvas.delete("all")
        self.clickP_Num = 0
        self.canvas.create_rectangle(0, 0, 600, 600)
        self.dataArray = []
        self.pointArray = []

    def clear_draw(self):
        self.canvas.delete("all")
        self.clickP_Num = 0
        self.canvas.create_rectangle(0, 0, 600, 600)
    def open_file(self):
        openfilename = fd.askopenfilename(initialdir="/", title="Select file",filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        print(openfilename)
        # try:
        reader = ReadFile(openfilename)
        reader.print_data()
        self.dataArray = reader.get_dataArray()
        self.pointArray = reader.get_pointArray()
        # self.run()
        # except:
        #     print("檔案不存在!")

    def save_file(self):
        f = fd.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        for i in self.draw_point:
            str1 = "P " + str(i.getX()) + " " + str(i.getY()) + '\n'
            f.writelines(str1)
        for i in self.draw_line :
            str1 = "E " + str(i.getp1().getX()) + " " + str(i.getp1().getY()) + " " + str(i.getp2().getX()) + " " + str(i.getp2().getY()) + '\n'
            f.writelines(str1)
        f.close()

    def open_PL_file(self):
        openfilename = fd.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        print(openfilename)
        reader = ReadFile(openfilename)
        reader.print_PL_data()
        self.draw_point = reader.get_P_array()
        self.draw_line = reader.get_L_array()
        for i in self.draw_point :
            # print(i)
            self.drawPoint(i)
        for i in self.draw_line:
            # print(i.getp1().getXY())
            self.drawlineV(i)
    def next_data(self):
        self.clear_draw()
        commonP = 0
        def check_common_point(_point):
            if _point in self.NOW_VD_pointArray:
                return True
            return None

        print('step')
        self.NOW_VD_pointNUM = int(self.dataArray[0][0])
        print(self.NOW_VD_pointNUM)
        for i in range(int(self.dataArray[0][0])):
            p = PointV(self.pointArray[0][0], self.pointArray[0][1])
            self.pointArray.remove(self.pointArray[0])
            if check_common_point(p) :
                commonP += 1
                print("{0:d}共點".format(commonP))
                self.NOW_VD_pointNUM -= 1
                print( "pppp{:d}".format(self.NOW_VD_pointNUM))
            else:
                self.NOW_VD_pointArray.append(p)
        # for i in self.pointArray:
        #     print(i.getXY())
        self.dataArray.remove(self.dataArray[0])
        if commonP != 0 :
            self.hit_point(commonP)

        # self.run()
        return 0
    def run(self):
        # for i in range(len(self.dataArray)) :
        #     voronoi.run()
        # print(self.clickP_Num)
        if self.clickP_Num is not 0 :
            self.dataArray.append([str(self.clickP_Num)])
            self.next_data()
            print("????")
            # print(self.dataArray)
        print(self.NOW_VD_pointNUM)
        voronoi = Voronoi(self.NOW_VD_pointNUM, self.NOW_VD_pointArray)
        voronoi.run()
        self.draw_point,self.draw_line = voronoi.getDraw_point_and_line()
        self.draw_point, self.draw_point_line = voronoi.getandline()

        for i in self.draw_point :
            # print(i)
            self.drawPoint(i)
            selected_rect = self.canvas.find_closest(i.getX(), i.getY())
            if selected_rect:
                colorval = "#%02x%02x%02x" % (109, 170, 44)
                self.canvas.itemconfigure(selected_rect, fill=colorval)

        for i in self.draw_line:
            # print(i.getp1().getXY())
            self.drawlineV(i)
        for i in self.draw_point_line:
            self.drawlineV(i)
        for i in voronoi.CH_Draw :
            self.drawlineV(i)
        self.clickP_Num = 0
        self.NOW_VD_pointArray.clear()
        self.NOW_VD_pointNUM = 0

    def step_by_step(self):

        return 1


if __name__ == '__main__':
    layout_Voronoi = layout_Voronoi()
    # layout_Voronoi.run()
    tkinter.mainloop()  # run GUI