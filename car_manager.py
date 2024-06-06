COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager():

    def __init__(self):
        self.carlist = []
        self.move_speed = 5


    def addcars(self):
        new_car = Turtle()
        new_car.hideturtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        new_car.showturtle()
        new_car.setheading(180)
        self.carlist.append(new_car)

    def move(self):
        for cars in self.carlist:
            cars.forward(self.move_speed)
            if cars.xcor() < -320:
                self.carlist.remove(cars)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT





