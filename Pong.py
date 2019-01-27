import turtle
import os

window = turtle.Screen()
window.title("Pong by BadassSalad")
window.bgcolor("black")
window.setup(width= 1000, height= 620)
window.tracer(0)

for i in range(0, 10):
    middle = turtle.Turtle()
    middle.speed(0)
    middle.shape("square")
    middle.color("grey")
    middle.shapesize(stretch_wid= 2, stretch_len=0.5)
    middle.penup()
    middle.goto(0, 260 - 100*i)

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid= 5, stretch_len=1)
paddleA.penup()
paddleA.goto(-450, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid= 5, stretch_len=1)
paddleB.penup()
paddleB.goto(450, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 5
ball.dy = 5

#Moving the Paddles
def paddleAup():
    y = int(paddleA.ycor())
    y += 30
    paddleA.sety(y)

def paddleAdown():
    y = int(paddleA.ycor())
    y -= 30
    paddleA.sety(y)

def paddleBup():
    y = int(paddleB.ycor())
    y += 30
    paddleB.sety(y)

def paddleBdown():
    y = int(paddleB.ycor())
    y -= 30
    paddleB.sety(y)

window.listen()
window.onkeypress(paddleAup, "a")
window.onkeypress(paddleAdown, "z")

window.onkeypress(paddleBup, "Up")
window.onkeypress(paddleBdown, "Down")

#Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 180)
pen.write("0     0", align="center", font=("OCR A Std", 100, "normal"))

scoreA = 0
scoreB = 0



while True:
    window.update()

    #ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1
        os.system("afplay pong.mp3&")
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1
        os.system("afplay pong.mp3&")

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        os.system("afplay oof.mp3&")
        pen.clear()
        pen.write("{}     {}".format(scoreA,scoreB), align="center", font=("OCR A Std", 100, "normal"))
    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        os.system("afplay oof.mp3&")
        pen.clear()
        pen.write("{}     {}".format(scoreA,scoreB), align="center", font=("OCR A Std", 100, "normal"))

    #Collision
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() >paddleB.ycor() - 50):
        ball.setx(440)
        ball.dx *= -1
        os.system("afplay pong.mp3&")
    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() >paddleA.ycor() - 50):
        ball.setx(-440)
        ball.dx *= -1
        os.system("afplay pong.mp3&")
    if paddleA.ycor() > 250:
        paddleA.sety(250)
    if paddleA.ycor() < -250:
        paddleA.sety(-250)

    if paddleB.ycor() > 250:
        paddleB.sety(250)
    if paddleB.ycor() < -250:
        paddleB.sety(-250)
