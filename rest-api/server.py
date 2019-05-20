from flask import Flask, jsonify, abort, make_response, request
from tinydb import TinyDB, Query

app = Flask(__name__)
servers = TinyDB('db.json')
Q = Query()


@app.route('/servers', methods=['GET'])
def get_servers():
    return jsonify({'servers': servers.all()})


@app.route('/servers/<string:server_name>', methods=['GET'])
def get_server(server_name):
    for server in servers:
        if (server['name'] == server_name):
            return jsonify({'server': server})
    abort(404)


@app.route('/servers', methods=['POST'])
def create_server():
    if not request.json or not 'name' or not 'type' or not 'location' in request.json:
        abort(400)
    if not isinstance(request.json['name'], str):
        abort(400)
    if not isinstance(request.json['type'], str):
        abort(400)
    if not isinstance(request.json['location'], str):
        abort(400)
    if ('ipaddress' in request.json and not isinstance(request.json['ipaddress'], str)):
        abort(400)
    if ('other' in request.json and not isinstance(request.json['other'], list)):
        abort(400)
    server = {
        'name': request.json['name'],
        'type': request.json['type'],
        'location': request.json['location'],
        'ipaddress': request.json.get('ipaddress', '111.1.1.111'),
        'other': request.json.get('other', [])
    }
    servers.insert(server)
    return jsonify({'server': server}), 201


@app.route('/servers/<string:server_name>', methods=['PUT'])
def update_server(server_name):
    if not request.json:
        abort(400)
    if ('name' in request.json and not isinstance(request.json['name'], str)):
        abort(400)
    if ('type' in request.json and not isinstance(request.json['type'], str)):
        abort(400)
    if ('location' in request.json and not isinstance(request.json['location'], str)):
        abort(400)
    if ('other' in request.json and not isinstance(request.json['name'], list)):
        abort(400)
    servers.update(request.json, Q.name == server_name)
    for server in servers:
        if ('name' in request.json and server['name'] == request.json['name']):
            return jsonify({'server': server})
        elif (server['name'] == server_name):
            return jsonify({'server': server})
    abort(404)


@app.route('/servers/<string:server_name>', methods=['DELETE'])
def delete_server(server_name):
    for server in servers:
        if (server['name'] == server_name):
            servers.remove(Q.name == server_name)
            return jsonify({'result': True})
    abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.debug = True
    app.run()
