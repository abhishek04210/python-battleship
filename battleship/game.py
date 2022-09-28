from collections import defaultdict
from battleship.board import Board
from battleship.ship import Ship

class Game:
    def __init__(self, rows, columns):
        self.board = Board(rows, columns)

    def create(self, data):
        data = data.get("ships")
        index = 0
        print("data&&&",data)
        for ship in data:
            print("entering into game section ship", ship)
            ship_name = f"ship{index}"
            x_axis = ship.get("x")
            y_axis = ship.get("y")
            size = ship.get("size")
            direction = ship.get("direction")
            ship_obj = Ship(x_axis, y_axis, size, ship_name, direction)
            print("ship objects**",ship_obj)
            index = index + 1
            if not ship_obj.plot_ships(self.board):
                return False
        return True



    def fire(self, payload):
        x_axis = payload.get("x")
        y_axis = payload.get("y")
        return self.board.place_shot(x_axis, y_axis)

    def reset_game(self):
        self.board.reset_board()
        return True