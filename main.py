from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')

# for number in range(50):
#     if number % 2 == 0:
#         timmy.pendown()
#         timmy.forward(10)
#     else:
#         timmy.penup()
#         timmy.forward(10)

# timmy.forward(100)
# timmy.right(90)

import random


def timmy_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)


# def draw_timmy(angle):
#
#     for number in range(angle):
#         timmy.forward(50)
#         timmy.right(360 / angle)
#         timmy_color()
#
#
# for number in range(3, 11):
#     draw_timmy(number)
# timmy.pensize(15)
# for number in range(200):

    # timmy.right(random.randint(0, 360))
    # timmy.left(random.randint(0, 360))
    # timmy_color()
    # sol = random.randint(1, 5)
    # if sol == 1:
    #     timmy.forward(50)
    # elif sol == 2:
    #     timmy.backward(50)
    # elif sol == 3:
    #     timmy.right(50)
    # else:
    #     timmy.left(50)
for number in range(200):
    timmy.circle(50)
    timmy_color()
    timmy.right(10)

screen = Screen()
screen.exitonclick()