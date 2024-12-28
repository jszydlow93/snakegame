import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off screen updates for better performance

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()


def reset_game():
    """Reset the game and clear the retry message."""
    global game_is_on
    game_is_on = True
    snake.reset_segments()
    food.refresh()
    scoreboard.reset()
    run_game()  # Restart the game loop


# Set up controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(reset_game, "Return")  # Bind the Enter key to reset the game

# Game loop
def run_game():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)  # Control the game speed

        # Move the snake
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
                snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:  # Skip the head
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


# Start the game loop
game_is_on = True
run_game()

screen.exitonclick()
