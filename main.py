#!/usr/bin/python3

import sys
from stats import count_words
from stats import count_char_frequency
from stats import sort_frequencies

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def report_frequencies(file_path):
    book_content = get_book_text(file_path)
    num_words = count_words(book_content)
    char_count_dict = count_char_frequency(book_content)
    char_count_list = sort_frequencies(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count_list = list(filter(lambda x: x["char"].isalpha(), char_count_list))
    for freq in char_count_list:
        print(f"{freq['char']}: {freq['num']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    report_frequencies(file_path)

main()
