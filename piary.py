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
    def push_up(self, tagList, countList):
        tail = self.tail
        s_tail = '</'+tail+'>'
        pattern = re.compile('('+s_tail+')')  
        with open(self.fileName,'r') as r:
            s_up = r.read()       
        c_=0     
        for tag in tagList:           
            c=1
            s_up = pattern.sub(mark_tag(tail,tag,c)+s_tail,s_up)
            while c<countList[c_]:
                s_up = pattern.sub(mark_tag(tail,tag,c+1)+s_tail, s_up)
                c = c+1
            c_=c_+1
            with open(self.fileName, 'w+') as f:
                f.write(s_up)
            with open(self.fileName, 'r') as r:
                s_up = r.read()
    # def draw(self, children=[self.tag], contents):
    #     if children==[]:


# def tracker(head_body, tag, num):
#     if tag == 'script':
#         leash = '//'+head_body+'_'+tag+num+'//'
#     elif tag == 'style':
#         leash = '/*'+head_body+'_'+tag+num+'*/'
#     else:
#         leash = '<!--'+head_body+'_'+tag+num+'-->'
#     return leash
# class paper:
#     def __init__(self,fileName,head_body,tag,num):
#         self.fileName = fileName
#         self.tag = tag
#         self.leash = tracker(head_body, tag, num)
#         with open(self.fileName,'r') as r:
#             self.grown_up = r.read()
#     def draw(self,contents):
        