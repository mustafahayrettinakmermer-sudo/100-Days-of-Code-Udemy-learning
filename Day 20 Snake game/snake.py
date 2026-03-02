from turtle import Turtle, position

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        x = 0
        for _ in range(3):
            self.add_segment((x, 0))
            x -= 20

        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extent(self):
        self.add_segment(self.segments[-1].position())




    def snake_up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def snake_down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)

    def snake_left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def snake_right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)