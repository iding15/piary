import re

class writeText:
    tree = "<!doctype html>\n<html>\n<head>\n\t<meta charset=\"UTF-8\">\n\t<title>Document</title>\n</head>\n<body>\n</body>\n</html>"
    def __init__(self, fileName):
        self.fileName = fileName
        self.html = open(self.fileName, 'w+')
    def getTree(self):
        html = self.html
        html.write(writeText.tree)
        html.close()
def mark_tag(tail, tag, num):
    if tag=='script':
        s_tag = '<'+tag+'>\n\t//'+tail+'_'+tag+str(num)+'//\n</'+tag+'>\n'
    elif tag=='style':
        s_tag = '<'+tag+'>\n\t/*'+tail+'_'+tag+str(num)+'*/\n</'+tag+'>\n'
    else:
        s_tag = '<'+tag+'>\n\t<!--'+tail+'_'+tag+str(num)+'-->\n</'+tag+'>\n'
    return s_tag
class hand(writeText):
    def __init__(self, fileName, tail, tag):
        self.fileName = fileName
        self.tag = tag
        self.tail = tail
        self.c = 1
        with open(self.fileName,'r') as r:
            self.s_tail = '</'+tail+'>'    
            grown_up = r.read()
            self.pattern = re.compile('('+self.s_tail+')')
            self.s_ = self.pattern.sub(mark_tag(self.tail,self.tag,self.c)+self.s_tail, grown_up)
    def stackUp(self, count):
        s_up = self.s_
        while self.c<count:
            s_up = self.pattern.sub(mark_tag(self.tail,self.tag,self.c+1)+self.s_tail, s_up)
            self.c = self.c+1
        return s_up
    def push(self):
        with open(self.fileName,'w+') as f:
            f.write(self.s_)
    def push_up(self, count):
        if count == 1:
            self.push()
        else:
            with open(self.fileName,'w+') as f:
                f.write(self.stackUp(count))
    # def tracker(self, )