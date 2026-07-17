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
nit = "in world war 2 more than 1 million people died and more than 1 million people got injured in world war 2"
nity = "Lie, Lie, Lie, Fe, Fe, Ki"
print(frequency_of_words(nt))
print(frequency_of_words(nit))
print(frequency_of_words(nity))
