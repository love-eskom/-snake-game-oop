import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__() 
        self.shape('circle')
        self.is_bonus = None
        self.shapesize(0.5)
        self.pu()
        self.change_pos()


    def change_pos(self):
        x_pos, y_pos = random.randint(-280, 280), random.randint(-280, 280)
        if random.randint(1, 10) == 10:
            self.shapesize(0.7)
            self.color('red')
            self.is_bonus = True
        else:
            self.color('blue')
            self.is_bonus = False
        self.goto(x_pos, y_pos)