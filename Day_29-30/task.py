def runner_up(scores):
    scores = list(set(scores))
    scores.sort()
    results = []
    index = len(scores) - 2
    while index >= 0:
        results.append(scores[index])
        index -= 1
    return results

score = [2, 3, 6, 7, 5]
print(runner_up(score))