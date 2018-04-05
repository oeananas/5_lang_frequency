import collections
import re
import sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        return content


def get_most_frequent_words(text, num_of_words=10):
    return collections.Counter(re.findall(r'\w+', text.lower())).most_common(num_of_words)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('Need input file path as parameter')
    try:
        top_ten_words = get_most_frequent_words(load_data(sys.argv[1]))
        print('The most common words in the text:')
        for element in top_ten_words:
            word = element[0]
            count = element[1]
            print(word, count)

    except FileNotFoundError:
        exit('File not found')
