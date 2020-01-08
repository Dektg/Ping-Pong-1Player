import turtle
from random import choice, randint


# ИНИЦИАЛИЗАЦИЯ
score = 0

rand_x = randint(-150, 150)
rand_y = randint(-150, 150)

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
let_orange = turtle.Turtle()
let_orange.shape("square")
let_orange.color("orange")
let_orange.shapesize(stretch_len=10, stretch_wid=2)
let_orange.up()
let_orange.goto(0, 278)

let_Yellow = turtle.Turtle()
let_Yellow.shape("square")
let_Yellow.color("Yellow")
let_Yellow.shapesize(stretch_len=10, stretch_wid=2)
let_Yellow.up()
let_Yellow.goto(210, 278)

let_cyan = turtle.Turtle()
let_cyan.shape("square")
let_cyan.color("Cyan")
let_cyan.shapesize(stretch_len=10, stretch_wid=2)
let_cyan.up()
let_cyan.goto(0, 228)

let_red = turtle.Turtle()
let_red.shape("square")
let_red.color("Orange Red")
let_red.shapesize(stretch_len=10, stretch_wid=2)
let_red.up()
let_red.goto(-210, 278)

let_Green = turtle.Turtle()
let_Green.shape("square")
let_Green.color("Lime Green")
let_Green.shapesize(stretch_len=10, stretch_wid=2)
let_Green.up()
let_Green.goto(-210, 228)

let_Blue = turtle.Turtle()
let_Blue.shape("square")
let_Blue.color("Medium Blue")
let_Blue.shapesize(stretch_len=10, stretch_wid=2)
let_Blue.up()
let_Blue.goto(210, 228)


let_Violet = turtle.Turtle()
let_Violet.shape("square")
let_Violet.color("Dark Violet")
let_Violet.shapesize(stretch_len=10, stretch_wid=2)
let_Violet.up()
let_Violet.goto(0, 178)

# ШАРИК И СТЕНЫ
while True:
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


# ШАРИК И КРАСТНОЕ И ЗЕЛЁНОЕ ПРИПЯДСТВИЕ
    if ball.ycor() >= let_orange.ycor() - 20 and ball.ycor() <= let_orange.ycor() + 20 \
            and ball.xcor() >= let_orange.xcor() - 110 and ball.xcor() <= let_orange.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let_orange.color() == ('Dim Gray', 'Dim Gray'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let_orange.color('Dim Gray')



    if ball.ycor() >= let_Yellow.ycor() - 20 and ball.ycor() <= let_Yellow.ycor() + 20 \
            and ball.xcor() >= let_Yellow.xcor() - 110 and ball.xcor() <= let_Yellow.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let_Yellow.color() == ('Dim Gray', 'Dim Gray'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let_Yellow.color('Dim Gray')



    if ball.ycor() >= let_cyan.ycor() - 20 and ball.ycor() <= let_cyan.ycor() + 20 \
            and ball.xcor() >= let_Yellow.xcor() - 110 and ball.xcor() <= let_cyan.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let_cyan.color() == ('Dim Gray', 'Dim Gray'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let_cyan.color('Dim Gray')



    if ball.ycor() >= let_red.ycor() - 20 and ball.ycor() <= let_red.ycor() + 20 \
            and ball.xcor() >= let_red.xcor() - 110 and ball.xcor() <= let_red.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let_red.color() == ('Dim Gray', 'Dim Gray'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let_red.color('Dim Gray')


    if ball.ycor() >= let_Green.ycor() - 20 and ball.ycor() <= let_Green.ycor() + 20 \
            and ball.xcor() >= let_Green.xcor() - 110 and ball.xcor() <= let_Green.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let_Green.color() == ('Dim Gray', 'Dim Gray'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let_Green.color('Dim Gray')


    if ball.ycor() >= let_Blue.ycor() - 20 and ball.ycor() <= let_Blue.ycor() + 20 \
            and ball.xcor() >= let_Blue.xcor() - 110 and ball.xcor() <= let_Blue.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let_Blue.color() == ('Dim Gray', 'Dim Gray'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let_Blue.color('Dim Gray')


    if ball.ycor() >= let_Violet.ycor() - 20 and ball.ycor() <= let_Violet.ycor() + 20 \
            and ball.xcor() >= let_Violet.xcor() - 110 and ball.xcor() <= let_Violet.xcor() + 110:
        ball.dy = -ball.dy
        score += 1
        s1.clear()
        s1.write(score, font=FONT)
        if let_Violet.color() == ('Dim Gray', 'Dim Gray'):
            score -= 1
            s1.clear()
            s1.write(score, font=FONT)
        let_Violet.color('Dim Gray')

#Dim Gray
window.mainloop()