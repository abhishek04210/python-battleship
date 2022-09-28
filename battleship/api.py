from distutils.log import error
import http
import flask
import json
from flask import request, jsonify
from battleship.game import Game
from jsonschema import validate, ValidationError, SchemaError
from battleship.valids import request_validation
COL_SIZE = 10
ROW_SIZE = 10

app = flask.Flask(__name__)
game = Game(ROW_SIZE,COL_SIZE)

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    response = request.data.decode("utf-8")
    data = json.loads(response)
    ships = data.get("ships")
    try:
        validate(data, request_validation.get("CREATE"))
        for ship in ships:
            validate(ship, request_validation.get("SHIP"))
        print("data***",data)
        val = game.create(data)
        if val:
            return jsonify({"result": "Game created"}), 200
        return jsonify({"message": "Bad Request"}), 400
    except ValidationError as e:
        print("errors are :",e)
        return jsonify({"message": "Bad Request","error":e}), 400

@app.route('/battleship', methods=['PUT'])
def shot():
    response = request.data.decode("utf-8")
    coordinates = json.loads(response)
    try:
        validate(coordinates, request_validation.get("SHOT"))
        val = game.fire(coordinates)
        return jsonify({"result": val}), 200
    except ValidationError as e:
        return jsonify({"result": "Bad Request"}), 400


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    game.reset_game()
    return jsonify({"result": "Game has been reset successfully"}), 200
