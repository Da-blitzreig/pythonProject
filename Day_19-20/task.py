def add_lists(first_list, second_list):
    index = []
    for i in range(len(first_list)):
        index.append(first_list[i] + second_list[i])
    return index
def multiply_lists(first_list, second_list):
    index = []
    for i in range(len(first_list)):
        index.append(first_list[i] * second_list[i])
    return index

list1 = [1, 2, 3, 5, 7]
list2 = [3, 5, 7, 1, 2]
print(add_lists(list1, list2))
print(multiply_lists(list1, list2))