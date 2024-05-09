from turtle import Turtle, register_shape

STARTING_POSITION = (0, -280)  # Initial position of the player turtle
MOVE_DISTANCE = 10           # Amount to move the player turtle each time
FINISH_LINE_Y = 280           # Y-coordinate of the game's finish line


class Player(Turtle):
    def __init__(self):
        super().__init__()  # Initialize inherited attributes from Turtle class

        self.shape("turtle")  # Set the player's shape to the default turtle
        self.penup()          # Lift the pen to avoid drawing while moving
        self.goto(STARTING_POSITION)  # Move the player to the starting position
        self.setheading(90)     # Set the player to face upwards (90 degrees)

    def go_up(self):
        """Moves the player turtle forward by the MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Moves the player turtle back to the STARTING_POSITION."""
        self.goto(STARTING_POSITION)

    def is_finish_line(self):
        """Checks if the player turtle has crossed the finish line.

        Returns:
            True if the player's y-coordinate is greater than FINISH_LINE_Y (crossed finish line), False otherwise.
        """
        return self.ycor() > FINISH_LINE_Y  # Check if player's y-position is past the finish line
