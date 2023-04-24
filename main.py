from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import the CORS module
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire Flask app

# Define the path to the directory containing the ai-plugin.json file
well_known_dir = os.path.join(app.root_path, '.well-known')

@app.route('/.well-known/<path:filename>')
def well_known(filename):
    return send_from_directory(well_known_dir, filename)

@app.route('/run', methods=['POST'])
def run_command():
    data = request.get_json()
    command = data.get('command')

    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        # Split the output into a list of lines
        output_lines = result.decode('utf-8').splitlines()
        return jsonify({'output': output_lines})
    except subprocess.CalledProcessError as e:
        error_lines = e.output.decode('utf-8').splitlines()
        return jsonify({'error': error_lines}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=3333)
