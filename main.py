def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
def get_text(example_string):
    words = example_string.split()
    num_words = len(words)
    return len(num_words)
