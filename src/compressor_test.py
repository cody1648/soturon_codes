from util import *
from compressor import *

c = Compressor('cmdTree_22-02-01-02-17.json', 1)
c.wholeHuffmanEncode()
c.countIncrement('access-profile ignore-sanity-checks \r\n')
c.countIncrement('access-profile\r\n')

print(c.encode('clear aaa cache filterserver acl\r\n'))
for i in range(10):
	c.countIncrement('clear aaa cache filterserver acl\r\n')
	print(str(i + 1) + ': ' + c.encode('clear aaa cache filterserver acl\r\n'))
print(c.encode('clear aaa cache filterserver acl\r\n'))
# print(RenderTree(c.root, maxlevel=10))
# mu, sigma
maketree_test('cmdTree_22-02-01-02-17.json')