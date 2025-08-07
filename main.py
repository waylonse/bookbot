from stats import *
import sys


def get_book_text(file):
    with open(file) as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    message = get_book_text(book)
    count = get_num_words(message)
    letter_count = count_letters(message)
    sorted_count = sorted(letter_count.items(), key=lambda item: item[1], reverse =True) # Sorts by the second element of each tuple (the value)
    sorted_dict_by_value = dict(sorted_count)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}
    ----------- Word Count ----------
    Found {count} total words
    --------- Character Count -------""")
    for item in sorted_dict_by_value:
        print(f"{item}: {sorted_dict_by_value[item]}")
    print("============= END ===============")

main()