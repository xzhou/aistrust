'''
Created on May 3, 2009

@author: xzhou
'''

import os
import sys
import DocSeperator
from Config import AisConfig
import math
import random

class Slot:
    def __init__(self, feature):
        self.feature = feature
        self.bind = None

class PageAPC:
    '''
    class PageAPC is the Atigen Presenting Cell of a Page
    '''
    def __init__(self, features):
        self.slots = []
        self.features = []
        self.addFeatures(features)
    
    #this is a private method
    def __addFeature(self, feature=""):
        #generate slots for the feature
        for i in range(0, AisConfig.nSlots):
            self.slots.append(Slot(feature))
    def addFeatures(self, features=[]):
        for feature in features:
            self.__addFeature(feature)
        random.shuffle(self.slots)
        
    def getFeatures(self):
        return self.features
            
class ICRMSystem:
    '''
    class TestPhase is the testing phase of the AIS system
    '''
    
    def __init__(self):
        pass
    
    def processAPage(self, aPage):
        sampleFeatures = []
        if len(aPage.words) >= AisConfig.nSample:
            i = 0
            while i < AisConfig.nSample:
                index = random.randint(0, len(aPage.words)-1)
                sampleFeatures.append(aPage.words[index])
                i = i + 1
            pageAPC = PageAPC(sampleFeatures)
            return pageAPC
        else:
            return None
    
    def preprocess(self, pageFileName):
        '''
        will decompse a web page into words and remove the common words and 
        stem the words
        '''
        aPage = readNormalHtml(pageFileName)
        return processAPage(aPage)

    def init(self, aPageAPC, repertoire, type="test"):
        features = aPageAPC.getFeatures();
        for feature in features:
            if not repertoire.existFeature(feature):
                if type == "trusted":
                    #generate E and R cells
                    repertoire.addTrustedFeature(feature)
                elif type == "malicious":
                    repertoire.addMaliciousWord(feature)
                elif type == "test":
                    repertoire.addTest(feature)
        return aPageAPC
    
    def bind(self, aPageAPC, repertoire):
        for slot in aPageAPC.slots:
            #get all cells of this feature and randomly select one
            cells = [cell for cell in repertoire.Cells if cell.feature == slot.feature]
            index = random.randint(0, len(cells)-1)
            slot.bind = cells[index]
        return aPageAPC
    
    def proliferation(self, aPageAPC, repertoire):
        '''
        this is the proliferation pahse of T, E cell with antigen
        '''
        interactionResult = []
        for i in range(0, len(aPageAPC.slots)):
            f1 = aPageAPC.slots[i]
            f2 = aPageAPC.slots[i+1]
            
            if f1.bind == None:
                if f2.bind == None:
                    pass
                elif f2.bind.type == "E":
                    interactionResult.append(f2.bind)
                    interactionresult.append(f2.bind)
                    repertoire.addACell(f2.bind.feature, f2.bind.type)
                elif f2.bind.type == "R":
                    interactionResult.append(f2.bind)
            elif f1.bind.type == "E":
                if f2.bind == None:    
                    interactionResult.append(f1.bind)
                    interactionResult.append(f1.bind)
                    repertoire.addACell(f1.bind.feature, f1.bind.type)
                elif f2.bind.type == "E":
                    #generate 4 E
                    interactionResult.append(f1.bind)
                    interactionResult.append(f1.bind)
                    interactionResult.append(f2.bind)
                    interactionResutl.append(f2.bind)  
                    repertoire.addACell(f1.bind.feature, f1.bind.type)
                    repertoire.addACell(f2.bind.feature, f2.bind.type)
                elif f2.bind.type == "R":
                    interactionResult.append(f1.bind)
                    interactionResult.append(f2.bind)
                    interactionResult.append(f2.bind)
                    repertoire.addACell(f2.bind.feature, f2.bind.type)
            elif f1.bind.type == "R":
                if f2.bind == None:
                    interactionResult.append(f1.bind)
                elif f2.bind.type == "E":
                    interactionResult.append(f1.bind)
                    interactionResutl.append(f1.bind)
                    repertoire.addACell(f1.bind.feature, f1.bind.type)
                    interactionResutl.append(f2.bind)
                elif f2.bind.type == "R":
                    interactionResult.append(f1.bind)
                    interactionResult.append(f2.bind)  
        return interactionResult  
 
    def decisionPhase(self, interactionResult):
        '''
        decision phase count the E cells and R cells that a page bind to  and 
        return the score for this page, a score > 0 means trusted
        '''
        pageScore = 0
        features = []
        for cell in interactionResult:
            if cell.feature not in features:
                features.append(cell.feature)
        
        for feature in features:
            Ef = 0
            Rf = 0
            for cell in interactionResult:
                if cell.feature == feature:
                    if(cell.type == "E"):
                        Ef = Ef + 1
                    if(cell.type == "R"):
                        Rf = Rf + 1
            scoref = (Rf - Ef)/math.sqrt(Rf*Rf + Ef*Ef)
            pageScore = pageScore + scoref
        
        return pageScore
                    
    def test(self, fileName, repertoire):
        aPageAPC = self.preprocess(fileName)
        self.init(aPageAPC, repertoire, "test")
        self.bind(aPageAPC, repertoire)
        interactionResult = self.proliferation(aPageAPC, repertoire)
        return self.decisionPhase(interactionResult)
    
    def train(self, aPage, repertoire):
        aPageAPC = self.processAPage(aPage)
        self.init(aPageAPC, repertoire, "test")
        self.bind(aPageAPC, repertoire)
        self.proliferation(aPageAPC, repertoire)
        return repertoire
      
    