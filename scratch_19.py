import time
import turtle
import math

def check_range_from_circle(x, y, pos):
    return math.sqrt((x - pos[0])**2 + (y - pos[1])**2)

t = turtle.Turtle()
t.shape("turtle")

time_limit = 10

circle_x_pos = 300
circle_y_pos = 280
circle_radius = 20

t.up()
t.goto(circle_x_pos, circle_y_pos)
t.down()
t.circle(circle_radius)
t.up()

t.goto(0, 0)
t.down()

started_at = time.time()
while True:
    timedelta = time.time() - started_at
    print(timedelta, "초 지났습니다.")
    t.write(int(timedelta))
    command = input()
    if command == "l":
        t.left(90)
        t.forward(100)
    elif command == "r":
        t.right(90)
        t.forward(100)
    else:
        continue
    if time_limit < timedelta:
        print("게임 오버!")
        t.write("게임 오버!")
        break
    elif check_range_from_circle(circle_x_pos, circle_y_pos, t.pos()) < circle_radius:
        print("이겼습니다!")
        t.write("이겼습니다!")

turtle.done()