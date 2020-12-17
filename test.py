from piary import writeText, hand
file = 'test.html'
test = writeText(file)
test.getTree()

h = hand(file, 'head')
h.push_up(['style','script'],[2,3])
b = hand(file, 'body')
b.push_up(['div','p','script'],[2,4,2])
b.children('div',2,['p','div','ul','li'])

