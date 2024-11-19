from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("white")
        self.x_move = 17
        self.y_move = 17
        self.move_speed = 0.2


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def defend(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.defend()