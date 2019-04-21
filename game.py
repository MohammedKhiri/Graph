import turtle
import math
import random
# set up the secren
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")


# draw windows border

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.begin_fill()
border_pen.color("Gainsboro")
border_pen.color("DarkGreen")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.color("Gainsboro")
border_pen.end_fill()
border_pen.hideturtle()


# score point enemy
score = 0
score_requier = 1
score_pin = turtle.Turtle()
score_pin.speed(0)
score_pin.color("DarkCyan")
score_pin.pu()
score_pin.setposition(-280, 275)
score_string = "Score: %s" % score + " / %s" % score_requier
score_pin.write(score_string, False, align="left", font=( "Tahoma", 13, "normal"))
score_pin.hideturtle()

# score point enemy
level_number = 1
level = turtle.Turtle()
level.speed(0)
level.color("Teal")
level.pu()
level.setposition(200, 275)
level_string = "level: %s" % level_number
level.write(level_string, False, align="left", font=( "Tahoma", 13, "normal"))
level.hideturtle()

line_border = turtle.Turtle()
line_border.speed(0)
line_border.color("DarkGreen")
line_border.pensize(20)

line_border.pu()
line_border.setposition(300, 260)
level_string = "----------------------------------------------------------------------------------------------------"
line_border.write(level_string, False, align="right", font=( "Tahoma", 13, "normal"))
line_border.hideturtle()


# greate player design
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.pu()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)



# number of enemy
number_of_enmey=6
enemies = []
enemy_color = ["FireBrick","red","green","OrangeRed","cyan"]
for i in range(number_of_enmey):
    enemies.append(turtle.Turtle())
    # greate enemy
for enemy in enemies:
    co = random.randint(0, 4)
    enemy.color(enemy_color[co])
    enemy.shape("circle")
    enemy.pu()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
# enemy speed
enemy_speed = 2

# player speed
playerspeed = 15


# great player bullet
bullet = turtle.Turtle()
co=random.randint(0,4)
bullet.color(enemy_color[co])
bullet.shape("circle")
bullet.pu()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
# bullet speed
bullet_speed=40
# bullet state

# ready to fire
bullet_state = "ready"


# is fire




# player move left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


# player move left
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

# bullet_fire
def bullet_fire():
    # declare bullet fire as global vareble to see change
    global bullet_state
    # move bullet with player
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()
# collision the bullet with enemy
def is_collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



# greate keybord control

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(bullet_fire,"space")

# main_game loop
while True:
    if score == score_requier:
        level_number = level_number +1
        level_string = "level: %s" % level_number
        level.clear()
        level.write(level_string, False, align="left", font=("Tahoma", 13, "normal"))
        score = 0

        score_requier = score_requier + 1

    for enemy in enemies:
        # move_enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
        # move enemy to back cord
        if enemy.xcor() > 280:
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                e.sety(y)
            enemy_speed = enemy_speed * -1


        if enemy.xcor() < -280:
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                e.sety(y)
            enemy_speed = enemy_speed * -1

        # check for collision is happened
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            # enemy.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 1
            score_string = "Score: %s" % score + " / %s" % score_requier
            score_pin.clear()
            score_pin.write(score_string, False, align="left", font=("Tahoma", 13, "normal"))


        # player dead game over
        if is_collision(player, enemy):
            player.hideturtle()
            bullet.hideturtle()
            for e in enemies:
                e.hideturtle()
            print("game over")
            break


    # move bullet
    if bullet_state == "fire":
        y=bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
    # check if the bull is out of range
    if bullet.ycor() > 250:
        bullet.hideturtle()
        bullet_state = "ready"


turtle.done()