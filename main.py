from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

well_known_dir = os.path.join(app.root_path, '.well-known')

@app.route('/.well-known/<path:filename>')
def well_known(filename):
    return send_from_directory(well_known_dir, filename)

@app.route('/run', methods=['POST'])
def run_command():
    data = request.get_json()
    commands = data.get('commands')

    if not commands:
        return jsonify({'error': 'No commands provided'}), 400

    output = {}
    for i, command in enumerate(commands):
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            output_lines = result.decode('utf-8').splitlines()
            output[f"command_{i}"] = {'output': output_lines}
        except subprocess.CalledProcessError as e:
            error_lines = e.output.decode('utf-8').splitlines()
            output[f"command_{i}"] = {'error': error_lines}

    return jsonify(output)

if __name__ == '__main__':
    app.run(host='localhost', port=3333)
