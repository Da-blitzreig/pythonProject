def runner_up(scores):
    scores = list(set(scores))
    scores.sort()
    return scores[-2]

score = [2, 3, 6, 7, 5]
print(runner_up(score))