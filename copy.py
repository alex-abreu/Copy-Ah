import re
from Arith import *
from Text import *

class Copyah():
    def __init__(self):
        self.io  = TextIO()
        self.art = Arithmetics()
    
    def config(self):
        '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
        print("Bem-vindo ao detector automático de COH-PIAH.")

        self.wal = float(input("Entre o tamanho medio de palavra:"))
        self.ttr = float(input("Entre a relação Type-Token:"))
        self.hlr = float(input("Entre a Razão Hapax Legomana:"))
        self.sal = float(input("Entre o tamanho médio de sentença:"))
        self.sac = float(input("Entre a complexidade média da sentença:"))
        self.pal = float(input("Entre o tamanho medio de frase:"))

        self.sigBase = [self.wal, self.ttr, self.hlr, self.sal, self.sac, self.pal]
    def start(self):
        
        self.config()
        texts = self.io.getInput()

        print("mostlikely a copy")
        print(self.checkCopy(texts, self.sigBase))


    def compareSignature(self, sig_A, sig_B):
        '''returns the degree of similarity between two signatures'''
        diffAB = 0
        for (vA, vB) in zip(sig_A, sig_B):
            diffAB = diffAB + abs(vA - vB)
        return diffAB/6

    def caculateSignature(self, text):
        '''calculates the signature of the given text'''
        self.sentences,self.coma = self.io.extractSentence(text)
        self.phrases             = self.io.getAllPhrases(self.sentences)
        self.wl                  = self.io.getAllWords(self.phrases)

        wal = self.art.avgCharWord(self.wl)
        ttr = self.art.typeToken(self.wl)
        hlr = self.art.hapax(self.wl)
        sal = self.art.avgCharPerSentence(self.wl,self.sentences, self.coma)
        sac = self.art.avgPhrasesPerSentence(self.phrases, self.sentences)
        pal = self.art.avgWordsPerPhrase(self.wl, self.phrases)

        return[wal, ttr, hlr, sal, sac, pal]

    def checkCopy(self, texts, signature):
        '''returns the index of the text with the highest probability of beeing a copy'''
        signatures  = []

        for text in texts:
            signatures.append(self.caculateSignature(text))

        for sig in signatures:
            print(sig)
        index = 0
        minSignature = self.compareSignature(signature, signatures[0])
        for i in range(1,len(signatures)):
            tempSig = self.compareSignature(signature, signatures[i])
            if tempSig < minSignature:
                minSignature = tempSig
                index = i
        print(f'the infected text is #{i} ')
        return minSignature 


if __name__ == '__main__':
    cp = Copyah()
    cp.start()
