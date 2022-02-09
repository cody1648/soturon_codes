import random
import re

from matplotlib.pyplot import get
from huffman import HuffmanCoding
from huffman_encoder import HuffmanCoding
from anytree.importer import *
from anytree import *



class Compressor:
	def __init__(self, treeData, initialCnt, mode=None, isJson=False):
		self.importer = JsonImporter(dictimporter=DictImporter(nodecls=AnyNode))
		if isJson:
			self.old_root = self.importer.read(open(treeData, 'r'))
		else:
			self.old_root = self.importer.import_(treeData)
		self.root = self.initializeTree(self.old_root, initialCnt)
		self.mode = mode
		
	# Cnt変数を追加し、初期化
	# 任意文字列に対応する予定(まだできてない)
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

	# コマンド列の通りにツリーを走査
	# ノードの到達回数を1追加し、符号の再計算を行う 
	def countIncrement(self, cmdString):
		cmdStringList = re.sub(r'(\r?\n)|(\r\n?)',' <cr>',cmdString).split()
		# node.childrenにNoneは入らない前提で書いているため、使う前にNoneかどうかチェックしないといけない
		def innerCntIncrement(node, cmd):
			try:
				children_tuple = node.children
				matchNode = None
				for n in children_tuple:
					if cmd == n.name:
						n.cnt = n.cnt + 1
						matchNode = n
				if matchNode:
					self.nodeHuffmanEncode(node)# 符号の再計算
					return matchNode
				else:
					e = Exception('such a word doesn`t exist in these nodes')
					raise e
			except:
				import traceback
				traceback.print_exc()

		_node = self.root
		for s in cmdStringList:
			if _node.children == None:
				break			
			_node = innerCntIncrement(_node, s)

	# 全てのノードに対してハフマン符号再計算
	def wholeHuffmanEncode(self):
		_node = self.root
		def inner_wholeHuffmanEncode(node):
			children_tuple = node.children
			if children_tuple:	
				self.nodeHuffmanEncode(node)
				for n in children_tuple:
					inner_wholeHuffmanEncode(n)
		inner_wholeHuffmanEncode(_node)
		

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
		
		def recursive_work(node):
			try:
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
			except:
				import traceback
				traceback.print_exc()
		return recursive_work(self.root)

	def randomEncode(self):
		cmdLength = 0
		def inner_randomEncode(node):
			nonlocal cmdLength
			if node.is_leaf:
				return ''
			children = node.children
			chosenNode = random.choice(children)
			cmdLength += 1
			return str(chosenNode.code) + inner_randomEncode(chosenNode)
		return 	inner_randomEncode(self.root), cmdLength
	
	def getCmd_zipf(self, isAll=False):
		def getCmd(node):
			if node.is_leaf:
				return ''
			children = node.children
			chosenNode = random.choice(children)
			return chosenNode.name + ' ' + getCmd(chosenNode)
		if isAll:
			return getCmd(self.root)[:-1]
		else:
			while True: 
				if '<cr>' in (cmd := getCmd(self.root)):
					return cmd[:-1]
			

	def randomEncode_zipf(self):
		cmdLength = 0
		def inner_randomEncode(node):
			nonlocal cmdLength
			if node.is_leaf:
				return ''
			children = node.children
			prob_list = []
			prob_max = 1
			for i in range(len(children)):
				prob_list.append(prob_max / (i + 1))
			chosenNode = random.choices(children, prob_list, k=1)[0]
			cmdLength += 1
			return str(chosenNode.code) + inner_randomEncode(chosenNode)
		return 	inner_randomEncode(self.root), cmdLength

	def clearCnt(self):
		def recursiveFunc(node):
			node.cnt = 1
			if node.children == None:
				return
			for n in node.children:
				recursiveFunc(n)
		recursiveFunc(self.root)