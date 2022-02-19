
import ast
from flask import *

from lstm_classifier import prediction_pipeline

app = Flask(__name__)


@app.post('/movie_review_predictor')
def get_review_sentiment():
    prediction_dt = {}
    try:
        if request.method == 'POST':
            req_json = ast.literal_eval(request.get_data(as_text=True))
            description = req_json['movie review']
            sentiment = prediction_pipeline(description)
            prediction_dt = {'review sentiment': sentiment}
    except Exception as ex:
        print("Exception occured in get_technology_url-->", ex)
    return jsonify(prediction_dt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, threaded=True)