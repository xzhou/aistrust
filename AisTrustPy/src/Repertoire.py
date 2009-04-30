'''
Created on Apr 29, 2009

@author: xzhou
'''
class Cell(object):
    def __init__(self):
        '''
        Constructor
        '''
        self.feature = ""   #this is a inmature cell



class Repertoire(object):
    '''
    Class Repertoire is the trained T cells and R Cells
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.TCells = []    #this is the T cells
        pself.RCells = []   #this is the R cells
    
    def addTCell(self, tCell):
        try:
            if(type(tCell) == Cell):
                self.TCells.append(tCell)
            
        except Exception, e:
            print "error: addTCell(), make sure you passed a valid cell"
        
    
    def addRCell(self, rCell):
        try:
            if(type(tCell) == Cell):
                self.RCells.append(rCell)
        except Exception, e:
            print "error: addRCell(), make sure you passed a valid cell"