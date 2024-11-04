n = int(input())
scores = list(map(int, input().split()))

unique_scores = set(scores)

sorted_unique_scores = sorted(unique_scores, reverse=True)

runner_up_score = sorted_unique_scores[1]

print(runner_up_score)
