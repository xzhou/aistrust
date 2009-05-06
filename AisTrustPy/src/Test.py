'''
Created on May 6, 2009

@author: xzhou
'''

import os
import DocSeperator
import ICRM

class Detector(object):
    '''
    Ais test will read a directory of file and report the test result
    '''
    def __init__(self, repertoire):
        '''
        Constructor
        '''
        self.repertoire = repertoire
    
    def testOnePage(self, aPage, repertoire):
        aICRMSys = ICRM.ICRMSystem()
        return aICRMSys.test(aPage, repertoire)
    
    def processDir(self, result, directory, fileList):
        for file in fileList:
            fullFileName = os.path.join(directory, file)
            print "testing file", fullFileName
            
            if os.path.isfile(fullFileName):
                #need some process
                pages = DocSeperator.readFile(fullFileName)
                result[1] += len(pages)
                for page in pages:
                    page.pageType = "test"
                    pageScore = self.testOnePage(page, self.repertoire)
                    if not pageScore:
                        pass
                    elif pageScore <= 0:
                        result[3] += 1
                    else:
                        result[2] += 1
    def detect(self, repertoire, fileDir, type=""):
        if type not in ["Trusted", "Untrusted"]:
            raise Exception("unsupported type");
        result = [type, 0, 0, 0] #type, nPages, trustedPages, untrustedPages
        os.path.walk(fileDir, self.processDir, result);
        
        return result