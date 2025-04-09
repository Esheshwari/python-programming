def word_count_with_frequency(sentence):
    words = sentence.split()
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return len(words), word_freq

sentence = input("Enter a sentence: ")
count, frequency = word_count_with_frequency(sentence)
print(f"Total word count: {count}")
print("Word frequencies:", frequency)
