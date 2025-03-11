#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the homepage."""
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    """Adds two numbers."""
    try:
        data = request.get_json()
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        return jsonify({'result': result})
    except (ValueError, KeyError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/multiply', methods=['POST'])
def multiply():
    """Multiplies two numbers."""
    try:
        data = request.get_json()
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 * num2
        return jsonify({'result': result})
    except (ValueError, KeyError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    """Reverses a string."""
    try:
        data = request.get_json()
        input_string = data['input_string']
        reversed_string = input_string[::-1]
        return jsonify({'reversed_string': reversed_string})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/is_palindrome', methods=['POST'])
def is_palindrome():
    """Checks if a string is a palindrome."""
    try:
        data = request.get_json()
        input_string = data['input_string'].lower().replace(" ", "")
        is_pal = input_string == input_string[::-1]
        return jsonify({'is_palindrome': is_pal})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
