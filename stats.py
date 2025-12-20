# Bookbot project stats.py


def word_count(book_contents):
    words = book_contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def char_count(book_contents):
    count = {}
    characters = book_contents.lower()

    for char in characters:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def sorting_hat(lst_of_dicts):
    return lst_of_dicts["num"]


def character_dict(count):
    lst_of_dicts = []
    for char, num in count.items():
        lst_of_dicts.append({"char": char, "num": num})
        lst_of_dicts.sort(reverse=True, key=sorting_hat)
    return lst_of_dicts
