import collections
import re
import sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        return content


def get_most_frequent_words(text, num_of_words=10):
    count_words = collections.Counter(re.findall(r'\w+', text.lower()))
    return dict(count_words.most_common(num_of_words))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('Need input file path as parameter')
    try:
        most_frequent_words = get_most_frequent_words(load_data(sys.argv[1]))
    except FileNotFoundError:
        exit('File not found')
    print('The most common words in the text:')
    for word, count in most_frequent_words.items():
        print(word, ':', count)
