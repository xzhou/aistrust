'''
Created on Apr 29, 2009

@author: xzhou
'''
from APage import WebPage
from 


class AisTrainning(object):
    '''
    AisTrainning read web pages one by one and train the Ais system
    '''
    def Train(self, aWebPage, repertoire):
        #sample n words in webpage
        if(type(aWebPage) == WebPage):
            if(aWebPage.pageType == "positive"):
                pass
            elif(aWebPage.pageType == "negative"):
                pass
            
            return repertoire
        else:
            pass