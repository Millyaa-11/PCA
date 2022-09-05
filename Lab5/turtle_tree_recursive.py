import turtle
screen = turtle.Screen()
turtles = 5
scn_length = 500
scn_width = 500
turtle.screensize(scn_length, scn_width)


def tree(dis):
    turtle.speed(10)
    if dis < 20:
        return
    else:
        turtle.fd(dis)
        turtle.lt(35)
    # the distance changes the shape and the number of branches
    # the turtle turns by the amount of distance, until distance is less than 20
        tree(3 * dis / 4)
    # after return, it runs line 20
        turtle.rt(70)
    # the distance from the last calculation of the previous function
        tree(3 * dis / 4)
    # run if distance from func 2 is less than 20
        turtle.lt(35)
        turtle.backward(dis)
    # return to func 1, return to the previous dis value
    # end function if all values are less than 20


tree(85)
while True:
    turtle.fd(0)
