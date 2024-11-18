from turtle import Screen
import time
from snake import Snake
from LISTA import Food,Scoreboard
import pygame
pygame.init()

def kasino():
    pygame.mixer.music.load('kasino.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

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
        kasino()
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Wall Collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.endgame()

    #Tail Collision
    for segments in snake.all_snakes:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.endgame()


screen.exitonclick()
