import random
from turtle import Turtle, register_shape

# Set the path to the custom car shape
CUSTOME_SHAPE = "Custome_Shape/car.gif"

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        # Randomly create cars with a 1 in 6 chance
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            # Register the custom car shape
            register_shape(CUSTOME_SHAPE)
            new_car.shape(CUSTOME_SHAPE)
            # Stretch the car shape to the desired size
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            # Set a random y position for the new car
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            # Add the new car to the list of all cars
            self.all_cars.append(new_car)

    def move_cars(self):
        # Move all cars forward
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
