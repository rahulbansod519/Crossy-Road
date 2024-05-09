import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates for better performance

# Create game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkeypress(player.go_up, "Up")  # Bind "Up" key to player movement

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Introduce a slight delay between updates

    # Update the screen manually
    screen.update()

    # Create new cars at random intervals
    car_manager.create_car()

    # Move all cars forward
    car_manager.move_cars()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Check if distance to player is less than 20 (collision threshold)
            game_is_on = False
            scoreboard.game_over()  # Display game over message

    # Check if player reached the finish line
    if player.is_finish_line():
        player.go_to_start()  # Move player back to starting position
        scoreboard.update_score()  # Increase score

# Exit the game when the window is closed
screen.exitonclick()
