from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.restart()
        self.left(90)
        self.finish_line = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.penup()
        self.goto(STARTING_POSITION)


    def detect_collision(self, carmanager):
        for cars in carmanager.carlist:
            if self.distance(cars) < 25:
                return True
