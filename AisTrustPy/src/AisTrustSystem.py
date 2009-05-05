'''
Created on Apr 30, 2009
@author: xzhou
'''

import Config
import DocSeperator
import APage
import sys
import Trainner

def main():
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
    
    
    
    
    
    
if __name__ == '__main__':
    main()
