from toy_robot.direction import Direction


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return f"Position({self.x}, {self.y})"    

    def move(self, direction: Direction, table_size: int) -> None:
        if direction == Direction.NORTH and self.y < table_size - 1:
            self.y += 1
        elif direction == Direction.EAST and self.x < table_size - 1:
            self.x += 1
        elif direction == Direction.SOUTH and self.y > 0:
            self.y -= 1
        elif direction == Direction.WEST and self.x > 0:
            self.x -= 1