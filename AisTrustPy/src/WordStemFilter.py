'''
Created on Apr 20, 2009

@author: xzhou

This is a class 
'''

from PoterStemAlg import PorterStemmer
import re
import string

class WordProcess(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.commonWords = []
        f = open("commonWords.txt", 'r')
        for line in f:
            words = line.split()
            for word in words:
                self.commonWords.append(word)
 
    def filterAndStem(self, words = []):
        aPoterStemAlg = PorterStemmer()
        stemmedWords = []
        exclude = set(string.punctuation)
        if(words):
            words = " ".join(words);
            words = ''.join(ch for ch in words if ch not in exclude)
            words = words.split()
            words = [word.lower() for word in words if len(word) > 3 and len(word) < 20]
            for word in words:
                if word:
                    f = word not in self.commonWords
                    f = word.isalpha() and f
                    f = word.find("www") == -1 and f
                    if f:
                        word = aPoterStemAlg.stem(word, 0, len(word)-1 )
                        stemmedWords.append(word)
            return stemmedWords        
        else:
            return []