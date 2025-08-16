from stats import num_words
from stats import num_chars

def get_book_text(book):
        with open(book) as f:
            file_contents = f.read()
        return file_contents     

def main():
    book = "/home/test/bootdev_projects/bookbot/books/frankenstein.txt"
    text = (get_book_text(book))
    num_words(text)
    num_chars(text)

main()