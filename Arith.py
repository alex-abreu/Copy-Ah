from Text import *
class Arithmetics():
    def __init__(self):
        self.io  = TextIO()

    def countSingleAppearance(self, wl):
        '''counts the amount of words that appear a single time only'''
        freq = dict()
        for word in wl:
            word_lower = word.lower()
            if word_lower in freq:
                if freq[word_lower] == 1:
                    freq[word_lower] += 1
            else:
                freq[word_lower] = 1
        val_list = list(freq.values())
        return val_list.count(1)

    def countUniqueWordsUsed(self, wl):
        '''counts the amount unique words used'''
        wSet = set()
        for word in wl:
            wSet.add(word.lower())
        return len(wSet)

    def avgCharWord(self, wl):
        '''average of characteres per words'''
        char = 0
        for word in wl:
            char = char + len(word)
        return char/len(wl)

    def typeToken(self, wl):
        '''number of different words divided by the total of words used'''
        unique = self.countUniqueWordsUsed(wl)
        return unique/len(wl)

    def hapax(self, wl):
        '''number of single appearances divided by the total of words used'''
        justOnce = self.countSingleAppearance(wl)
        return justOnce/len(wl)

    def avgCharPerSentence(self, wl, sentences,coma):
        '''average of words per sentence'''
        char = 0
        for word in wl:
            char = char + len(word)
        return (char+len(wl)-1+coma)/len(sentences)

    def avgPhrasesPerSentence(self, phrases, sentences):
        '''average of phrases per sentence'''
        return len(phrases)/len(sentences)

    def avgWordsPerPhrase(self, wl, phrases):
        '''average of words per phrase'''
        char = 0
        for word in wl:
            char = char + len(word)
        return (char+len(wl)-1)/len(phrases)