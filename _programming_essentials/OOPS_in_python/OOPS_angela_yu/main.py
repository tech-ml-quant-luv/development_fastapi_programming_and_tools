# import turtle
from turtle import Turtle, Screen

timmy = Turtle()
print(Turtle)
print(timmy)
timmy.shape("turtle")


count = 0
steps = 30
for i in range(20):
    timmy.color("Red")
    timmy.forward(steps+count)
    timmy.color("Black")
    timmy.left(90)
    timmy.forward(steps+count)
    timmy.color("Blue")
    timmy.left(90)
    timmy.forward(steps)
    timmy.color("Green")
    # if count%5==0:
    #     timmy.right(90)
    if count % 50 == 0:
        timmy.right(90)

    count+=10

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
print("Exit")