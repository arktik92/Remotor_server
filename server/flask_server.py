from flask import Flask, request
from server.handlers import handle_command

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def execute_command():
    command = request.json.get('command')
    if command:
        handle_command(command)
        return {'message': 'Command executed successfully'}
    else:
        return {'error': 'Invalid command'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)