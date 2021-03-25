from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKEGAME")
screen.tracer(0)



# t1 = Turtle(Turtle.setp)
# t2 = Turtle()

Tom = Snake()
Food = Food()
screen.update()
game_is_on = True
score = Scoreboard()
screen.listen()
screen.onkey(Tom.up, "Up")

screen.onkey(Tom.down, "Down")


screen.onkey(Tom.left,"Left")

screen.onkey(Tom.right, "Right")

while game_is_on:
    screen.update()
    sleep(.05)
#====================================

    Tom.move("null")

    #detect fooood colision
    tom_dist = Tom.distance(Food)
    if tom_dist < 50:
        print(tom_dist)
    if tom_dist < 15:
        Food.collide()
        score.update()
        Tom.extend()
    if Tom.wallhit():
        print("WALLHIT WALLHIT WALLHIT")
        score.gameover()
        screen.update()
        game_is_on = False
    for segment in Tom.turtle_list[1:]:
        if Tom.turtle_list[0].distance(segment) < 10:
            print("SNAKSANKSNAKNS")
            game_is_on = False
            score.gameover()
            screen.update()






screen.exitonclick()
