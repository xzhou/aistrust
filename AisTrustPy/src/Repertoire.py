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
    
    def addACell(self, feature, type):
        self.Cells.append(Cell(feature, type))
        
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
        while ( i < AisConfig.eMalicious):
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
        except Exception, e:
            print "dummping error, can not open file"
        
        print "dumping repertoire to file: ", len(self.Cells)
        badCells = 0
        try:
            for aCell in self.Cells:
            #print aCell.feature, aCell.type
                eFile.write(aCell.feature + " " + aCell.type +  "\n")
        except Exception, e:
            #continue write
            badCells += 1
            pass
        
        print badCell, "bad cells"
        
        eFile.close()
        
    def recover(self, fileName = "file.dmp"):
        '''
        recover will read the repertoire back from a file
        '''
        self.Cell = []
        f = open(fileName, "r")
        for line in f:
            feature, type = line.split()
            aCell = Cell(feature, type)
            self.Cells.append(aCell)
        
        
        