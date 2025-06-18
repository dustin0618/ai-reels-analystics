from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer.scoring import calculate_normalized_score, analyze_boost, predict_views

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    req = request.get_json()
    url = req.get('url')

    mock_data = {
        'views': 8000,
        'likes': 120,
        'comments': 6,
        'saves': 2,
        'shares': 1,
        'avg_watch_time': 9,
        'duration': 15
    }

    score, norm = calculate_normalized_score(mock_data)
    boost, explanation = analyze_boost(norm, mock_data['views'])
    projected_views = predict_views(mock_data['views'], boost)

    return jsonify({
        'url': url,
        'score': score,
        'projectedViews': projected_views,
        'metrics': mock_data,
        'boost': boost,
        'explanation': explanation
    })
