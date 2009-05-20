'''
Created on May 6, 2009

@author: xzhou
'''

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import socket



class WebCrowler(object):
    '''
    donwload the webpages
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getPages(self, pageList="WEBSPAM-UK2007-hostnames.txt"):
        
        timeout = 10
        socket.setdefaulttimeout(5)
        
        fPageList = open(pageList, "r")
        lines = fPageList.readlines()
        urlList = []
        for line in lines:
            id, hostName = line.split()
            url = "http://"+hostName
            urlList.append(url)
        
        #downlaod the page
        i = 0;
        for url in urlList:
            i = i + 1
            print i
            print i, url
            try:
                page = urllib2.urlopen(url)
                lines = page.readlines()
                fname = "./malData/" + str(i)+".txt"
                f = open(fname, 'w')
                for line in lines:
                    f.write(line)
                f.close()
                page.close()
            except Exception, e:
                pass
                
if __name__ == '__main__':      
    wc = WebCrowler()
    wc.getPages()
            
        