import sys

from stats import count_words
from stats import count_char_occurance

def get_book_text(path):
    with open(path) as f:
        output = f.read()
    return output

def print_introduction(book_filepath: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at /{book_filepath}...")

def print_wordcount(book: str):
    num_words = count_words(book)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def print_character_count(book: str):
    char_occurances = count_char_occurance(book)
    for occurance in char_occurances:
        print(f"{occurance["char"]}: {occurance["num"]}")

def analyze_book(book_filepath: str):
    book = get_book_text(f"./{book_filepath}")

    print_introduction(book_filepath)
    print_wordcount(book)
    print_character_count(book)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_filepath = sys.argv[1]
    analyze_book(book_filepath)

main()
