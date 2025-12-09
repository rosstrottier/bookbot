def count_words(book):
    count = book.split()
    return len(count)

def count_char_occurance(book) -> list[dict]:
    occurances = {}
    chars = list(book)

    for char in chars:
        char = char.lower()
        count = occurances.get(char, 0)
        count = count + 1
        occurances[char] = count
    
    return format_char_occurances(occurances)

def format_char_occurances(occurances) -> list[dict]:
    list_of_occurances = [
        {"char": k, "num": v}
        for k,v in occurances.items()
    ]
    
    output = remove_bad_chars(list_of_occurances)
    output.sort(reverse=True, key=lambda occurance: occurance["num"])

    return output

def remove_bad_chars(occurances: list[dict]) -> list[dict]:
    output = []

    for occurance in occurances:
        occurance_char: str = occurance["char"]
        if occurance_char.isalpha():
            output.append(occurance)
    
    return output