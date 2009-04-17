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
import sys

#extract the words from the record function
def extractWords(aRecord):
    try:
        soup = BeautifulSoup(aRecord, convertEntities=BeautifulSoup.HTML_ENTITIES)
        #exclude punctuation
        exclude = set(string.punctuation)
        #if the doc has body, extract the words in body
        if(soup.body):
            bodyText= soup.body(text=True)
            if(bodyText):
                pureText = " ".join(soup.body(text=True))
                pureText = ''.join(ch for ch in pureText if ch not in exclude)
                words = pureText.split()
                #print words
                return words
        else:
            allText = soup.findAll(text=True)
            #print allText
            allText = " ".join(allText)
            
            pureText = ''.join(ch for ch in allText if ch not in exclude)
            
            words = pureText.split()
            print words
            return words
            
    except Exception, e:
        print "dump error html"
        file = open("error.html", 'w')
        file.write(aRecord)
        file.close()
        #exit(0)
    

    
    
if __name__ == '__main__':
    inputFile = open("B01.txt", 'r')
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
        