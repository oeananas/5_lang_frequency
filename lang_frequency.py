import collections
import re
import sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        return content


def get_most_frequent_words(text):
    return collections.Counter(re.findall(r'\w+', text.lower()))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('Need input file path as parameter')
    try:
        top_words = get_most_frequent_words(load_data(sys.argv[1]))
        num_of_words = 10
        print('The most common words in the text:')
        for word, count in top_words.most_common(num_of_words):
            print(word, count)

    except FileNotFoundError:
        exit('File not found')
