from stats import num_words
from stats import num_chars
from stats import split_dicts


def get_book_text(book):
        with open(book) as f:
            file_contents = f.read()
        return file_contents     

def main():
    book = "books/frankenstein.txt"
    text = (get_book_text(book))
    word_count = num_words(text)
    dic = num_chars(text)
    input = split_dicts(dic)
    #output = 

    print(f"""============ BOOKBOT ============")
"Analyzing book found at {book}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    
    for dicts in input:
        num = None
        letter = None
        for alphanum in dicts:
            stat = dicts[alphanum]
            if alphanum == "num":
                num = stat
            else:
                letter = stat
        print(f"{letter}: {num}")
        
    print("============= END ===============")


main()