import cmd
from mimetypes import init
from huffman import HuffmanCoding
from huffman_encoder import HuffmanCoding
from anytree.importer import *
from anytree import *


class Compressor:
	def __init__(self, jsonFileName, initialCnt):
		self.importer = JsonImporter(dictimporter=DictImporter(nodecls=AnyNode))
		self.old_root = self.importer.read(open(jsonFileName, 'r'))
		self.root = self.initializeTree(self.old_root, initialCnt)
		
	# Cnt変数を追加し、初期化
	# 任意文字列に対応するために<any>を追加
	def initializeTree(self, root, initialCnt):
		global newRoot
		def recursiveFunc(node):
			global newRoot
			node.cnt = initialCnt
			if node.parent == None:
				newRoot = node 
			if node.children == None:
				return
			for n in node.children:
				recursiveFunc(n)
		recursiveFunc(root)
		return newRoot

	def countIncrement(self, cmdString):
		cmdStringList = cmdString.split()
		# node.childrenにNoneは入らない前提で書いているため、使う前にNoneかどうかチェックしないといけない
		def innerCntIncrement(node, cmd):
			children_tuple = node.children
			matchNode = None
			for n in children_tuple:
				if cmd == n.name:
					n.cnt = n.cnt + 1
					matchNode = n
			if matchNode:
				return matchNode
			else:
				e = Exception('such a word doesn`t exist in these nodes')
				raise e
		_node = self.root
		for s in cmdStringList:
			_node = innerCntIncrement(_node, s)
			if _node.children == None:
				break
	# 全てのノードに対してハフマン符号再計算
	def wholeHuffmanEncode(self, node):
		children_tuple = node.children
		if children_tuple:	
			self.nodeHuffmanEncode(node)
			for n in children_tuple:
				self.wholeHuffmanEncode(n)
		

	# nodeを指定してその子ノードに対してハフマン符号化する関数
	def nodeHuffmanEncode(self, node):
		hc = HuffmanCoding()
		children_tuple = node.children
		cntList = []
		for n in children_tuple:
			cntList.append(n.cnt)
		_dict = hc.makeHuffmanDict(dict(zip(children_tuple, cntList)))
		for n in children_tuple:
			n.code = _dict[n]

	def encode(self, cmdString):
		cmdStringList = cmdString.split()
		cmdStringList.append('<cr>')
		code = ''
		
		def recursive_work(node):
			if node.children:
				children_tuple = node.children
				if cmdStringList:
					tmpTopWord = cmdStringList.pop(0)
					isExistWord = False
					for n in children_tuple:
						if n.name == tmpTopWord:
							isExistWord = True
							return n.code + recursive_work(n)
					if not isExistWord:
						raise Exception('This code is not suitable. maybe wrong words are included.')
				else:
					raise Exception('This code is not suitable. mayabe too short.')
			else:
				if cmdStringList:
					raise Exception('This code is not suitable. mayabe too long.')
				return ''
					
		return recursive_work(self.root)

c = Compressor('cmdTree_22-01-25-01-55.json', 1)

c.countIncrement('access-profile ignore-sanity-checks <cr>')
c.countIncrement('access-profile <cr>')

c.wholeHuffmanEncode(c.root)
print(RenderTree(c.root, maxlevel=10))
print(c.encode('clear aaa cache filterserver acl\r\n'))

