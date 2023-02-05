

def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def get_num_chars(text):

    dict = {}
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in text:
        lwr_char = i.lower()
        if lwr_char in letters:
            if lwr_char in dict:
                dict[lwr_char] += 1
            else:
                dict[lwr_char] = 1
    return dict


path_to_file = "./books/frankenstein.txt"
with open(path_to_file) as f:
    file_contents = f.read()
    print(get_num_words(file_contents))
    print(get_num_chars(file_contents))
    





