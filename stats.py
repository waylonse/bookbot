def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    count = {}
    for char in text:
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    return count