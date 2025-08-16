def num_words(text):
    count = len(text.split())
    return count
    print(f"""---------- Word Count ----------
Found {count} total words""")

def num_chars(text):
    same_case = text.lower()
    char_dict = {}
    for char in same_case:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_key(items):
    return items["num"]

def split_dicts(input):
    dicts = []
    for letter in input:
        num = input[letter]
        if letter.isalpha():
            if letter not in dicts:
                dicts.append({"char":letter, "num":num})
    dicts.sort(reverse=True, key=sort_key)
    return dicts
