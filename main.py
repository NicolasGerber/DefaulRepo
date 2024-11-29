from turtle import Turtle, Screen
import pandas as pd
from map_text import Texto
import time

data = pd.read_csv("points.csv", index_col=False)
points = data.to_dict("list")
points["state"] = [state.strip().title() for state in points["state"]]

text = Texto()
turtle = Turtle()
screen = Screen()
time_text = Turtle()

screen.setup(947, 980)
screen.title("South America Countries and Brazil States Game")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

start = time.time()
time_limit = 125
i = 0
game_is_on = True
guessed_answers = []


def update_time():
    elapsed_time = int(time.time() - start)
    remaining_time = time_limit - elapsed_time


    time_text.clear()
    time_text.penup()
    time_text.hideturtle()
    time_text.goto(220, 417)
    time_text.write(f"Time: {remaining_time}", font=("Courier", 30, "normal"))

    if remaining_time > 0:
        screen.ontimer(update_time, 1000)
    else:
        game_over()

def game_over():
    global game_is_on
    game_is_on = False
    text.clear()
    text.penup()
    text.hideturtle()
    text.goto(0, 0)
    text.write("TIME'S UP! Game Over!", align="center", font=("times new roman", 30, "normal"))



screen.textinput("ARE YOU READY!","Press OK to start")
screen.ontimer(update_time, 1000)

while game_is_on:
    answer = screen.textinput(f"{i}/38 Correct", "Guess a State or a Country").title().strip()

    if not answer or answer in guessed_answers:
        pass

    if answer in points["state"]:
        index = points["state"].index(answer)
        x = points["x"][index]
        y = points["y"][index]
        name = points["state"][index]
        text.create(name, x, y)
        guessed_answers.append(answer)
        i += 1

    if i == 38:
        text.clear()
        text.penup()
        text.goto(0, 50)
        text.write("YOU WON!", align="center", font=("times new roman", 30, "normal"))
        text.hideturtle()


screen.mainloop()
