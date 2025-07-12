import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win this race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue"]
all_turtles = []
turtle_y_coordinate = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-210, y=turtle_y_coordinate)
    all_turtles.append(new_turtle)
    turtle_y_coordinate += 40



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You won! The {winning_color} turtle won.")
            else:
                print(f"You lost. The actual winner was the {winning_color} turtle.")



screen.exitonclick()