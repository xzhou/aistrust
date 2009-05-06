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
from WordStemFilter import WordProcess


def uniqueWords(strList, idfun=None): 
    '''
    order perserving uniqify words in a list
    '''
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in strList:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

#extract the words from the record function
def extractWords(aRecord):
    '''
        returns a page
    '''
    #TODO 
    aPage = APage.WebPage("", "", "")
    wp = WordProcess()
    #if True:
    try:
        soup = BeautifulSoup(aRecord, convertEntities=BeautifulSoup.HTML_ENTITIES)
        #exclude punctuation
        #exclude = set(string.punctuation)
        #if the doc has body, extract the words in body
        if(soup.title):
            title = soup.title(text = True)
            aPage.title = wp.filterAndStem(title)
            aPage.title = uniqueWords(aPage.title, None)
        
        '''
        if(soup.body):
            bodyText= soup.body(text=True)
            aPage.words = wp.filterAndStem(bodyText)
            aPage.words = uniqueWords(aPage.words, None)
        # else we extract all string
        '''
        allText = soup.findAll(text=True)
        aPage.words = wp.filterAndStem(allText)
        aPage.words = uniqueWords(aPage.words, None)
            #print len(aPage.words)
        
        #get the out link page
        links = [ each.get('href') for each in soup.findAll('a') ]
        outLinks = []
        
        for aLink in outLinks:
            if(aLink.startswith("..")): #remove the 
                pass
            else:
                outLinks.append(aLink)
        
        aPage.outLinks = outLinks
        #we have to construct the inlink
        #we need the other meta data
        return aPage, 0
     
    except Exception, e:
        print "dump error html"
        file = open("error.html", 'w')
        file.write(aRecord)
        file.close() 
        return aPage, 1

def readFile(fileName):
    inputFile = open(fileName, 'r')
    pages = []
    aRecord = ''''''
    allPages = 0
    badPages = 0
    npages = 0
    flag = False
    for line in inputFile:
        #print line
        if line.startswith("<DOC>"):
            #we have read a new blockrea
            #clear record
            aRecord = ""
        elif line.startswith("</DOC>"):
            flag = False
            #aRecord += line
            allPages += 1
            #print aRecord
            print npages, "pages extracted"
            aPage, i = extractWords(aRecord)
            if i == 0: 
                pages.append(aPage)
            badPages += i
            npages += 1
        elif line.startswith("</DOCHDR>"):
            flag = True
        else:
            if flag:
                aRecord += line
                
    print "pages processed: ", allPages
    print "bad pages: ",  badPages
    print (badPages*1.0/allPages)*100, "%"
    #return the pages in
    print "good pages: ", len(pages) 
    return pages

def readNormalHtml(fileName):
    try:
        inputFile = open(fileName, 'r')
    except Exception, e:
        print "can not open file ", fileName
        return None
    aRecord = ''''''
    for line in inputFile:
        aRecord += line
    
    return extractWords(aRecord)

if __name__ == '__main__':
    #readFile("B01.txt")
    pass