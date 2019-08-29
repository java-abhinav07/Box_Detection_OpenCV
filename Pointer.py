class Pointer:

    def __init__(self):
        self.direction = '>'
        self.directions = {'>': (1, 0), 'v': (0, 1), '<': (-1, 0), '^': (0, -1)}
        self.helper = {(1, 0): '>', (0, 1): 'v', (-1, 0): '<', (0, -1): '^'}
        self.xcoor = 0
        self.ycoor = 0

    def getDir(self):
        return self.direction

    def getMove(self):
        return self.directions.get(self.direction)

    def right_switch(self):  # /
        move_x, move_y = self.directions.get(self.direction)
        if move_x != 0:
            new_y = move_x * (-1)
            new_x = 0
        elif move_y != 0:
            new_x = move_y * (-1)
            new_y = 0
        self.direction = self.helper.get((new_x, new_y))

    def left_switch(self):  # \
        move_x, move_y = self.directions.get(self.direction)
        if move_x != 0:
            new_y = move_x
            new_x = 0
        elif move_y != 0:
            new_x = move_y
            new_y = 0
        self.direction = self.helper.get((new_x, new_y))


