'''
Created on Apr 20, 2009

@author: xzhou

This is a class 
'''

import PoterStemAlg;

class WordProcess(object):
    '''
    classdocs
    '''
    

    def __init__(selfparams):
        '''
        Constructor
        '''
    
    def filterAndStem(self, words = []):
        aPoterStemAlg = PorterStemmer()
        stemmedWords = []
        exclude = set(string.punctuation)
        if(words):
            words = " ".join(words);
            words = ''.join(ch for ch in words if ch not in exclude)
            words = words.split()
            words = [word.lower() for word in words if len(word) > 3]
            for word in words:
                if(word):
                    word = aPoterStemAlg.stem(word, 0, len(word)-1 )
                    stemmedWords.append(word)
            
            return stemmedWords
        else:
            return []
            
            
        
        