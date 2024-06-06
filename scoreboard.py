FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

   def __init__(self):
       super().__init__()
       self.hideturtle()
       self.penup()
       self.color("black")
       self.level = 1
       self.display_level()

   def display_level(self):
       self.clear()
       self.goto(-200, 250)
       self.write(f"Level: {self.level}", align="Center", font= FONT )

   def game_over(self):
       self.goto(0,0)
       self.write("GAME OVER", align="Center", font= FONT )


