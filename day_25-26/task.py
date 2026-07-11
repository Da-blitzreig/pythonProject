def reversal(list_of_names: list):
    result = []
    index = len(list_of_names) - 1
    while index >= 0:
        result.append(list_of_names[index])
        index -= 1
    return result

names = ["Bosco", "Jayden", "Steven", "Vincent"]
print(reversal(names))