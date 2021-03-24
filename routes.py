from flask import Flask, jsonify

from models import predictor

app = Flask(__name__)


@app.route('/')
def index():
    predictions = predictor.get_forecast().tolist()
    return jsonify({'predictions': predictions})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
