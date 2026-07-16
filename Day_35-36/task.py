def find_duplicates(list_of_num: list):
    seen = []
    duplicates = []
    for item in list_of_num:
        if item in seen:
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates

one = [ 11,11,22,22,33,44,55]
print(find_duplicates(one))