from piary import writeText, hand
file = 'test.html'
test = writeText(file)
test.getTree()

hs = hand(file, 'head', 'style')
hs.push_up(1)
hscr = hand(file, 'head', 'script')
hscr.push_up(2)
bscr = hand(file, 'body', 'script')
bscr.push_up(4)

