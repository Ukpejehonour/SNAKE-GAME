from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# --- Screen setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# --- Keyboard controls ---
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# --- Main game loop ---
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.research()
        score.increase_score()
        snake.extend()

    # Detect wall collision
    if abs(snake.segments[0].xcor()) > 280 or abs(snake.segments[0].ycor()) > 280:
        game_is_on = False
        score.gameOver()

    # Detect self-collision
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.gameOver()

screen.exitonclick()
