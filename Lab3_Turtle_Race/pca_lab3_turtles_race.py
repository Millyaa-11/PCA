import turtle
import random

screen = turtle.Screen()
turtles = 5
scn_length = 500
scn_width = 500
turtle.screensize(scn_length, scn_width)


class TURTLES:
    def __init__(self, colour, pos, speed, energy, dist, tur_type):  # declare class variables
        self.colour = colour
        self.pos = pos
        self.speed = speed
        self.energy = energy
        self.dist = dist
        self.tur = turtle.Turtle()
        self.tur.penup()
        self.tur.shape("turtle")
        self.tur.color(colour)
        self.tur.setpos(pos)
        self.tur_type = tur_type
    
    def normal(self):  # normal turtle movement func
        self.tur.setheading(0)
        self.tur.pendown()
        self.tur.forward(self.dist)
        self.tur.penup()
        turtle.update()

    def random_tur(self, rounds):  # random turtle movement func
        self.tur.pendown()
        directions = random.randint(-180, 180)
        n = random.randint(0, 1)
        if self.energy > 0:  # energy settings
            if n == 1:  # randomize turning left or right
                for i in range(rounds):
                    self.tur.rt(directions)
                    self.tur.forward(self.dist)
                    directions += 0.5
                    self.energy -= 1
                    print(self.energy)

            elif n == 0:
                for i in range(rounds):
                    self.tur.lt(directions)
                    self.tur.forward(15)
                    directions += 0.5
                    self.energy -= 1
                    print(self.energy)
        elif self.energy <= 0:  # if energy = 0 forward = 0
            self.tur.fd(0)
        turtle.update()
        turtle.penup()


def start():
    # set turtle to the middle of the screen and hide
    turtle.hideturtle()
    turtle.pu()
    turtle.color("black")
    turtle.setpos(300, -450)
    turtle.setheading(90)
    turtle.pd()
    turtle.fd(845)

    t_list = []
    type_list = []

    turtle.hideturtle()
    colours = ["blue", "red", "green", "pink", "yellow"]
    pos_y = []
    tur_col_list = []
    # set the turtle to positions and set the characteristics
    for i in range(turtles):
        tur_type = int(input("1 : Normal Turtle\n2 : FPO Turtle \n3 : Drunk Turtle \n"))
        start_pos_y = -350 + i * 170
        pos_y.append(start_pos_y)
        # append the characteristic of each turtles
        t_list.append(TURTLES(colours[i], (-300, start_pos_y), 500, random.randint(15, 40), random.randint(15, 100), tur_type))
        # create colour list to declare the winner
        tur_col_list.append(colours[i])
        # store the turtle type input into list
        type_list.append(tur_type)
        t_list[i].tur.hideturtle()
        t_list[i].tur.showturtle()

    run = True
    while run:
        # run through the number of turtle that was inputted
        for i in range(len(t_list)):
            try:
                # if the turtle run pass the finish line then print winner
                if t_list[i].tur.pos() >= (300, -450):
                    print(tur_col_list[i], " turtle is the winner!!")
                    run = False
                    exit(1)
                # if the turtle goes off the screen put it back to position
                elif t_list[i].tur.pos() <= (-450, -450) or t_list[i].tur.pos() >= (450, 450):
                    t_list[i].tur.pu()
                    t_list[i].tur.setpos(-300, pos_y[i])
                    t_list[i].tur.pd()
                # if the type list[i] input is 1 then run the turtle characteristic list [1]
                elif type_list[i] == 1:
                    t_list[i].normal()
                elif type_list[i] == 2:
                    t_list[i].random_tur(1)
                elif type_list[i] == 3:
                    t_list[i].random_tur(5)
            except ValueError:
                print("Invalid Input for turtle type selection")


start()
screen.exitonclick()
