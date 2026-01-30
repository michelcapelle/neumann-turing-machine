import pika
from bletchley import Chat
from bletchley import Channel
from flask import Flask, request, jsonify, abort
from flask_swagger_ui import get_swaggerui_blueprint
from game import Game


app = Flask(__name__)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "The Neumann-Turing Machine API",
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
chat = Chat()
channel: pika.channel.Channel = Channel(connection=pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost', 
        credentials=pika.PlainCredentials('admin', 'admin'),
        heartbeat=60,
        blocked_connection_timeout=30,
    )
), queue_name='game_queue')

@app.route('/api/v1/hello', methods=['GET'])
def hello_multipolar_world():
    return jsonify(message="Hello, Multipolar World!")

@app.route('/api/v1/game', methods=['POST'])
def generate_game():
    data: object = request.json
    side_a: str = data.get('side_a', '')
    side_b: str = data.get('side_b', '')
    game = Game(side_a=side_a, side_b=side_b, qas=[])
    chat.insert(game)
    return jsonify(game.__dict__), 201

@app.route('/api/v1/game/<string:id>/turn', methods=['POST'])
def perform_next_turn(id):
    game: Game = chat.retrieve(Game, id)
    if game:
        channel.send(game._id)
        return id, 202
    abort(404, description="Game not found")

@app.route('/api/v1/game/last/turn', methods=['POST'])
def perform_last_game_next_turn():
    game: Game = chat.last(Game)
    if game:
        channel.send(game._id)
        return game._id, 202
    abort(404, description="No games found")
    
@app.route('/api/v1/game/<string:id>', methods=['GET'])
def retrieve_game(id):
    game: Game = chat.retrieve(Game, id)
    if game:
        return jsonify(game.__dict__), 200
    else:
        abort(404, description="Game not found")

@app.route('/api/v1/game/last', methods=['GET'])
def retrieve_last_game():
    game: Game = chat.last(Game)
    if game:
        return jsonify(game.__dict__), 200
    else:
        abort(404, description="No games found")

if __name__ == '__main__':
    app.run(debug=False)
