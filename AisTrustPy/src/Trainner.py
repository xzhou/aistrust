'''
Created on Apr 29, 2009

@author: xzhou
'''
from APage import WebPage


class AisTrainning(object):
    '''
    AisTrainning read web pages one by one and train the Ais system
    '''
    def Train(self, aWebPage, repertoire):
        #sample n words in webpage
        if(type(aWebPage) == type(WebPage)):
            pass
        if(aWebPage.pageType == "positive"):
            pass
        else:
            pass
            
        return repertoire