from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import pygame
pygame.init()


POS1=350,0
POS2=-350,0


screen= Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle(POS1)
l_paddle = Paddle(POS2)

screen.listen()

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 282 or ball.ycor() < -282:
        ball.bounce()
        pygame.mixer.Sound.play(pygame.mixer.Sound('pong.mp3'))
    if ball.distance(r_paddle) < 45 and ball.xcor() > 330:
        ball.defend()
        pygame.mixer.Sound.play(pygame.mixer.Sound('pong.mp3'))
    if ball.distance(l_paddle) < 45 and ball.xcor() > -330:
        ball.defend()
        pygame.mixer.Sound.play(pygame.mixer.Sound('pong.mp3'))

    if ball.xcor() > 420:
        scoreboard.score_l()
        time.sleep(ball.move_speed)
        ball.reset()

    if ball.xcor() < -420:
        scoreboard.score_r()
        time.sleep(0.8)
        ball.reset()
screen.mainloop()