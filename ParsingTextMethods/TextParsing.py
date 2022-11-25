import os

class TextParsing:
    def __init__(self):
        pass

    # Methods for printing all of words, number of words and the numbers of occurences of each word
    def print_all_words(cls, striped_list, words):
        print(f'The text contains the following words ({len(words)}):')
        TextParsing.number_of_words( striped_list, counter = {})


    @classmethod
    def number_of_words(cls, striped_list, counter):
        TextParsing.print_words_and_create_dict(striped_list, counter)
        print('\n\nThe text contains the following numbers of words:') 
        for key, value in counter.items():
            print(f'{key}: {value}')

    
    def print_words_and_create_dict(striped_list, counter):
        for word in striped_list:
            print(word, end=', ')
            TextParsing.create_dict_number_of_words(word, counter)


    def create_dict_number_of_words(word, counter):
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1


    # Method for printing enumerated sentences
    @staticmethod
    def print_all_sentences(sentences_list):
        print(f'\n\nThe text contains the following sentences:')
        for ind, sentence in enumerate(sentences_list, 1):
            if(len(sentence)):
                print(ind, sentence.lstrip('\n '))     


path_to_txt = f'{os.getcwd()}/Resources/text_to_parsing.txt'
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


read_text_file(path_to_txt)                     