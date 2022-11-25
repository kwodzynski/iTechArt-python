class TextParsing:
    def __init__(self):
        pass

    # Read, split and strip text from the file
    def read_text_file(txt_path):
        with open(txt_path, 'r', encoding='UTF-8') as f:
            text = f.read()
            words = text.split(' ')
            striped_words = map(lambda x: x.rstrip(',.():'), words)
            sentences = text.split('.')

            # Methods for returning preparing lists
            return TextParsing.return_all_lists(striped_words, words, sentences)


    # Methods for returning concatenated lists of words and sentences
    def return_all_lists(striped_list, words, sentences):
        return TextParsing.return_all_sentences(sentences) + TextParsing.create_dict_number_of_words(striped_list, words)


    # Method for returnig list of word occurences
    def create_dict_number_of_words(striped_list, words):
        dict_list = []
        counter = {}
        dict_list.append(f'The text contains {len(words)} words and their occurences:')
        for word in striped_list:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
        for key, value in counter.items():
            dict_list.append(f'{key}: {value}') 
        return dict_list     
   


    # Method for returning enumerated sentences
    def return_all_sentences(sentences_list):
        list_of_sentences = []
        list_of_sentences.append('The text contains the following sentences:')
        for ind, sentence in enumerate(sentences_list, 1):
            if(len(sentence)):
                processes_sentence = sentence.lstrip('\n ')
                list_of_sentences.append(f"{ind}. {processes_sentence}")
        return list_of_sentences