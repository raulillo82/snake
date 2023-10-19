from turtle import Turtle

INITIAL_LENGTH = 3
PIXEL_SIZE = 20
SNAKE_COLOR = "white"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = []
for i in range(INITIAL_LENGTH):
    STARTING_POSITIONS.append((-i * PIXEL_SIZE, 0))


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.hideturtle()
        new_segment.color(SNAKE_COLOR)
        new_segment.pu()
        new_segment.goto(STARTING_POSITIONS[i])
        self.segments.append(new_segment)
        self.segments[-1].showturtle()
        #new_segment.showturtle()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        #self.head.left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

