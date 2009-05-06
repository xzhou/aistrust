'''
Created on Apr 30, 2009
@author: xzhou
'''

import Config
import DocSeperator
import APage
import sys
import Trainner
import Test
import Repertoire

def main():
    '''
    try:
        trustedDir = argv[1]
        untrustedDir = argv[2]
    except Exception, e:
        trustedDir = "../data/trusted"
        untrustedDir = "../data/untrusted"

    print "trainning on ", trustedDir, untrustedDir
    trainner = Trainner.AisTrainning()
    repertoire = trainner.train(trustedDir, untrustedDir)
    print "trainning complete, dump file"
    repertoire.dump()
    '''
    
    print "recovering from file ...", 
    repertoire = Repertoire.Repertoire()
    repertoire.recover("T2.dmp")
    print "complete, Cells=", len(repertoire.Cells)
    
    
    trustTestData = "../data/testTrusted"
    untrustedTestData = "../data/testUnTrusted"
    
    tester = Test.Detector(repertoire)
    result = tester.detect(repertoire, trustTestData, "Trusted")
    print "nPages=", result[1], " Trusted=", result[2], " Untrusted=", result[3]
    
    
    '''
    result2 = tester.detect(repertoire, untrustedTestData, "Untrusted")
    print result2
    '''
if __name__ == '__main__':
    main()
