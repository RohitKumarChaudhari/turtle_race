import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)
my_screen.bgcolor("coral")

y_cordinate = [-120, 120, 80, -80, 40, -40, 0]
y_cordinate_line = [-142, -102, -62, -22, 22, 62, 102, 142]
color = ["violet", "indigo", "blue", "green", "orange", "red", "yellow"]
all_turtle = []

tim = Turtle()  # A turtle for line making
tim.speed("fastest")
tim.color("white")
tim.pensize(4)
is_race_on = False

user_guess = my_screen.textinput(prompt="Which turtle will win the race! Choose the color", title="Guess the winner")

for line_index in range(0, 8):  # for making the line on the track
    tim.penup()
    tim.goto(x=-260, y=y_cordinate_line[line_index])
    tim.pendown()
    tim.setheading(0)
    tim.fd(600)

if user_guess:
    is_race_on = True

for turtle_index in range(0, 7):  # for making the turtle and sending him to the starting position
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cordinate[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtle.append(new_turtle)

while is_race_on:  # for starting the race

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_guess == turtle:
                print(f"You've win the race! The winner is  {turtle.pencolor()} color turtle")
            else:
                print(f"You've lost the race! The winner is  {turtle.pencolor()} color turtle")

        walk_distance = random.randint(0, 10)
        turtle.fd(walk_distance)

my_screen.exitonclick()
