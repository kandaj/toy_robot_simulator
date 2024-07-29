class Table:
    def __init__(self, size: int):
        self.size = size

    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size