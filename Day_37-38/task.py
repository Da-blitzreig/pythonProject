def frequency_of_words(sentence):
    n = sentence.split()
    frequency = {}
    for words in n:
        if words in frequency:
            frequency[words] += 1
        else:
            frequency[words] = 1
    return frequency

nt = "hi, I am Steve, I like Spoke,"

print(frequency_of_words(nt))