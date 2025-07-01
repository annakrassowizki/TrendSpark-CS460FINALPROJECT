# main.py
import datetime
from trendspark import compute_trendspark_score, generate_mock_data

if __name__ == "__main__":
    # Generate mock Reddit-style post engagement
    post_time, early_comments = generate_mock_data()

    # Compute TrendSpark virality score
    results = compute_trendspark_score(post_time, early_comments, weights=(0.5, 0.2, 0.3), threshold=0.6)

    print("\n=== TrendSpark Analysis ===")
    for key, value in results.items():
        print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")