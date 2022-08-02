import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(232, 153, 79), (246, 206, 76), (94, 171, 209), (26, 110, 156), (219, 245, 235), (215, 75, 108),
              (160, 56, 93), (104, 197, 161), (194, 228, 241), (232, 76, 52), (248, 223, 234), (12, 139, 103),
              (182, 169, 28), (195, 52, 37), (213, 127, 152), (40, 53, 114), (129, 223, 201), (246, 155, 176),
              (109, 38, 70), (7, 97, 71), (130, 218, 233), (245, 164, 151), (43, 162, 192), (45, 172, 134),
              (24, 47, 92), (111, 113, 171), (71, 34, 64), (8, 70, 51), (161, 32, 23)]
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.up()
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

