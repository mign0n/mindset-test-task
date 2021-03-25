from flask import Flask, jsonify

from models import predictor

app = Flask(__name__)


@app.route('/')
def index():
    predictions = predictor.get_forecast().tolist()
    probabilities = predictor.get_probability().tolist()
    policy_id = predictor.policy_id.tolist()
    return jsonify(
        {
            'policy_id': policy_id,
            'predictions': predictions,
            'probabilities': probabilities
        }
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
