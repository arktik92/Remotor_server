from flask import Flask, request
from handlers import handle_command
import threading

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return {'message': 'connection established successfully'}


@app.route('/command', methods=['POST'])
def execute_command():
    command = request.json.get('command')
    if command:
        callback = handle_command(command)
        return callback
    else:
        return {'error': 'Invalid command'}, 400


def start_server():
    def run():
        app.run(host='0.0.0.0', port=12345, debug=False)

    # Lancer le serveur Flask dans un thread
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
