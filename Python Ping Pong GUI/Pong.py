    # Simple pong game by Salman
    # Part 1 : getting started and setting up the gui of the game


import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Salman")
wn.setup(width=800, height=600)
wn.bgcolor("Black")
wn.tracer()
    # Score
left_score = 0
right_score = 0

    # Left Paddle

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color("purple")
left_paddle.penup()
left_paddle.goto(-375,0)

    # Right Paddle

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color("purple")
right_paddle.penup()
right_paddle.goto(370,0)


    # Ball

ball = turtle.Turtle()
ball.speed(5)
ball.shape("circle")
#ball.shapesize(stretch_len=2, stretch_wid=2).
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=5
ball.dy=5

    # Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Player A : 0     Player B : 0", align= "center", font = ("Courier", 24, "normal"))


    #Functions

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


    # Keyboard  input Setup

wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")

wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")

    # Main Loop

while True:
    # Window visual
    wn.update()

    # Ball movement

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1


    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1


    if ball.xcor() >  380:
        ball.goto(0 , 0)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        left_score += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        right_score += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    # Ball Paddle Collision

    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -355 and ball.xcor() > -365) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)