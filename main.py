from turtle import Screen
import time
from snake import Snake
from scoreboard  import Food,Scoreboard
import pygame
pygame.init()


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()



    #Food Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Wall Collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.endgame()
        time.sleep(1)
        snake.reset_position()

    #Tail Collision
    for segments in snake.all_snakes:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            scoreboard.endgame()
            time.sleep(1)
            snake.reset_position()


screen.exitonclick()