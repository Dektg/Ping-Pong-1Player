import turtle#
from random import choice, randint#

#score = 0

window = turtle.Screen()#
window.title("2d Ping-Pong")#
# Размеры окна на весь монитор#
window.setup(width=1.0, height=1.0)#
# Задний фон#
window.bgcolor("black")#
window.tracer(2)

# Отрисовка поля
border_rectangle = turtle.Turtle()#
border_rectangle.color("white")#
border_rectangle.speed(5)#
# Спрятал отрисовку курсора#
border_rectangle.hideturtle()#
border_rectangle.up()#
border_rectangle.goto(-500, 300)#
border_rectangle.down()#
border_rectangle.begin_fill()#
border_rectangle.goto(500, 300)#
border_rectangle.goto(500, -300)#
border_rectangle.goto(-500, -300)#
border_rectangle.goto(-500, 300)#
border_rectangle.end_fill()#

#FONT = ("Arial", 44)
#score = 0
#s1 = turtle.Turtle(visible=False)
#s1.color('white')
#s1.penup()
#s1.setposition(-200, 300)
#s1.write(score, font=FONT)

rocket = turtle.Turtle()#
rocket.color("black")#
rocket.shape("square")#
rocket.shapesize(stretch_len=5, stretch_wid=1)#
# Не оставляет следов#
rocket.penup()#
rocket.goto(0, -250)#

space_rocket = 80#


def move_Right():#
    x = rocket.xcor() + space_rocket
    if x > 490:
        x = 490
    rocket.setx(x)


def move_Left():
    x = rocket.xcor() - space_rocket
    if x < -490:
        x = -490
    rocket.setx(x)


ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.dx = 5
ball.dy = 5
ball.penup()

window.listen()
window.onkeypress(move_Right, "d")
window.onkeypress(move_Left, "a")

while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.goto(0, 0)

    if ball.xcor() >= 490:
        ball.dx = -ball.dx

    if ball.xcor() <= -490:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket.ycor() - 5 and ball.ycor() <= rocket.ycor() + 5 \
            and ball.xcor() >= rocket.xcor() - 50 and ball.xcor() <= rocket.xcor() + 50:
        ball.dy = -ball.dy

window.mainloop()
