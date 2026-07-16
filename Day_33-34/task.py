def average(list_of_num: list):
    index = 0
    results = 0
    while index < len(list_of_num):
        results += list_of_num[index]
        index += 1
    return results / len(list_of_num)

code = [1, 2, 3]
print(average(code))