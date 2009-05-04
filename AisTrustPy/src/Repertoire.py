'''
Created on Apr 29, 2009

@author: xzhou
'''

from Config import AisConfig

class Cell(object):
    def __init__(self, feature, type):
        '''
        Constructor
        '''
        self.feature = feature   #this is a inmature cell
        self.type = type    #either E or T


class Repertoire(object):
    '''
    Class Repertoire is the trained T cells and R Cells
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.Cells = []
    
    def existFeature(self, aWord):
        for cell in self.Cells:
            if cell.feature == aWord:
                return True
        return False
    
    def addTrustWord(self, aWord):
        '''
        add positive will initialize the T Cells and R Cells according to 
        the configuration, ePositive << rPositive 
        '''
        i = 0
        while ( i < AisConfig.eTrusted):
            aCell = Cell(aWord, "E")
            self.Cells.append(aCell)
            i = i + 1
        i = 0
        while( i < AisConfig.rTrusted):
            aCell = Cell(aWord, "R")
            self.Cells.append(aCell)
            i = i + 1
        
    
    def addMaliciousWord(self, aWord):
        '''
        initialize a malicious word
        '''
        i = 0
        while ( i < AisConfig.eMalicious):
            aCell = Cell(aWord, "E")
            self.Cells.append(aCell)
            i = i + 1
        
        i = 0
        while ( i < AisConfig.rMalicous):
            aCell = Cell(aWord, "R")
            self.Cells.append(aCell)
            i = i + 1
    
    def addTest(self, aWord):
        i = 0
        while( i < AisConfig.eTest):
            aCell = Cell(aWord, "E")
            self.Cells.append(aCell)
            i = i + 1
        i = 0
        while( i < AisConfig.rTest):
            aCell = Cell(aWord, "R")
            self.Cells.append(aCell)
            i = i + 1
            
    def dump(self, eFileName = "file.dmp", rFileName = "rfile.dmp"):
        try:
            eFile = open(eFileName, 'w')
            rFile = open(rFileName, 'w')
        except Exception, e:
            print "dummping error, can not open file"
        
        for aCell in self.Cells:
            #print eCell.feature
            eFile.write(aCell.feature + " " + aCell.type +  "\n")
        
        eFile.close()
        
        
        