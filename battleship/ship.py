### Directions in V & H

VERTICAL = 'V'
HORIZONTAL = 'H'


class Ship:
    def __init__(self, x_axis, y_axis, size, ship_name, direction):
        self.ship_name =  ship_name
        self.x_axis =  x_axis
        self.y_axis =  y_axis
        self.size =  size
        self.direction = direction


    def plot_ships(self, board):
        if self.direction == VERTICAL:
            total_size = self.y_axis + self.size
            try:
                return board.plot_ship_vertically(self.x_axis, self.y_axis, self.ship_name, total_size)
            except IndexError:
                return False
        elif self.direction == HORIZONTAL:
            total_size = self.x_axis + self.size
            try:
                return board.plot_ship_horizontally(self.x_axis, self.y_axis, self.ship_name, total_size)
            except IndexError:
                return False
        return False