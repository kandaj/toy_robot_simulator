# Toy Robot Package

This package provides a command-line interface to control a toy robot.

## Installation

To install the package and its dependencies, run:

```sh
pip install -r requirements.txt

```

Usage
To run the toy robot simulator, use the following command:

```sh
python -m toy_robot
```

You will be prompted to enter commands for the toy robot. The available commands are:

PLACE X,Y,F: Places the robot at the specified coordinates (X, Y) facing the specified direction (F). The direction must be one of NORTH, SOUTH, EAST, or WEST.
MOVE: Moves the robot one unit forward in the direction it is currently facing.
LEFT: Rotates the robot 90 degrees to the left.
RIGHT: Rotates the robot 90 degrees to the right.
REPORT: Outputs the robot's current position and direction.
EXIT: Exits the simulator.

Example session:

```
Enter commands for the toy robot (type 'EXIT' to quit):
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
LEFT
MOVE
REPORT
Output: 0,1,WEST
EXIT
Exiting the toy robot simulator. Goodbye!
```


Running Tests
To run the test cases, you need to have pytest installed. If you don't have it installed, you can install it using:

pip install -r requirements.txt

Once pytest is installed, you can run the tests by navigating to the root directory of the project and executing:

``` pytest ```

This will discover and run all the test cases in the tests directory.