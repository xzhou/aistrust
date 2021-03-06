'''
Created on Apr 29, 2009

@author: xzhou
'''
from APage import WebPage
from Config import AisConfig
from Repertoire import Repertoire
import DocSeperator
from ICRM import ICRMSystem

import os
import random



class AisTrainning(object):
    '''
    AisTrainning read web pages one by one and train the Ais system
    '''
    
    def __init__(self):
        self.repertoire = Repertoire()
    
    def setRepertoire(self, repertoire):
        self.repertoire = repertoire

    def trainOnePage(self, aWebPage, repertoire):
        #sample n words in webpage
        aICRMSys = ICRMSystem()
        if aWebPage == None:
            return None
        aICRMSys.train(aWebPage, repertoire)
    
    
    def trainOnPages(self, pages):
        print "train on ", len(pages), " pages"
        for page in pages:
            print ".",
            self.trainOnePage(page, self.repertoire)
        print ""
    
    
    def processDir(self, stats, directory, fileList):
        '''
        process Dir will scan through the directory in a directory
        stats:    the stats of file
        directory: is the current scanning directory
        fileList is the file inside the current directory
        '''
        if(stats[0] == "trusted"):
            for file in fileList:
                fullFileName = os.path.join(directory, file)
                print "processing file: ", fullFileName
                if os.path.isfile(fullFileName):
                    pages = DocSeperator.readFile(fullFileName)
                    print "number of pages", len(pages)
                    for page in pages:
                        page.type = "trusted"
                    self.trainOnPages(pages)
                else:      
                    print "not file: ", fullFileName
        else: # a untrusted website
            for file in fileList:
                fullFileName = os.path.join(directory, file)
                print "processing file: ", fullFileName
                if os.path.isfile(fullFileName):
                    page = DocSeperator.readNormalHtml(fullFileName)
                    if page:
                        print "******"
                        page.type = "malicious"
                        self.trainOnePage(page, self.repertoire)
                    else:
                        print page
                        pass
                else:      
                    print "not file: ", fullFileName
    
    def shuffleCells(self):
        for list in self.repertoire.Cells.values():    
            random.shuffle(list)
    
    def train(self, trusted, untrusted):
        '''
        Function Train will scan the trusted directory for trusted web site and 
        scan the untrusted directory for untrusted website.
        '''
        #trainning on trusted website
        trustedStats = ["trusted", 0, 0, 0]   #number of pages, bad pages, other
        os.path.walk(trusted, self.processDir, trustedStats)
        
        unTrustedStates = ["untrusted", 0, 0, 0]
        #os.path.walk(untrusted, self.processDir, unTrustedStates)
        
        self.shuffleCells()
        return self.repertoire
        
    def main(self, trustedDir, untrustedDir):
        pass
        
        
        