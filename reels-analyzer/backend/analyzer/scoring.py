def calculate_normalized_score(data):
    weights = {
        'likes': 0.2,
        'comments': 0.3,
        'saves': 0.4,
        'shares': 0.5,
        'watch_time_factor': 0.6,
        'completion_rate': 0.3
    }
    norm = {
        'likes': data['likes'] / data['views'] * 1000,
        'comments': data['comments'] / data['views'] * 1000,
        'saves': data['saves'] / data['views'] * 1000,
        'shares': data['shares'] / data['views'] * 1000,
        'watch_time_factor': data['avg_watch_time'] / data['duration'],
        'completion_rate': data['avg_watch_time'] / data['duration']
    }
    score = min(10, round(sum(norm[k] * weights[k] for k in weights), 2))
    return score, norm

def analyze_boost(norm, views):
    thresholds = {
        'likes': 20,
        'comments': 5,
        'saves': 3,
        'shares': 2
    }
    boost = {}
    explanation = {}
    for k in ['likes', 'comments', 'saves', 'shares']:
        current = norm[k]
        required = thresholds[k]
        if current < required:
            need = int(round((required - current) * views / 1000))
            boost[k] = need
            explanation[k] = f"현재 {k} 수치는 1,000뷰당 {current:.1f}건으로 기준치({required})보다 낮습니다. 약 {need}건 보강 필요."
        else:
            boost[k] = 0
            explanation[k] = f"{k}는 기준 이상."
    return boost, explanation

def predict_views(views, boost):
    return int(views + boost['likes']*3 + boost['comments']*10 + boost['saves']*12 + boost['shares']*15)
