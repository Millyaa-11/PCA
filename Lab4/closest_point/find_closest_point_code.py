import random
import matplotlib.pyplot as plt
import timeit
import keyboard

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

    def distance(self):
        totalDiff = []
        for i in range(len(PointLst)):
            # original X and Y minus by the new coordinate X and Y
            totalDiff.append((abs(0 - lstX[i])) + (abs(0 - lstY[i])))
        return totalDiff

    def findClosest(self, totalDiff, lstX, lstY):
        closest = 1000
        closestX = 0
        closestY = 0
        # Find the closest coordinate by setting the least difference as closest and updating it everytime
        # Set the closest X and Y coordinate into the closest X-Y variables
        for i in range(len(totalDiff)):
            if totalDiff[i] < closest:
                closestX = lstX[i]
                closestY = lstY[i]
                closest = totalDiff[i]
            else:
                continue
        return closestX, closestY


PointLst = []
lstX = []
lstY = []
p = []
storeRun_distance = []
storeRun_closest = []


def start():
    n = int(input("Input number of points : "))
    nArray = []
    ClosestCoor = []
    try:
        if n > 1 and n <= 100000:
            for i in range(n):
                # Randomize and set X and Y into class
                lstX.append(random.randint(-1000, 1000))
                lstY.append(random.randint(-1000, 1000))
                PointLst.append(Point(lstX[i], lstY[i]))
                # Plot the coordinates of all points
                plt.scatter(lstX, lstY, label="stars", color="black")
                # Run function find distance with each point
                start = timeit.default_timer()
                totalDiff = PointLst[i].distance()
                # Run function find closest with each point
                ClosestCoor = PointLst[i].findClosest(totalDiff, lstX, lstY)
                end = timeit.default_timer()
                storeRun_closest.append(abs(start - end))
                nArray.append(i)
            # Plot Coordinate of the closest point
            print("The time used to find all of the closest point is ", sum(storeRun_closest))
            plt.scatter(ClosestCoor[0], ClosestCoor[1], color="red")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.grid()
            plt.show()
    except ValueError:
        print("Invalid! Please enter a number")
    return nArray, storeRun_closest


def runtime_closest(nArray):
    plt.plot(nArray, storeRun_closest)
    plt.xlabel("Run time")
    plt.ylabel("n")
    plt.grid()
    plt.show()


runtime_closest(start()[0])
