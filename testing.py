from trendspark import compute_trendspark_score
import datetime

# Helper to simulate a test case
def simulate_test(post_time, comments, description, expected):
    result = compute_trendspark_score(post_time, comments, weights=(0.5, 0.2, 0.3), threshold=0.6)
    print(f"\n[Test] {description}")
    print(f"Expected: {expected}, Actual: {result['Predicted Viral']}, Score: {result['TrendSpark Score']:.4f}")

# Test Case 1: High volume, low diversity
post_time = datetime.datetime(2025, 6, 25, 12, 0, 0).timestamp()
comments = [
    {'timestamp': post_time + i * 120, 'user_id': 'user1', 'user_karma': 300, 'parent_id': 'post_id'}
    for i in range(30)
]
simulate_test(post_time, comments, "High volume, low diversity", expected=False)

# Test Case 2: Rapid engagement, high influence
comments = [
    {'timestamp': post_time + i * 2, 'user_id': f'user{i}', 'user_karma': 5000, 'parent_id': 'post_id'}
    for i in range(30)
]
simulate_test(post_time, comments, "Rapid engagement, high influence", expected=True)

# Test Case 3: Slow, broad participation
comments = [
    {'timestamp': post_time + i * 180, 'user_id': f'user{i}', 'user_karma': 20, 'parent_id': 'post_id'}
    for i in range(30)
]
simulate_test(post_time, comments, "Slow but broad participation", expected=False)
