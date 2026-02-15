import random
from turtle import Turtle, Screen, colormode

tim = Turtle()
tim.shape("turtle")
tim.color("red")
colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#For a square
#for _ in range(4):
#    tim.forward(100)
#    tim.right(90)


#For dashed line
#for _ in range(50):
#    tim.forward(3)
#    tim.penup()
#    tim.forward(3)
#    tim.pendown()


#Draw a triangle, square, pentagon, hexagon, heptagon,octagon, nonagon, and decagon
"""def drwas_shapes(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)
    
for shape_side in range(3, 11):
    drwas_shapes(shape_side)"""

#Challenge 4, Random Walk
"""screen = Screen()
screen.setup(600, 600)
STEP = 20
LIMIT = 280

def up_direction():
    tim.right(-90)
    tim.forward(50)

def down_direction():
    tim.right(90)
    tim.forward(50)

def left_direction():
    tim.forward(-50)
def right_direction():
    tim.forward(50)


random_direction = [up_direction,down_direction, left_direction, right_direction]"""


"""def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r,g,b)
    return random_color"""
    


"""for _ in range(100):
    move = random.choice(random_direction)
    move()
    tim.color(random.choice(colours))
    tim.speed("fastest")
    tim.pensize(10)

    x = tim.xcor()
    y = tim.ycor()

    # If the turtle hits a wall, turn it back
    if x > LIMIT or x < -LIMIT:
        tim.setheading(180 - tim.heading())

    if y > LIMIT or y < -LIMIT:
        tim.setheading(-tim.heading())"""


#Challenge 5 Drawinfg circles
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

number_of_circles = int(360 / 5)

for _ in range(number_of_circles):
    tim.color(random_color())
    tim.circle(150)
    tim.right(5)
    tim.speed("fastest")
    


















screen = Screen()
screen.exitonclick()
