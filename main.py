def get_book_text(book):
        with open(book) as f:
            file_contents = f.read()
        return file_contents

def main():
    book = "/home/test/bootdev_projects/bookbot/books/frankenstein.txt"
    print(get_book_text(book))

main()