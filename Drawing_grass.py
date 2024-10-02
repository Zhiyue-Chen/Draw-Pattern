from turtle import *

def grass():
    speed(3)
    color("green")
    pensize(2)
    for i in range(10):  # draw 10 grasses
        penup()
        goto(-100 + i * 20, -150)  # set the position of each grass
        pendown()
        seth(90)  
        fd(30)  # height of grass
        right(45)
        fd(20)
        penup()
        goto(-100 + i * 20, -150)  # go back to the bottom of grass
        pendown()
        seth(90)  # print upward
        fd(30)
        left(45)
        fd(20)


    pensize(3)
    for j in range(10):  # draw 10 grasses
        color("red")
        penup()
        goto(-100 + j * 20, -150)  # set the position of each grass
        seth(90) 
        fd(30)  # height of grass
        right(30) 
        fd(20)
        pendown()
        dot(8)

        color("yellow")
        penup()
        goto(-100 + j * 20, -150)  # go back to the bottom of grass
        seth(90)  # print upward
        fd(30)
        left(30)
        fd(10)
        pendown()
        dot(8)

    hideturtle()

    done()

# test
grass()