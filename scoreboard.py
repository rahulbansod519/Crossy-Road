from turtle import Turtle

FONT = ("Courier", 24, "normal")  # Font style for the scoreboard text


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize inherited attributes from Turtle class

        self.score = 0  # Initialize score to 0

        self.penup()
        self.goto(-250, 260)  # Position the scoreboard on the top left corner
        self.hideturtle()  # Hide the turtle object (scoreboard will be visible)
        self.show_score()  # Display the initial score

    def show_score(self):
        """Updates and displays the current score on the scoreboard."""
        self.clear()  # Clear any previous text on the scoreboard
        self.write(f"Score - {self.score}", font=FONT)  # Write the score with formatted text

    def update_score(self):
        """Increases the score by 1 and displays the updated score."""
        self.score += 1  # Increment the score
        self.show_score()  # Display the updated score

    def game_over(self):
        """Displays a "GAME OVER" message in the center of the screen."""
        self.home()  # Move the turtle to the center of the screen (0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)  # Write "GAME OVER" with centered alignment
