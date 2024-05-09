import random
from turtle import Turtle, register_shape

STARTING_MOVE_DISTANCE = 5  # Initial movement distance for cars
MOVE_INCREMENT = 10       # Amount to increase movement distance each time
CUSTOME_SHAPE = "Custome_Shape/car.gif"  # Path to the custom car image
y_pos = random.randint(-300, 300)  # Random y-position for car creation (unused in this code)


class CarManager:
    def __init__(self):
        self.all_cars = []  # List to store all created car objects

    def create_car(self):
        """Creates a new car with a 1 in 6 chance.

        This method creates a new car object with a custom car image, sets
        its properties (heading, position, etc.), and adds it to the list
        of all cars. There's a 1 in 6 chance (approximately 16.6%) that a
        new car will be created on each call.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            register_shape(CUSTOME_SHAPE)
            new_car.shape(CUSTOME_SHAPE)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)  # Make the car face left
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars forward by the current movement distance.

        This method iterates through all cars in the `all_cars` list and
        moves them forward by the value of `STARTING_MOVE_DISTANCE`.
        """
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
