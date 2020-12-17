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
def mark_tag(tail, tag, num, tab=1):
    if tag=='script':
        s_tag = '\t'*tab+'<'+tag+'>\n\t'+'\t'*tab+'//'+tail+'_'+tag+str(num)+'//\n'+'\t'*tab+'</'+tag+'>\n'
    elif tag=='style':
        s_tag = '\t'*tab+'<'+tag+'>\n\t'+'\t'*tab+'/*'+tail+'_'+tag+str(num)+'*/\n'+'\t'*tab+'</'+tag+'>\n'
    else:
        s_tag = '\t'*tab+'<'+tag+'>\n\t'+'\t'*tab+'<!--'+tail+'_'+tag+str(num)+'-->\n'+'\t'*tab+'</'+tag+'>\n'
    return s_tag
class hand:
    def __init__(self, fileName, tail):
        self.fileName = fileName
        self.tail = tail
    def borrow(self):
        with open(self.fileName, 'r') as r:
            asset = r.read()
        return asset
    def earn(self,asset):
        with open(self.fileName, 'w+') as f:
            f.write(asset)
    def push_up(self, tagList, countList):
        tail = self.tail
        s_tail = '</'+tail+'>'
        pattern = re.compile('('+s_tail+')')  
        s_up = self.borrow()       
        c_=0     
        for tag in tagList:           
            c=1
            s_up = pattern.sub(mark_tag(tail,tag,c)+s_tail,s_up)
            while c<countList[c_]:
                s_up = pattern.sub(mark_tag(tail,tag,c+1)+s_tail, s_up)
                c = c+1
            c_=c_+1
            # with open(self.fileName, 'w+') as f:
            #     f.write(s_up)
            self.earn(s_up)
            self.borrow()
    def tracker(self, tail, tag, num):
        long_tail=tail+'_'+tag
        if tag == 'script':
            leash = '//'+long_tail+str(num)+'//'
        elif tag == 'style':
            leash = '/*'+long_tail+str(num)+'*/'
        else:
            leash = '<!--'+long_tail+str(num)+'-->'
        return leash
    def children(self, tag, num, kids):
        tail=self.tail
        leash=self.tracker(tail, tag, num)
        asset=self.borrow()    
        tab=2
        long_tail=tail
        for kid in kids:
            leash=self.tracker(long_tail,tag,num)
            long_tail=long_tail+'_'+tag
            asset=asset.replace('\t'*tab+leash,mark_tag(long_tail,kid,num,tab))
            tail=tag
            tag=kid
            tab=tab+1
            self.earn(asset)
            asset=self.borrow()