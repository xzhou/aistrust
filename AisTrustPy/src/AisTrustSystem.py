'''
Created on Apr 30, 2009
@author: xzhou
'''

import Config
import DocSeperator
import APage

def main():
    inputFile = open("B01.txt", 'r')
    aRecord = ''''''
    allPages = 0
    badPages = 0
    for line in inputFile:
        #print line
        if line.startswith("<DOC>"):
            #we have read a new block
            aRecord = line
        elif line.startswith("</DOC>"):
            aRecord += line
            allPages += 1
            aPage, i = extractWords(aRecord)
            badPages += i
        else:
            aRecord+=line
    
    print "pages processed: ", allPages
    print "bad pages: ",  badPages
    print (badPages*1.0/allPages)*100, "%"


if __name__ == '__main__':
    main()
