#### Game Results
HIT = 'HIT'
WATER = 'WATER'
SINK = 'SINK'



class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[0] * self.rows for i in range(self.columns)]

    def can_plot_ship_vertically(self, x_axis, y_axis, total_size):
        ship_size = y_axis
        for start in range(y_axis, total_size):
            if self.grid[x_axis][start] == 0:
                ship_size = ship_size + 1
        if ship_size == total_size:
            return True
        return False

    def plot_ship_vertically(self, x_axis, y_axis, ship_name, total_size):
        if self.can_plot_ship_vertically(x_axis, y_axis, total_size):
            for start in range(y_axis, total_size):
                self.grid[x_axis][start] = ship_name
            return True
        return False


    def can_plot_ship_horizontally(self, x_axis, y_axis, total_size):
        ship_size = x_axis
        for start in range(x_axis, total_size):
            if self.grid[start][y_axis] == 0:
                ship_size = ship_size + 1
        if ship_size == total_size:
            return True
        return False

    def plot_ship_horizontally(self, x_axis, y_axis, ship_name, total_size):
        if self.can_plot_ship_horizontally(x_axis, y_axis, total_size):
            for start in range(x_axis, total_size):
                self.grid[start][y_axis] = ship_name
            return True
        return False

    def place_shot(self, x_axis, y_axis):
        ship_name = self.grid[x_axis][y_axis]
        # 1: indicate ship part already got hit
        if ship_name == 1:
            return HIT
        elif ship_name != 0:
            ship_parts_count = self.ship_parts_count(ship_name)
            self.grid[x_axis][y_axis] = 1
            return self.ship_status(ship_parts_count)
        return WATER

    # get_ship_parts_count returns number of ship's parts which are not hit yet
    def ship_parts_count(self, ship_name):
        count = 0
        for x_axis in self.grid:
            for y_axis in x_axis:
                if y_axis == ship_name:
                    count = count + 1
        return count

    #return ship status ["HIT, SINK"]
    def ship_status(self, ship_parts_count):
        if ship_parts_count > 1:
            return HIT
        return SINK

    def reset_board(self):
        # reset board entries to 0
        self.grid = [[0] * self.rows for i in range(self.columns)]


