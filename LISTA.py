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
        self.hideturtle()
        self.score =0
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}",False,ALIGNMENT,FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}",False,ALIGNMENT,FONT)

    def endgame(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!! \nFINAL SCORE:{self.score}", False, ALIGNMENT, FONT)