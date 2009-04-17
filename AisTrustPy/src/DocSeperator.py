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
import APage

#extract the words from the record function
def extractWords(aRecord):
    '''
        returns the 
    '''
    #TODO 
    aPage = APage.WebPage("", "", "")
    try:
        soup = BeautifulSoup(aRecord, convertEntities=BeautifulSoup.HTML_ENTITIES)
        #exclude punctuation
        exclude = set(string.punctuation)
        #if the doc has body, extract the words in body
        if(soup.title):
            title = soup.title(text = True)
            if(title):
                title = " ".join(title)
                title = ''.join(ch for ch in title if ch not in exclude)
                aPage.title = title
        
        if(soup.body):
            bodyText= soup.body(text=True)
            if(bodyText):
                pureText = " ".join(soup.body(text=True))
                pureText = ''.join(ch for ch in pureText if ch not in exclude)
                words = pureText.split()
                aPage.words = words
            else:
                aPage.words = []
        # else we extract all string
        else:
            allText = soup.findAll(text=True)
            allText = " ".join(allText)   
            pureText = ''.join(ch for ch in allText if ch not in exclude)
            words = pureText.split()
            aPage.words = words
        
        #get the out link page
        
        aPage.outLink = [ each.get('href') for each in soup.findAll('a') ]
        
        #we have to construct the inlink
        
        #we need the other meta data
        
        return aPage, 0
        
    except Exception, e:
        print "dump error html"
        file = open("error.html", 'w')
        file.write(aRecord)
        file.close() 
        return aPage, 1
    
if __name__ == '__main__':
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