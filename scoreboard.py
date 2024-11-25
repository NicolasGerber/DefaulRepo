from turtle import Turtle
import random
#CONSTANTES
ALIGNMENT="center"
FONT=("times new roman",15,"normal")
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("highscores.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.score =0
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score} High Score: {self.highscore}",False,ALIGNMENT,FONT)



    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score} High Score: {self.highscore}",False,ALIGNMENT,FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score:{self.score} High Score: {self.highscore}",False,ALIGNMENT,FONT)


    def endgame(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscores.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
