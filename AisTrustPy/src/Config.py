'''
Created on Apr 29, 2009

@author: xzhou
'''

class AisConfig(object):
    '''
    AisConfig read the configration file and save it's member
    '''

    def __init__(selfparams):
        '''
        Constructor
        '''
        self.nSample = 50
        self.nSlot = 10
        
        self.ePositive = 6      #more r cells than e cells for positive case
        self.rPositive = 12
        
        self.eNegative = 6
        self.rNegative = 5
        
        self.eTest = 6
        self.rTest = 5
        
        
        