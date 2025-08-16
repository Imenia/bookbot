def num_words(text):
    count = len(text.split())
    print(f"{count} words found in the document")

def num_chars(text):
    same_case = text.lower()
    char_dict = {}
    for char in same_case:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    print(char_dict)