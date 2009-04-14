'''
Created on Apr 13, 2009

@author: xzhou

In the log files, each record include many html file and BS can not handle them
very well, we will first decompose them into single html files 
'''
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import BeautifulSoup
import re

#extract the words from the record function
def extractWords(aRecord):
    #print "call function"
    print aRecord
    soup = BeautifulSoup(aRecord)
    return aRecord


if __name__ == '__main__':
    inputFile = open("B01.txt", 'r')
    aRecord = ''''''
    for line in inputFile:
        if line.startswith("<DOC>"):
            #we have read a new block
            aRecord = ''''''.join(line)
            aRecord.join(line)
        elif line.startswith("</DOC>"):
            aRecord.join(line)
            extractWords(aRecord)
        else:
            aRecord.join(line)
        