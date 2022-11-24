import os
import sys

sys.path.insert(0, f'{os.getcwd()}')
from ParsingTextMethods.TextParsing import *

tp = TextParsing()

# Read, split and strip text from the file
def read_text_file(path):
    with open(path, 'r', encoding='UTF-8') as f:
        text = f.read()
        words = text.split(' ')
        striped_words = map(lambda x: x.rstrip(',.():'), words)
        sentences = text.split('.')

        # Call method for parsing words
        tp.print_all_words(striped_words, words)

        # Call method to parsing sentences
        tp.print_all_sentences(sentences)


# Path to file with text to be parsed
read_text_file(
    f'{os.getcwd()}/Resources/text_to_parsing.txt')
