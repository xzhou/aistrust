'''
Created on Apr 16, 2009
@author: xzhou
Class WebPage represent a web page which has key words and meta info of the page.
'''

class WebPage(object):
    '''
        Class WebPage represent a web page which has key words and meta info of the page.
    '''

    def __init__(self, words=[], metadata=[], title=[], outLinks=[], inLinks=[]):
        '''
        this is the construct, words is the words sampled in the doc
        and meta data is the meta info of the web site
        '''
        self.words = words;
        self.metadata = metadata;
        self.title = title
        #connecting to other web site
        self.outLinks = outLinks
        #connection in web sites
        self.inLinks = inLinks
    
    def setWords(self, words):
        self.words = words
    
    def setMetadata(self, metadata):
        self.metadata = metadata
    
    
if __name__ == '__main__':
    pass
    
        
      