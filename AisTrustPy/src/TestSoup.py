'''
Created on Apr 11, 2009

@author: xzhou
'''
from BeautifulSoup import BeautifulSoup
import re

if __name__ == '__main__':
    doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']

    soup = BeautifulSoup(''.join(doc))

    print soup.prettify()

    x = open("file.txt", 'w')