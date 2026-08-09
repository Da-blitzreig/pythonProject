characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#%$^*&"

password = ""

for i in range(12):
    password += characters[(id(password) + i) % len(characters)]

print("Your password is:", password)