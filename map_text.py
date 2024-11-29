from turtle import Turtle

class Texto(Turtle):
    def __init__(self):
        super().__init__()

    def create(self,name,x,y):
        new_texto = Turtle()
        new_texto.hideturtle()
        new_texto.penup()
        new_texto.goto(x, y)
        new_texto.write(f"{name}",align="center",font=("times new roman",10,"normal"))
