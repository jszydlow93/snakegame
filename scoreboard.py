from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()  # Load the high score from a file
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Starting position of the scoreboard
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display with the current score and high score."""
        self.clear()  # Clear the current text
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Show 'Game Over' and prompt to retry."""
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER\nPress Enter to Retry", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset the score and update the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()  # Save the new high score to a file
        self.score = 0
        self.goto(0, 270)  # Reset position to the top for the scoreboard
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def save_high_score(self):
        """Save the high score to a file."""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        """Load the high score from a file."""
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0  # If the file doesn't exist, start with 0
