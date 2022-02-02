from numpy import c_
from util_eval import *
from compressor import *

c = Compressor('cmdTree_22-02-01-02-17.json', 1, isJson=True)
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
c_test = Compressor(maketree_test('cmdTree_22-02-01-02-17.json'), 1, isJson=False)
c_test.wholeHuffmanEncode()
c_test.countIncrement('29 2')
print(RenderTree(c_test.root, maxlevel=2))
# print(average_length(c.root.descendants))