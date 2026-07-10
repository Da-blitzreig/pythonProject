def even_or_odd(numbers):
    result = {}
    for num in numbers:
        if num % 2 == 0:
            result[num] = "even"
        else:
            result[num] = "odd"
    return result
nums = [2, 3, 56]
d = even_or_odd(nums)
print(d)