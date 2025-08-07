import random
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(0, 250)
        self.color('white')
        self.high_score = 0
        self.score = 0
        self.write_score()

    def write_score(self):
        """
        displays the score
        """
        self.clear()
        try:
            self.get_highscore()
        except(ValueError, FileNotFoundError):
            self.high_score = 0
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align='center', font=('Ariel', 10, 'normal'))

    def get_highscore(self):
        """
        retrieves the value for highscore from the score_data file
        """
        with open('score_data.txt', mode='r') as highscore:
            self.high_score = int(highscore.read())

    def update_score(self):
        """
        increments score by one
        """
        self.score += 1
        self.write_score()

    def check_high_score(self):
        """
        Updates highscore and saves it to the score-data.txt file
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score_data.txt', mode='w') as file:
                file.write(str(self.high_score))
            self.write_score()

    def bonus(self):
        bonus_amount = random.randint(4,12)
        self.score += bonus_amount
        self.write_score()