def runner_up(scores):
    scores = list(set(scores))
    results = []

    while len(scores) > 1:
        largest = scores[0]
        for num in scores:
            if num > largest:
                largest = num
        scores.remove(largest)
        results.append(largest)

    return results

score = [2, 3, 6, 7, 5]
print(runner_up(score))