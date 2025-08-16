def get_book_text(book):
        with open(book) as f:
            file_contents = f.read()
        return file_contents     

def main():
    book = "/home/test/bootdev_projects/bookbot/books/frankenstein.txt"
    text = (get_book_text(book))
    num_words(text)
    
def num_words(text):
    count = len(text.split())
    print(f"{count} words found in the document")
    

main()