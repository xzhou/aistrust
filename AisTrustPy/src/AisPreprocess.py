'''
Created on Apr 13, 2009

@author: xzhou
'''

from BeautifulSoup import BeautifulSoup

if __name__ == '__main__':
    inputFile = open("onhtml.htm", 'r');
    lines = inputFile.readlines();
    
    #print lines
    
    soup = BeautifulSoup(''.join(lines))
    
    print soup.prettify()
    
    