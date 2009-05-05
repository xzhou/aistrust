'''
Created on May 3, 2009

@author: xzhou
'''

import os
import sys
import DocSeperator
from Config import AisConfig
import math

class Slot:
    def __init__(self, feature):
        self.feature = feature
        self.bind = None

class PageAPC:
    '''
    class PageAPC is the Atigen Presenting Cell of a Page
    '''
    def __init__(self, features):
        self.addFeatures(features)
    
    def addFeature(self, feature):
        slots = []
        for i in range(0, AisConfig.nSlot):
            slots.append(Slot(feature))
        
        self.featureArray.append(slots)
    
    def addFeatures(self, features):
        slots = []
        for feature in features:
            for i in range(0, AisConfig.nSlot):
                slots.append(Slot(feature))
            self.featureArray.append(slots)

class ICRMSystem:
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
                i = i + 1
            pageAPC = PageAPC(sampleFeatures)
            return pageAPC
        else:
            return None
        
    def interactionPhase(self, aPageAPC, repertoire):
        '''
        this is the proliferation pahse of T, E cell with antigen
        '''
        for featureSlots in aPageAPC.featureArray:
            feature = featureSlots[0].feature
            #find nSlots R, E cells in repertoire
            specifiedCells = []
            for cell in repertoire.Cells:
                if cell.feature == feature:
                    specifiedCells.append(cell)
            
            #select nSlot specified Cells and bind to the APC
            #bind
            for i in range(0, AisConfig.nSlot):
                index = random.randint(0, len(specifiedCells) - 1)
                featureSlots[i].bind = specifiedCells[index]
            
            
        #test initilization
        for i in range(0, len(aPageAPC.featureArray), 2):
            for j in range(0, AisConfig.nSlot):
                f1 = aPageAPC.featureArray[i][j]
                f2 = aPageAPC.featureArray[i+1][j]
                pass
                #TODO add test initialization
                
                             
            
        #proliferation
        interactionResult = []
        for i in range(0, len(aPageAPC.featureArray), 2):
            for j in range(0, AisConfig.nSlot):
                f1 = aPageAPC.featureArray[i][j]
                f2 = aPageAPC.featureArray[i+1][j]
                
                if f1.bind == None:
                    if f2.bind == None:
                        #initializ the E and R
                        for k in range(0, AisConfig.eTest):
                            interactionResult.append(Cell(f1.feature, "E"))
                            interactionResult.append(Cell(f2.feature, "E"))
                        for k in range(0, AisConfig.rTest):
                            interactionResult.append(Cell(f1.feature, "R"))
                            interactionResult.append(Cell(f2.feature, "R"))                          
                    elif f2.bind.type == "E":
                        interactionResult.append(f2.bind)
                        interactionresult.append(f2.bind)
                    elif f2.bind.type == "R":
                        interactionResult.append(f2.bind)
                        
                elif f1.bind.type == "E":
                    if f2.bind == None:
                        for k in range(0, AisConfig.eTest):
                            interactionResult.append(Cell(f2.feature, "E"))
                        for k in range(0, AisConfig.rTest):
                            interactionResult.append(Cell(f2.feature, "R"))
                            
                        interactionResult.append(f1.bind)
                        interactionResult.append(f1.bind)
                    elif f2.bind.type == "E":
                        #generate 4 E
                        interactionResult.append(f1.bind)
                        interactionResult.append(f1.bind)
                        interactionResult.append(f2.bind)
                        interactionResutl.append(f2.bind)
                    elif f2.bind.type == "R":
                        interactionResult.append(f1.bind)
                        interactionResult.append(f2.bind)
                        interactionResult.append(f2.bind)
                elif f1.bind.type == "R":
                    if f2.bind == None:
                        for k in range(0, AisConfig.eTest):
                            interactionResult.append(Cell(f2.feature, "E"))
                        for k in range(0, AisConfig.rTest):
                            interactionResult.append(Cell(f2.feature, "R"))
                        interactionResult.append(f1.bind)
                    elif f2.bind.type == "E":
                        interactionResult.append(f1.bind)
                        interactionResutl.append(f1.bind)
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
        interactionResult = self.interactionPhase(aPageAPC, repertoire)
        return self.decisionPhase(interactionResult)
    
        
        
        
        
    