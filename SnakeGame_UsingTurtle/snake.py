from turtle import Turtle
from time import sleep
import random
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.mpos = self.turtle_list[0].pos()




    def create_snake(self):
        for turtle_index in range(0, 3):
            self.add_segment(turtle_index)

    def add_segment(self, turtle_index):
        px = 0
        color = ["white", "red", "blue", "orange", "cyan", "pink"]
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color(random.choice(color))
        new_turtle.setx(px)
        px -= 20
        self.turtle_list.append(new_turtle)


    def extend(self):
        self.add_segment(self.turtle_list[-1].position())


    def move(self, direction):

        for seg_num in range(len(self.turtle_list) -1 , 0, -1):
            x = self.turtle_list[seg_num - 1].xcor()
            y = self.turtle_list[seg_num - 1].ycor()
            self.turtle_list[seg_num].goto(x, y)

        if direction == "null":
            self.turtle_list[0].forward(MOVE_DISTANCE)


    def distance(self, food):
        return self.turtle_list[0].distance(food)


    def wallhit(self):
        x = self.turtle_list[0].xcor()
        y = self.turtle_list[0].ycor()
        if x > 300 or y > 300 or x < -300 or y < -300:
            return True

        else:
            return False


    def up(self):
        heading = self.turtle_list[0].heading()
        tpos = self.turtle_list[0].pos()
        if tpos != self.mpos:
            if heading == 0 or heading == 180:
                self.turtle_list[0].setheading(90)
                self.mpos = self.turtle_list[0].pos()

    def snakecollide(self):
        pass




    def down(self):

        heading = self.turtle_list[0].heading()
        tpos = self.turtle_list[0].pos()
        if tpos != self.mpos:
            if heading == 0 or heading == 180:
                self.turtle_list[0].setheading(270)
                self.mpos = self.turtle_list[0].pos()

    def left(self):

        heading = self.turtle_list[0].heading()
        tpos = self.turtle_list[0].pos()
        if tpos != self.mpos:
            if heading == 90 or heading == 270:
                self.turtle_list[0].setheading(180)
                self.mpos = self.turtle_list[0].pos()

    def right(self):

        heading = self.turtle_list[0].heading()
        tpos = self.turtle_list[0].pos()
        if tpos != self.mpos:
            if heading == 90 or heading == 270:
                self.turtle_list[0].setheading(0)
                self.mpos = self.turtle_list[0].pos()


