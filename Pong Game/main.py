from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game ⚽")
screen.setup(height=600, width=800)
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
player_1 = 0
player_2 = 0

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # wall bouncing
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(l_paddle) < 70 and ball.xcor() < -320) or (ball.distance(r_paddle) < 70 and ball.xcor() > 320):
        ball.collide()

    # Score board
    if ball.xcor() > 400:
        ball.reset_position()
        score_board.l_point()
        score_board.update_score()

    if ball.xcor() < -400:
        ball.reset_position()
        score_board.r_point()
        score_board.update_score()






screen.exitonclick()
