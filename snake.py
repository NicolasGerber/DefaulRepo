from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self,position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        new_snake.speed(5)
        self.all_snakes.append(new_snake)


    def extend(self):
        self.add_snake(self.all_snakes[-1].position( ))

    def reset_position(self):
        for seg in self.all_snakes:
            seg.goto(1000,1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]


    def move(self):
        for snake_num in range(len(self.all_snakes)-1,0,-1):
            new_x = self.all_snakes[snake_num - 1].xcor()
            new_y = self.all_snakes[snake_num - 1].ycor()
            self.all_snakes[snake_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)