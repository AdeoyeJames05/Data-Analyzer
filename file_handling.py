file = 'my_folder/Example2.txt'

with open(file, 'r') as test_write_file:
    test_content = test_write_file.read()

class TextAnalyzer:
    def __init__(self, text):
        text_format = text.replace(',', '').replace('.','').replace('?','').replace('!','')

        text_format = text_format.lower()

        self.fmt_text = text_format


    def freq_all(self):
        list_words = self.fmt_text.split(" ")

        freq_dict ={ }
        for word in list_words:
            freq_dict[word] = list_words.count(word)

        return freq_dict


    def freq_of(self, word):
        freq_map = self.freq_all()

        if word in freq_map:
            return freq_map[word]
        else:
            return None


analyze_file = TextAnalyzer(test_content)
display = analyze_file.fmt_text
print(display)
user_input = str(input("Enter the word you would like to search for in your data: "))
display_specific_word = analyze_file.freq_of(user_input)
print(f"The word {user_input} appears {display_specific_word} times")