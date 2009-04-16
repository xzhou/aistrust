'''
Created on Apr 13, 2009

@author: xzhou

In the log files, each record include many html file and BS can not handle them
very well, we will first decompose them into single html files 
'''
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import BeautifulSoup
import re
import urllib2
import string
import timeit

#extract the words from the record function
def extractWords(aRecord):
    soup = BeautifulSoup(aRecord, convertEntities=BeautifulSoup.HTML_ENTITIES)
    exclude = set(string.punctuation)
    pureText = " ".join(soup.body(text=True))
    pureText = ''.join(ch for ch in pureText if ch not in exclude)
    words = pureText.split()
    return words
    
    

if __name__ == '__main__':
    inputFile = open("test.html", 'r')
    aRecord = ''''''
    for line in inputFile:
        #print line
        if line.startswith("<DOC>"):
            #we have read a new block
            aRecord = line
        elif line.startswith("</DOC>"):
            aRecord+=line
            extractWords(aRecord)
        else:
            aRecord+=line
        