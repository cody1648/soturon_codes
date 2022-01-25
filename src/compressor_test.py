from compressor import *

c = Compressor('cmdTree_22-01-25-01-55.json', 1)
c.wholeHuffmanEncode()
c.countIncrement('access-profile ignore-sanity-checks <cr>')
c.countIncrement('access-profile <cr>')
print(RenderTree(c.root, maxlevel=5))
print(c.encode('clear aaa cache filterserver acl\r\n'))
for i in range(10):
	c.countIncrement('clear aaa cache filterserver acl <cr>')
	print(str(i) + ': ' + c.encode('clear aaa cache filterserver acl\r\n'))
print(c.encode('clear aaa cache filterserver acl\r\n'))
print(RenderTree(c.root, maxlevel=5))
print(len(c.root.descendants))