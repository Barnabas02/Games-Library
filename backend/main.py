from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app,resources={r"/*":{'origins':"*"}})
# CORS(app,resources={r"/*":{'origins':'http;//localhost:8080', "allow_headers": "Access-Controll-Allow-Origin"}})

# hellow world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello World!")

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!")

GAMES = [
    {   
         'id': uuid.uuid4().hex,
        'title': 'FIFA',
        'genre': 'Sports',
        'played': True,
    },
    {
         'id': uuid.uuid4().hex,
        'title': '2k21',
        'genre': 'Sports',
        'played': False,
    },
    {
         'id': uuid.uuid4().hex,
        'title': '007',
        'genre': 'action',
        'played': True,
    },
    {
         'id': uuid.uuid4().hex,
        'title': 'Apex',
        'genre': 'Sports',
        'played': False,
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Resident Evil',
        'genre': 'Horror',
        'played': False,
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Rising Star',
        'genre': 'horro',
        'played': True,
    }
]
# the get route handler

# GET and POST handler
@app.route('/games', methods=['GET','POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method =="POST":
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')        
        })
        response_object['message'] = 'Game Added!'
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)

# PUT and DELETE handlers
@app.route('/games/<game_id>', methods=['PUT','DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')        
        })
        response_object['message'] = 'Game Updated!'
    if request.method == "DELETE":        
        remove_game(game_id)
        response_object['message'] = 'Game Deleted!'
    return jsonify(response_object)

def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False


if __name__ == "__main__":
    app.run(debug=True)