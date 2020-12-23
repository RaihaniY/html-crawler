from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
def testParser(url):
    content = urlopen(url).read().decode()
    parser = Collector(url)
    parser.feed(content)
    return parser.getData()

class Collector(HTMLParser):
    'final parser of web crawler'
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.lst=[]
        self.url=url
        
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for pair in attrs:
                if pair[0].lower() == 'href':
                    if not pair[1].lower().startswith('mailto:'):
                        self.lst.append(urljoin(self.url,pair[1]))
    def getData(self):
        return self.lst
        
    
class LinksPrinter1(HTMLParser):
    'print the links in an HTML page'
    
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for pair in attrs:
                if pair[0].lower() == 'href':
                    if not pair[1].lower().startswith('mailto:'):
                        print(pair[1])

class listParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.ilst=[]
        self.inL=False #not in head
        
    def handle_data(self, data):
        if self.inL:
            self.ilst.append(data.strp())

    def handle_starttag(self,tag,attrs):
        if tag.lower()=='li':
            self.inL=True #entering into a head

    def handle_endtag(self, tag):
        if tag.lower()=='li':
            self.inL=False #leaving a head

    def getItems(self):
        return self.ilst
    

class HeaderParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.hlst=[]
        self.inH=False #not in head
        
    def handle_data(self, data):
        if self.inH:
            self.hlst.append(data)

    def handle_starttag(self,tag,attrs):
        if tag.lower() in ['h1','h2','h3','h4','h5','h6']:
            self.inH=True #entering into a head

    def handle_endtag(self, tag):
        if tag.lower() in ['h1','h2','h3','h4','h5','h6']:
            self.inH=False #leaving a head

    def getHeadings(self):
        return self.hlst
    
class DataCollector(HTMLParser):
    'collect and return the data in an HTML page'
    def __init__(self):
        HTMLParser.__init__(self)
        self.st=''

    def handle_data(self, data):
        self.st += data.strip() +' '
        
    def getData(self):
        return self.st

class DataPrinter(HTMLParser):
    'print the data in an html page'
    def handle_data(self, data):
        'print the data in the page'
        print(data)

class PrettyParser(HTMLParser):
    'parser that prints start and end tags with indents'
    def __init__(self):
        'The constructor'
        HTMLParser.__init__(self) #Call the parent constructor
        self.indent = 0
    #print the tag->use the indent
    #increase indent
    def handle_starttag(self, tag, attrs):
        'handle starting tags'
        print(f"{' '*self.indent} start {tag}")
        if tag.lower() not in ['br','img'] :
            self.indent+=4
    #print the tag -> use the indent
    #decrease the indent
    def handle_endtag(self, tag):
        'handle ending tags'
        self.indent-=4
        print(f"{' '*self.indent} end {tag}")
        
        
    
class LinksPrinter(HTMLParser):
    'print the links in an HTML page'
    
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for pair in attrs:
                if pair[0].lower() == 'href':
                    print(pair[1])

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Encountered a {tag} start tag with attrs {attrs}")
    def handle_endtag(self, tag):
        print(f"Encountered a {tag} end tag")


