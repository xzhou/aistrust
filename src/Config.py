'''
Created on Apr 29, 2009

@author: xzhou
'''

class AisConfig(object):
    '''
    AisConfig read the configration file and save it's member
    '''

    nSample = 50 #number of features must be a even number
    nSlot = 10
    
    eTrusted = 6      #more r cells than e cells for positive case
    rTrusted = 12
    
    eMalicious = 6
    rMalicious = 5
    
    eTest = 6
    rTest = 5
        
    def __init__(self):
        '''
        Constructor
        '''
        pass
        
        
        