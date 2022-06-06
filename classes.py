class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self, blocks_count):
        return 0 <= self.x < blocks_count and 0 <= self.y < blocks_count

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and\
               self.x == other.x and self.y == other.y


class Bad_block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Bad_block) and\
               self.x == other.x and self.y == other.y
