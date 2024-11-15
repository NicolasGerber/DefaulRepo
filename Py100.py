import turtle
import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet","Which color will win the race?  Enter a color: ")
colors = ["red","blue","yellow","purple","green","orange"]
y_positions = [-100,-50,0,50,100,150]
all_turtles = []

for i in range(0,6):
    tuga = t.Turtle(shape="turtle")
    tuga.color(colors[i])
    tuga.penup()
    tuga.speed(2)
    tuga.goto(x=-230,y=y_positions[i])
    all_turtles.append(tuga)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"YOU WON!!! The winner is the {winning_color} turtle")
            else:
                print(f"YOU LOSE!!! The winner is the {winning_color} turtle")
        walk =  random.randint(0, 10)
        turtle.forward(walk)
screen.exitonclick()


