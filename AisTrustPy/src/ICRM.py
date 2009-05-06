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
        self.__addFeatures(features)
    
    #this is a private method
    def __addFeature(self, feature=""):
        #generate slots for the feature
        for i in range(0, AisConfig.nSlot):
            self.slots.append(Slot(feature))
    def __addFeatures(self, features=[]):
        for feature in features:
            self.__addFeature(feature)
            self.features.append(feature)
        random.shuffle(self.slots)
        
    def getFeatures(self):
        return self.features
        
class ICRMSystem:
    '''
    class TestPhase is the testing phase of the AIS system
    '''
    
    def __init__(self):
        pass
    
    def page2APC(self, aPage):
        sampleFeatures = []
        if len(aPage.words) >= AisConfig.nSample:
            i = 0
            while i < AisConfig.nSample:
                index = random.randint(0, len(aPage.words)-1)
                sampleFeatures.append(aPage.words[index])
                i = i + 1
            pageAPC = PageAPC(sampleFeatures)
            '''
            for slot in pageAPC.slots:
                print slot.feature
            '''
            return pageAPC
        else: #get all words
            nWords = len(aPage.words)
            for i in range(0, nWords):
                sampleFeatures = aPage.words[i]
            
            pageAPC = PageAPC(sampleFeatures)
            return pageAPC
    def preprocess(self, pageFileName):
        '''
        will decompse a web page into words and remove the common words and 
        stem the words
        '''
        aPage = readNormalHtml(pageFileName)
        return processAPage(aPage)

    def init(self, aPageAPC, repertoire, type="test"):
        print "init ",
        if aPageAPC == None:
            return None
        features = aPageAPC.getFeatures();
        for feature in features:
            if not repertoire.existFeature(feature):
                #print feature
                if type == "trusted":
                    #generate E and R cells
                    repertoire.addTrustWord(feature)
                elif type == "malicious":
                    repertoire.addMaliciousWord(feature)
                elif type == "test":
                    #repertoire.addTest(feature)
                    pass
        return aPageAPC
    
    def bind(self, aPageAPC, repertoire):
        print "rep size = ", len(repertoire.Cells), 
        print "bind to ", len(aPageAPC.slots), "slots",
        features = aPageAPC.getFeatures()
        for feature in features:
            #get all cells of this feature and randomly select one
            cells = [cell for cell in repertoire.Cells if cell.feature == feature]
            slots = [slot for slot in aPageAPC.slots if slot.feature == feature]
            random.shuffle(cells)
            if len(cells) > len(slots):
                for i in range(0, len(slots)):
                    slots[i].bind = cells[i]                
            else:
                for i in range(0, len(cells)):
                    slots[i].bind = cells[i]
                i = len(cells)
                for j in range(i+1, len(slots)):
                    slots[j].bind = None 
        print "complete ",
        return aPageAPC
    
    def proliferation(self, aPageAPC, repertoire):
        '''
        this is the proliferation pahse of T, E cell with antigen
        '''
        print "proliferation"
        interactionResult = []
        for i in range(0, len(aPageAPC.slots)-1):
            f1 = aPageAPC.slots[i]
            f2 = aPageAPC.slots[i+1]
            
            if f1.bind == None:
                if f2.bind == None:
                    pass
                elif f2.bind.type == "E":
                    interactionResult.append(f2.bind)
                    interactionResult.append(f2.bind)
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
                    interactionResult.append(f2.bind)  
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
                    interactionResult.append(f1.bind)
                    repertoire.addACell(f1.bind.feature, f1.bind.type)
                    interactionResult.append(f2.bind)
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
                    
    def test(self, aPage, repertoire):
        #page -> APC
        aPageAPC = self.page2APC(aPage)
        if not aPageAPC == None:
            self.init(aPageAPC, repertoire, "test")
            self.bind(aPageAPC, repertoire)
            interactionResult = self.proliferation(aPageAPC, repertoire)
            return self.decisionPhase(interactionResult)
        return None
    
    def train(self, aPage, repertoire):
        aPageAPC = self.page2APC(aPage)
        if True and not aPageAPC == None:
            self.init(aPageAPC, repertoire, aPage.type)
            self.bind(aPageAPC, repertoire)
            self.proliferation(aPageAPC, repertoire)
            return repertoire
        return None
      
    