import random
import turtle


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)


class Line():
    def __init__(self, point1, point2, tur):
        self.point1 = point1
        self.point2 = point2
        self.tur = tur

    def draw(self, point1, point2):
        self.tur.goto(point1.get_x(), point1.get_y())
        self.tur.pd()
        self.tur.goto(point2.get_x(), point2.get_y())
        self.tur.setpos(point2.get_x(), point2.get_y())

    def get_point(self):
        return self.point1, self.point2

    def __str__(self):
        return "(%s,%s)" % (self.point1, self.point2)

    def joins(self, line2):
        line2Pts = line2.get_point()
        self.tur.pu()
        self.tur.goto(self.point2.get_x(), self.point2.get_y())
        self.tur.pd()
        self.tur.goto(line2Pts[0].get_x(), line2Pts[0].get_y())


def start():
    tur = turtle.Turtle()
    PointLst = []
    LineLst = []
    for i in range(2):
        n = int(input("Input number of points for line " f"{i+1}"" : "))
        for i in range(n):
            # Randomize and set X and Y into class
            x_coor = random.randint(-500, 500)
            y_coor = random.randint(-500, 500)
            PointLst.append(Point(x_coor, y_coor))
            tur.pu()
            tur.goto(x_coor, y_coor)
            tur.dot()
            tur.write("   P : " f"{i+1}")
        LineLst.append(PointLst)
        PointLst = []
    for x in range(len(LineLst)):
        for i in range(len(LineLst[x])):
            try:
                draw_line = Line(LineLst[x][i], LineLst[x][i+1], tur)
                draw_line.draw(LineLst[x][i], LineLst[x][i+1])
                tur.pu()
            except:
                continue
    line1 = Line(LineLst[0][0], LineLst[0][-1], tur)
    line2 = Line(LineLst[1][0], LineLst[1][-1], tur)
    line1.joins(line2)


screen = turtle.Screen()
scn_length = 1000
scn_width = 1000
turtle.screensize(scn_length, scn_width)

start()
