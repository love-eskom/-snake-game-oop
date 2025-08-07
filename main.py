import time
from food import Food
from turtle import Screen
from snake_data import Snake
from score_board import ScoreBoard
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

food  = Food()
snake = Snake()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.go_up, 'Up')
screen.onkey(snake.go_down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')

game_is_on = True
while game_is_on:
        snake.move()
        screen.update()
        time.sleep(0.08)


        if snake.snake_head.distance(food) < 14: # Detect collision with food
            if food.is_bonus:
                print("Bonus received")
                food.change_pos()
                score.bonus()
            else:
                food.change_pos()
                snake.generate_segment()
                score.update_score()

        for segment in snake.snake[1:]: # Detect collision with body, from the second segment to the last 
            if snake.snake[0].distance(segment) < 5:
                print("Collision with body")
                game_is_on = False

        x = 285 # Detect if player is out of boundaries
        if abs(snake.snake_head.xcor()) > x or abs(snake.snake_head.ycor()) > x:
            score.check_high_score()
            print("Out of boundaries")
            game_is_on = False




screen.exitonclick()
