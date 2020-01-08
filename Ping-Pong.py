import turtle
from random import choice, randint


# ИНИЦИАЛИЗАЦИЯ
score = 0

rand_x = randint(-150, 150)
rand_y = randint(0, 150)

ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.goto(rand_x, rand_y)

ball.dx = 5
ball.dy = 5

space_rocket = 80

window = turtle.Screen()
window.title("2d Ping-Pong")
window.setup(width=1.0, height=1.0) # Размеры окна на весь монитор
window.bgcolor("black") # Задний фон
window.tracer(2)

# ПОЛЕ
border_rectangle = turtle.Turtle()
border_rectangle.color("white")
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


# СЧЁТ
FONT = ("Arial", 44)
s1 = turtle.Turtle(visible=False)
s1.color('white')
s1.penup()
s1.setposition(0, 300)
s1.write(score, font=FONT)


# РАКЕТКА
rocket = turtle.Turtle()
rocket.color("black")
rocket.shape("square")
rocket.shapesize(stretch_len=5, stretch_wid=1)
    # Не оставляет следов
rocket.penup()
rocket.goto(0, -250)

# УПРАВЛЕНИЕ РАКЕТКИ
def move_Right():
    x = rocket.xcor() + space_rocket
    if x > 450:
        x = 450
    rocket.setx(x)


def move_Left():
    x = rocket.xcor() - space_rocket
    if x < -450:
        x = -450
    rocket.setx(x)


window.listen()
window.onkeypress(move_Right, "d")
window.onkeypress(move_Left, "a")
window.onkeypress(move_Right, "Right")
window.onkeypress(move_Left, "Left")


#ПРЕПЯТСТВИЯ
let = turtle.Turtle()
let.shape("square")
let.color("green")
let.shapesize(stretch_len=10, stretch_wid=2)
let.up()
let.goto(0, 278)

a = 0
# ШАРИК И СТЕНЫ
while True:
    a+=1
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        score -= 1
        s1.clear()
        s1.write(score, font=FONT)
        ball.goto(rand_x, rand_y)
        ball.dx = choice([-4,-3, 3, 4,])
        ball.dy = randint(-10, -5)

    if ball.xcor() >= 490:
        ball.dx = -ball.dx

    if ball.xcor() <= -490:
        ball.dx = -ball.dx

# ШАРИК И РАКЕТКА
    if ball.ycor() >= rocket.ycor() - 10 and ball.ycor() <= rocket.ycor() + 10 \
            and ball.xcor() >= rocket.xcor() - 50 and ball.xcor() <= rocket.xcor() + 50:
        ball.dy = -ball.dy
    print(a,let.color(), sep=":")


# ШАРИК И КРАСТНОЕ И ЗЕЛЁНОЕ ПРИПЯДСТВИЕ
    if ball.ycor() >= let.ycor() - 20 and ball.ycor() <= let.ycor() + 20 \
            and ball.xcor() >= let.xcor() - 110 and ball.xcor() <= let.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let.color() == ('red', 'red'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let.color('red')


window.mainloop()