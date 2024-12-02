def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)

    chars_dict = get_chars_dict(text)

    generate_book_report(book_path, num_words, chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}

    for c in text:
        lowered = c.lower()

        if lowered.isalpha() is False:
            continue

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def sort_on(key):
    return key["num"]


def chars_to_sorted_list(num_chars_dict):
    sorted_list = []
    for item in num_chars_dict:
        sorted_list.append({"char": item, "num": num_chars_dict[item]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def generate_book_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    sorted_list = chars_to_sorted_list(chars_dict)

    for item in sorted_list:
        if not item["char"].isalpha():
            continue

        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


main()
