import turtle
import random
import time

screen = turtle.Screen()
screen.title("Crossy Road")
screen.bgcolor("green")
screen.setup(width=800, height=700)
screen.tracer(0)

player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.goto(0, -300)
player.setheading(90)

player_speed = 25

score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(-370, 310)

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 20, "bold"))

update_score()

cars = []
car_colors = ["red", "blue", "yellow", "orange", "purple"]

def create_car(y):
    car = turtle.Turtle()
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=2)
    car.color(random.choice(car_colors))
    car.penup()

    if random.choice([True, False]):
        car.goto(-450, y)
        car.direction = 1
    else:
        car.goto(450, y)
        car.direction = -1

    car.speed = random.randint(3, 7)
    cars.append(car)

road_y_positions = [-225, -150, -75, 0, 75, 150, 225]

road = turtle.Turtle()
road.hideturtle()
road.penup()

for y in road_y_positions:
    road.goto(-400, y - 25)
    road.color("gray")
    road.begin_fill()

    for _ in range(2):
        road.forward(800)
        road.left(90)
        road.forward(50)
        road.left(90)

    road.end_fill()

def move_up():
    player.sety(player.ycor() + player_speed)

def move_down():
    player.sety(player.ycor() - player_speed)

def move_left():
    player.setx(player.xcor() - player_speed)

def move_right():
    player.setx(player.xcor() + player_speed)

screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

def reset_game():
    global score

    player.goto(0, -300)

    for car in cars:
        car.hideturtle()

    cars.clear()

    score = 0
    update_score()

last_car_time = time.time()

while True:
    screen.update()

    if player.xcor() > 380:
        player.setx(380)

    if player.xcor() < -380:
        player.setx(-380)

    if player.ycor() > 330:
        score += 1
        update_score()
        player.goto(0, -300)

        for car in cars:
            car.speed += 0.5

    if player.ycor() < -330:
        player.sety(-330)

    if time.time() - last_car_time > 1:
        y = random.choice(road_y_positions)
        create_car(y)
        last_car_time = time.time()

    for car in cars:
        car.setx(car.xcor() + car.speed * car.direction)

        if car.xcor() > 450:
            car.goto(-450, car.ycor())

        if car.xcor() < -450:
            car.goto(450, car.ycor())

        if player.distance(car) < 30:
            reset_game()

    time.sleep(0.02)