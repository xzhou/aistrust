'''
Created on Apr 29, 2009

@author: xzhou
'''
from APage import WebPage
from Config import AisConfig
import random
from Repertoire import Repertoire


class AisTrainning(object):
    '''
    AisTrainning read web pages one by one and train the Ais system
    '''
    def TrainOnePage(self, aWebPage, repertoire):
        #sample n words in webpage
        if(type(aWebPage) == WebPage):  #
            
            if(aWebPage.pageType == "trusted"):
                #sample n words
                if(len(aWebPage.words) >= AisConfig.nSample):
                    i = 0;
                    while(i < AisConfig.nSample):
                        index = random.randint(0, len(webPages.words))
                        if(not repertoire.existFeature(webPages.words[index])):
                           repertoire.addPositive(webPages.words[index])
                           i = i + 1
                
            elif(aWebPage.pageType == "malicious"):
                if(len(aWebPage.words) >= AisConfig.nSample):
                    i = 0
                    while(i < AisConfig.nSample):
                        index = random.randint(0, len(webPage.words))
                        if(not repertoire.existFeature(webPages.words[index])):
                           repertoire.addNegative(webPages.words[index])
                           i = i + 1
    
    def Train(self):
        #scan a directory for all the webpages
        pass
        