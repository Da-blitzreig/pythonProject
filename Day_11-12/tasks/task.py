def check_weird(n):
    if n % 2 == 1:
        return "Weird"
    else:
        if 2 <= n <= 5:
            return "Not Weird"
        elif 6 <= n <= 20:
            return "Weird"
        elif n > 20:
            return "Not Weird"


numbers = [3, 4, 7, 8, 20, 21, 28, 78]

for n in numbers:
    print(check_weird(n))