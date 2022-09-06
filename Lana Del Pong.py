#Pong
#Cat Schnelle

import turtle


wn = turtle.Screen()
wn.title("Lana Del Pong")
wn.bgcolor("black")
wn.bgpic("ldr.png")
wn.setup(width=800, height=600)
wn.tracer(0)

#score keep
score_1 = 0
score_2 = 0

# paddle left
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350,0)
# paddle right
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1
#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  Player 2: 0", align ="center", font=("courier", 15, "normal"))

# move left paddle up
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

# move left paddle down
def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

# move right paddle up
def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

# move right paddle down
def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

#key bindings
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "i")
wn.onkeypress(paddle_r_down, "k")


#main loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    # bottom border
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    
    #right border recenter ball
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align ="center", font=("courier", 15, "normal"))

    #left border recenter ball
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align ="center", font=("courier", 15, "normal"))

    # paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() +50 and ball.ycor() > paddle_r.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() +50 and ball.ycor() > paddle_l.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1    