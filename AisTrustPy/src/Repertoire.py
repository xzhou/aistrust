'''
Created on Apr 29, 2009

@author: xzhou
'''

from Config import AisConfig


class RCell(object):
    def __init__(self, feature):
        '''
        Constructor
        '''
        self.feature = feature   #this is a inmature cell

class ECell(object):
    def __init__(self, feature):
        '''Constructor'''
        self.feature = feature


class Repertoire(object):
    '''
    Class Repertoire is the trained T cells and R Cells
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.ECells = []    #this is the T cells
        self.RCells = []   #this is the R cells
    
    def existFeature(self, aWord):
        for cell in self.ECells:
            if cell.feature == aWord:
                return True
        for cell in self.RCells:
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
            aCell = ECell(aWord)
            self.ECells.append(aCell)
            i = i + 1
        i = 0
        while( i < AisConfig.rTrusted):
            aCell = RCell(aWord)
            self.RCells.append(aCell)
            i = i + 1
        
    
    def addMaliciousWord(self, aWord):
        '''
        initialize a malicious word
        '''
        i = 0
        while ( i < AisConfig.eMalicious):
            aCell = ECell(aWord)
            self.ECells.append(aCell)
            i = i + 1
        
        i = 0
        while ( i < AisConfig.rMalicous):
            aCell = RCell(aWord)
            self.RCells.append(aCell)
            i = i + 1
    
    def addTest(self, aWord):
        i = 0
        while( i < AisConfig.eTest):
            aCell = Cell(aWord)
            self.ECells.append(aCell)
            i = i + 1
        i = 0
        while( i < AisConfig.rTest):
            aCell = Cell(aWord)
            self.RCells.append(aCell)
            i = i + 1
            
    def dump(self, eFileName = "efile.dmp", rFileName = "rfile.dmp"):
        try:
            eFile = open(eFileName, 'w')
            rFile = open(rFileName, 'w')
        except Exception, e:
            print "dummping error, can not open file"
        
        for eCell in self.ECells:
            #print eCell.feature
            eFile.write(eCell.feature + "\n")
        
        eFile.close()
        
        for rCell in self.RCells:
            #print rCell.feature
            rFile.write(rCell.feature + "\n")
            
        rFile.close()

        
        
        