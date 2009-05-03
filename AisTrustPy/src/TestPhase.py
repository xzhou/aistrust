'''
Created on May 3, 2009

@author: xzhou
'''

import os
import sys
import DocSeperator
from Config import AisConfig

class PageAPC:
    '''
    class PageAPC is the Atigen Presenting Cell of a Page
    '''
    def __init__(self, features):
        self.addFeatures(features)
    
    def addFeature(self, feature):
        slots = []
        for i in range(0, AisConfig.nSlot):
            slots.append(feature)
        
        self.featureArray.append(slots)
    
    def addFeatures(self, features):
        for feature in features:
            for i in range(0, AisConfig.nSlot):
                slot.append(feature)
            self.featureArray.append(slot)

class TestPhase:
    '''
    class TestPhase is the testing phase of the AIS system
    '''
    
    def __init__(self):
        pass
    
    def preprocess(self, pageFileName):
        '''
        will decompse a web page into words and remove the common words and 
        stem the words
        '''
        aPage = readNormalHtml(pageFileName)
        sampleFeatures = []
        if len(aPage.words) >= AisConfig.nSample:
            i = 0
            while i < AisConfig.nSample:
                index = random.randint(0, len(aPage.words)-1)
                sampleFeatures.append(aPage.words[index])
        
            pageAPC = PageAPC(sampleFeatures)
            return pageAPC
        else:
            return None
        
    def interactionPhase(self, aPageAPC, repertoire):
        pass
        
    def decisionPhase(self, interactionResult):
        pass
        
        
        
    