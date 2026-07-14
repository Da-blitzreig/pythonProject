def runner_up(scores):
    scores = list(set(scores))
    scores.sort()
    result = []
    index = len(scores) - 2
    while index >= 0:
        result.append(scores[index])
        index -= 1
    return result

score = [2, 3, 6, 7, 5]
print(runner_up(score))