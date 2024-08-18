def main(path):
    with open(path) as f:
        file_contents = f.read()
        
        word_count = get_number_of_words(file_contents)

        char_counts = count_chars(file_contents)
        
        alpha_char_counts = make_alpha_list(char_counts)
        alpha_char_counts.sort(reverse=True, key=sort_on)

        print(f"--- Begin report of {path} ---")
        print(f"{word_count} words found in the document")
        for i in alpha_char_counts:
            print(f"The {i["letter"]} character was found {i["count"]} times")
        print("--- End report ---")


def get_number_of_words(text):
    words = text.split()
    n_words = len(words)
    
    return(n_words)


def count_chars(text):
    text = text.lower()
    char_counts = {}

    for i in list(text):
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1

    return char_counts


def make_alpha_list(dict):
    d = [{"letter": i, "count": dict[i]} for i in dict if i.isalpha()]

    return d


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]


main("books/frankenstein.txt")
