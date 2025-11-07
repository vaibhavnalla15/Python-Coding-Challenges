""" Create a Python program that counts how many times each word appears in a given sentence. """

sentence = "cloud, cloud, cloud, engineer, engineer, aws"
words = sentence.lower().replace(",", "").split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(f"{key}: {value}")

