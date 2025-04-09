def word_count(sentence):
    words=sentence.split()
    return len(words)
sentence=input("Enter a sentence:")
print(f"{word_count(sentence)}")
