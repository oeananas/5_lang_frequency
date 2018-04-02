import collections
import re
import sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read().lower()
        return content


def get_most_frequent_words(text):
    all_words_in_text = collections.Counter(re.findall(r'\w+', text))
    most_frequent_ten_words = all_words_in_text.most_common(10)
    return most_frequent_ten_words


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit("Need input file path as parameter")
    try:
        most_frequent_words_lst = get_most_frequent_words(load_data(sys.argv[1]))
        for words_and_counts in most_frequent_words_lst:
            print(words_and_counts[0], ": ", words_and_counts[1], sep='')
    except FileNotFoundError:
        exit("File not found")
