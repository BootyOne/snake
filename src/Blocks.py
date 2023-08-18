class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self, blocks_count):
        return 0 <= self.x < blocks_count and 0 <= self.y < blocks_count

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


class BadBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, BadBlock) and self.x == other.x and self.y == other.y
