import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)


screen.tracer(0)

carmanager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(fun= player.move, key= "Up")


count = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)

    if count % (7-scoreboard.level) == 0:
        carmanager.addcars()

    carmanager.move()

    screen.update()


    # when player touches finish_line
    if player.ycor() == player.finish_line:
        player.restart()
        carmanager.increase_speed()
        scoreboard.level += 1
        scoreboard.display_level()

    # detect collision with cars
    if player.detect_collision(carmanager):
        scoreboard.game_over()
        game_is_on = False


    count += 1

screen.exitonclick()