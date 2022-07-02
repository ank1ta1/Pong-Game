from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
r_player = Scoreboard(100)
l_player = Scoreboard(-100)
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)

screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect a miss
    elif ball.xcor() > 400:
        l_player.increase_score()
        l_player.update_scoreboard()
        ball.restart("left")

    elif ball.xcor() < -400:
        r_player.increase_score()
        r_player.update_scoreboard()
        ball.restart("right")


screen.exitonclick()