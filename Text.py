import re

class TextIO():
    '''gets the texts'''
    def getInput(self):
        i = 1
        texts = []
        text = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        while text:
            texts.append(text)
            i += 1
            text = input("Digite o texto " + str(i) +" (aperte enter para sair):")

        return texts

    def extractSentence(self, text):
        coma = text.count(",")
        ''' split the text into sentences'''
        sentences = re.split(r'[.!?]+', text)
        if sentences[-1] == '':
            del sentences[-1]
        return [sentences,coma]


    def extractPhrases(self, sentence):
        ''' split the sentences into phrases'''
        return re.split(r'[,:;]+', sentence)

    def extractWords(self, frase):
        '''split the phrase into words'''
        return frase.split()

    def getAllWords(self, phrases):
        wl = []
        for phrase in phrases:
            wl = wl + self.extractWords(phrase)
        return wl

    def getAllPhrases(self, sentences):
        all_phrases = []
        i = 0
        for sentence in sentences:
            all_phrases = all_phrases + self.extractPhrases(sentence)
        return all_phrases

