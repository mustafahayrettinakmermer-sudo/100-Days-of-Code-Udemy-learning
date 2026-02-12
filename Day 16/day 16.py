# import turtle

from turtle import Turtle, Screen, forward, left
"""timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
for steps in range(100):
    timmy.forward(steps)
    timmy.left(20)


my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()"""
from prettytable import PrettyTable
table = PrettyTable() 
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])
table.align = "c"


print(table)