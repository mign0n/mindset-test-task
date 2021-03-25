from flask import jsonify

from webapp.models import predictor
from webapp import app


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
