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
        #self.Cells = []
        self.Cells = {} #Cells is a dictionary of list
    
    def existFeature(self, aWord):
        return self.Cells.has_key(aWord)
    
    def getNumOfCells(self):
        i = 0
        for list in self.Cells:
            i += len(list)
        return i
    
    def addACell(self, feature, type):
        if not self.Cells.has_key(feature):
            self.Cells["feature"] = []
        self.Cells[feature].append(Cell(feature, type))
        
    def addTrustWord(self, aWord):
        '''
        add positive will initialize the T Cells and R Cells according to 
        the configuration, ePositive << rPositive 
        '''
        
        if not self.Cells.has_key(aWord):
            self.Cells[aWord] = []
        
        i = 0
        while ( i < AisConfig.eTrusted):
            aCell = Cell(aWord, "E")
            self.Cells[aWord].append(aCell)
            i = i + 1
        i = 0
        while( i < AisConfig.rTrusted):
            aCell = Cell(aWord, "R")
            self.Cells[aWord].append(aCell)
            i = i + 1
        
    def addMaliciousWord(self, aWord):
        '''
        initialize a malicious word
        '''
        
        if not self.Cells.has_key(aWord):
            self.Cells[aWord] = []
        
        i = 0
        while ( i < AisConfig.eMalicious):
            aCell = Cell(aWord, "E")
            self.Cells[aWord].append(aCell)
            i = i + 1
        
        i = 0
        while ( i < AisConfig.eMalicious):
            aCell = Cell(aWord, "R")
            self.Cells[aWord].append(aCell)
            i = i + 1
    
    def addTest(self, aWord):
        
        if not self.Cells.has_key(aWord):
            self.Cells[aWord] = []
        
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
            for aList in self.Cells.values():
                for aCell in aList:
                    eFile.write(aCell.feature + " " + aCell.type +  "\n")
        except Exception, e:
            #continue write
            badCells += 1
            pass
        
        print badCells, "bad cells"
        
        eFile.close()
        
    def recover(self, fileName = "file.dmp"):
        '''
        recover will read the repertoire back from a file
        '''
        self.Cell = {}
        f = open(fileName, "r")
        for line in f:
            feature, type = line.split()
            if not self.Cells.has_key(feature):
                self.Cells["feature"] = []
            aCell = Cell(feature, type)
            self.Cells["feature"].append(aCell)
            
        
        
        