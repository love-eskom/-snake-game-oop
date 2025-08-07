from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        self.xpos = 0
        self.create_snake()
        self.snake_head = self.snake[0]

    def generate_segment(self, position=None):
        """
        generate a new segment
        """
        segment = Turtle()
        segment.pu()
        segment.hideturtle()
        segment.shape('square')
        segment.color('white')
        segment.shapesize(1)
        self.snake.append(segment)

        if position:
            segment.goto(position, 0)
            segment.showturtle()
        else:
            segment.goto(self.snake[-1].pos())
            segment.showturtle()

    def create_snake(self):
        """
        initializes the initial size of the snake
        """
        for _ in range(4):
            self.generate_segment(self.xpos)
            self.xpos -= 20

    def move(self):
        for segment_number in range(len(self.snake) -1, 0, -1):
            new_pos = self.snake[segment_number -1].position()
            self.snake[segment_number].goto(new_pos)
        self.snake_head.forward(10)

    def turn_left(self):
        if self.snake_head.heading() == 90:
            self.snake_head.left(90)
        elif self.snake_head.heading() == 270:
            self.snake_head.right(90)

    def turn_right(self):
        if self.snake_head.heading() == 90:
            self.snake_head.right(90)
        elif self.snake_head.heading() == 270:
            self.snake_head.left(90)

    def go_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def go_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

