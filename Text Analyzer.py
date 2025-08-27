given_string=("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore?"
              " et diam magna. et diam amet.")


class TextAnalyzer:
    def __init__(self, text):
        formated_text = text.replace(",", "").replace("!", "").replace("?", "").replace(".", "")

        formated_text = formated_text.lower()

        self.fmtText = formated_text

    def freq_all(self):
        wordList = self.fmtText.split(" ")

        freqMap = {}
        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap


    def freq_of(self, word):
        freqDict = self.freq_all()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0


analyzed = TextAnalyzer(given_string)
display = analyzed.fmtText
print(display)
count = analyzed.freq_all()
print(count)
user_input = str(input("Enter the word you would like to search for in your data: "))
display_specific_word = analyzed.freq_of(user_input)
print(f"The word {user_input} appears {display_specific_word} time")