# Bookbot project main.py

from stats import word_count
from stats import char_count
from stats import sorting_hat
from stats import character_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    word_count(text)
    count = char_count(text)
    sorted_list = character_dict(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    word_count(text)
    print("--------- Character Count -------")

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
