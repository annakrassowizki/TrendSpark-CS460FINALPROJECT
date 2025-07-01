import math
import datetime
import random
from typing import List, Dict

def compute_trendspark_score(post_time: float, comments: List[Dict], weights=(0.2, 0.3, 0.5), threshold=0.5) -> Dict:
    w1, w2, w3 = weights

    timestamps = sorted([c['timestamp'] for c in comments])
    time_diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_diff = sum(time_diffs) / len(time_diffs) if time_diffs else 1
    burstiness = 1 / avg_diff if avg_diff > 0 else 0

    influence = sum(
        math.log(1 + c['user_karma']) / (c['timestamp'] - post_time + 1)
        for c in comments
    )

    unique_users = len(set(c['user_id'] for c in comments))
    top_level = [c for c in comments if c['parent_id'] == "post_id"]
    branching_factor = unique_users + len(top_level)

    nb = min(burstiness / 0.1, 1.0)
    ni = min(influence / 10, 1.0)
    nbf = min(branching_factor / 50, 1.0)

    score = w1 * nb + w2 * ni + w3 * nbf

    return {
        "Burstiness": burstiness,
        "Influence": influence,
        "Branching Factor": branching_factor,
        "TrendSpark Score": score,
        "Predicted Viral": score >= threshold
    }

def generate_mock_data():
    post_time = datetime.datetime(2025, 6, 25, 12, 0, 0).timestamp()
    comments = []
    for i in range(30):
        timestamp = post_time + random.randint(600, 3600)
        karma = random.randint(1, 50)
        user_id = f"user{random.randint(1, 300)}"
        parent_id = "post_id" if random.random() < 0.7 else f"comment{random.randint(1, i)}"
        comments.append({
            'timestamp': timestamp,
            'user_id': user_id,
            'user_karma': karma,
            'parent_id': parent_id
        })
    return post_time, comments