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


class Line:
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

    def joins(self, line2, line1):
        line1pts = line1.get_point()
        line2pts = line2.get_point()
        self.tur.pu()
        self.tur.goto(line1pts[-1].get_x(), line1pts[-1].get_y())
        self.tur.pd()
        self.tur.goto(line2pts[0].get_x(), line2pts[0].get_y())
        list(line1pts).append(line2pts)
        line2pts = ()

    def joins_extend(self, line2, line1):
        line1pts = line1.get_point()
        line2pts = line2.get_point()
        self.tur.pu()
        self.tur.goto(line1pts[-1].get_x(), line1pts[-1].get_y())
        self.tur.pd()
        self.tur.goto(line2pts[0].get_x(), line2pts[0].get_y())
        list(line1pts).extend(line2pts)
        line2pts = ()

    def zigzag1(self, LineLst):
        line1pts = []
        line2pts = []
        line3 = []
        self.tur.pu()
        for i in range(len(LineLst[0])):
            try:
                line1pts.append(LineLst[0][i])
            except IndexError:
                continue
        for i in range(len(LineLst[1])):
            try:
                line2pts.append(LineLst[1][i])
            except IndexError:
                continue
        line1pts.extend(line2pts)
        random.shuffle(line1pts)
        for i in range(len(line1pts)):
            try:
                line3.append(line1pts[i])
                draw_line = Line(line1pts[i], line1pts[i + 1], self.tur)
                draw_line.draw(line1pts[i], line1pts[i + 1])
                line1pts[i] = "k"
            except IndexError or ValueError:
                continue


class LineTester:
    def __init__(self):
        self.tur = turtle.Turtle()

    def testJoin(self):
        PointLst = []
        LineLst = []
        for i in range(2):
            n = int(input("Input number of points for line " f"{i + 1}"" : "))
            for x in range(n):
                # Randomize and set X and Y into class
                x_coor = random.randint(-500, 500)
                y_coor = random.randint(-500, 500)
                PointLst.append(Point(x_coor, y_coor))
                self.tur.pu()
                self.tur.goto(x_coor, y_coor)
                self.tur.dot()
                self.tur.write("   P : " f"{x + 1}")
            LineLst.append(PointLst)
            PointLst = []
        for x in range(len(LineLst)):
            for i in range(len(LineLst[x])):
                try:
                    draw_line = Line(LineLst[x][i], LineLst[x][i + 1], self.tur)
                    draw_line.draw(LineLst[x][i], LineLst[x][i + 1])
                    self.tur.pu()
                except IndexError:
                    continue
        line1 = Line(LineLst[0][0], LineLst[0][-1], self.tur)
        line2 = Line(LineLst[1][0], LineLst[1][-1], self.tur)
        line1.joins(line2, line1)

    def testZigzag(self):
        PointLst = []
        LineLst = []
        for i in range(2):
            n = int(input("Input number of points for line " f"{i + 1}"" : "))
            for x in range(n):
                # Randomize and set X and Y into class
                x_coor = random.randint(-500, 500)
                y_coor = random.randint(-500, 500)
                PointLst.append(Point(x_coor, y_coor))
                self.tur.pu()
                self.tur.goto(x_coor, y_coor)
                self.tur.dot()
                self.tur.write("   P : " f"{x + 1}")
            LineLst.append(PointLst)
            PointLst = []

        line1 = Line(LineLst[0][0], LineLst[0][-1], self.tur)
        line2 = Line(LineLst[1][0], LineLst[1][-1], self.tur)
        line1.zigzag1(LineLst)


def start():
    screen = turtle.Screen()
    scn_length = 1000
    scn_width = 1000
    turtle.screensize(scn_length, scn_width)
    test = LineTester()
    test.testZigzag()


start()
