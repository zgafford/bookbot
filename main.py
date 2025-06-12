def get_book_text(path):
    with open(path) as book:
        return book.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


main()