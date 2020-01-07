import turtle
from random import choice, randint

score_a = 0
score_b = 0
window = turtle.Screen()
window.title("2d Ping-Pong")
# Размеры окна на весь монитор
window.setup(width=1.0, height=1.0)
# Задний фон
window.bgcolor("black")
window.tracer(2)

# Отрисовка поля
border_rectangle = turtle.Turtle()
border_rectangle.color("white")
border_rectangle.speed(5)
# Спрятал отрисовку курсора
border_rectangle.hideturtle()
border_rectangle.up()
border_rectangle.goto(-500, 300)
border_rectangle.down()
border_rectangle.begin_fill()
border_rectangle.goto(500, 300)
border_rectangle.goto(500, -300)
border_rectangle.goto(-500, -300)
border_rectangle.goto(-500, 300)
border_rectangle.end_fill()

border_rectangle.goto(0, 300)
border_rectangle.color("black")
# Повернуться вниз
border_rectangle.setheading(270)

# Цикл для пунктира
for i in range(0, 25, 1):
    if i % 2 == 0:
        border_rectangle.forward(24)
    else:
        border_rectangle.up()
        border_rectangle.forward(24)
        border_rectangle.down()

FONT = ("Arial", 44)
score_a = 0
s1 = turtle.Turtle(visible=False)
s1.color('white')
s1.penup()
s1.setposition(-200, 300)
s1.write(score_a, font=FONT)

score_b = 0
s2 = turtle.Turtle(visible=False)
s2.color('white')
s2.penup()
s2.setposition(200, 300)
s2.write(score_a, font=FONT)

rocket_a = turtle.Turtle()
rocket_a.color("black")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
# Не оставляет следов
rocket_a.penup()
rocket_a.goto(-450, 0)

rocket_b = turtle.Turtle()
rocket_b.color("black")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
# Не оставляет следов
rocket_b.penup()
rocket_b.goto(450, 0)
space_rocket = 80

def move_up():
    y = rocket_a.ycor() + space_rocket
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down():
    y = rocket_a.ycor() - space_rocket
    if y < -250:
        y = -250
    rocket_a.sety(y)


def move_up_b():
    y = rocket_b.ycor() + space_rocket
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - space_rocket
    if y < -250:
        y = -250
    rocket_b.sety(y)


ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.dx = 5
ball.dy = 5
ball.penup()

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")

while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        score_b += 1
        s2.clear()
        s2.write(score_b, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-5, 5])
        ball.dy = choice([-5, 5])

    if ball.xcor() <= -490:
        score_a += 1
        s1.clear()
        s1.write(score_a , font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-5, 5])
        ball.dy = choice([-5, 5])

    if ball.ycor() >= rocket_b.ycor() - 50 and ball.ycor() <= rocket_b.ycor() + 50 \
            and ball.xcor() >= rocket_b.xcor() - 5 and ball.xcor() <= rocket_b.xcor() + 5:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket_a.ycor() - 50 and ball.ycor() <= rocket_a.ycor() + 50 \
            and ball.xcor() >= rocket_a.xcor() - 5 and ball.xcor() <= rocket_a.xcor() + 5:
        ball.dx = -ball.dx

window.mainloop()
