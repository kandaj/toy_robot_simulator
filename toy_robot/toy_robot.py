from typing import Optional
from toy_robot.direction import Direction
from toy_robot.position import Position
from toy_robot.table import Table


class ToyRobot:
    def __init__(self, table_size: int = 5):
        self.position: Optional[Position] = None
        self.facing: Optional[Direction] = None
        self.table = Table(table_size)

    def place(self, x: int, y: int, facing: str) -> None:
        if not self.table.is_within_bounds(x, y) or \
                facing not in Direction.__members__:
            self.position = None
            self.facing = None
            return
        self.position = Position(x, y)
        self.facing = Direction[facing]

    def move(self) -> None:
        if self.position and self.facing:
            self.position.move(self.facing, self.table.size)

    def left(self) -> None:
        if self.facing:
            self.facing = {
                Direction.NORTH: Direction.WEST,
                Direction.WEST: Direction.SOUTH,
                Direction.SOUTH: Direction.EAST,
                Direction.EAST: Direction.NORTH
            }[self.facing]

    def right(self) -> None:
        if self.facing:
            self.facing = {
                Direction.NORTH: Direction.EAST,
                Direction.EAST: Direction.SOUTH,
                Direction.SOUTH: Direction.WEST,
                Direction.WEST: Direction.NORTH
            }[self.facing]

    def report(self) -> Optional[str]:
        if self.position and self.facing:
            return f"{self.position.x},{self.position.y},{self.facing.value}"
        return None

    def execute_command(self, command):
        if not command.strip():
            print("Invalid command.")
            return
        parts = command.split()
        if parts[0] == 'PLACE' and len(parts) == 2:
            try:
                x, y, direction = parts[1].split(',')
                self.place(int(x), int(y), direction)
            except ValueError:
                print("Invalid PLACE command format.")
        elif parts[0] == 'MOVE':
            self.move()
        elif parts[0] == 'LEFT':
            self.left()
        elif parts[0] == 'RIGHT':
            self.right()
        elif parts[0] == 'REPORT':
            report = self.report()
            if report:
                print("Output:" + report)
        else:
            print("Invalid command.")