from json import JSONEncoder
import random
from anytree import *
import tkinter
from tkinter import filedialog
import compressor
class SWOperator:
    def __init__(self):
        idir = 'C:\\Users\\Tanabe Koudai\\codes\\lab\\huffman\\src\\cmdTree_22-02-01-02-17.json' #初期フォルダ
        filetype = [("すべて","*")] #拡張子の選択
        file_path = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
        self.c = compressor.Compressor(file_path, 1, isJson=True)
        self.c.wholeHuffmanEncode()

    def inputcommand_random(self, root):
        def inner_inputcommand_random(node):
            if node.is_leaf:
                return
            children = node.children
            chosenNode = random.choice(children)
            chosenNode.cnt += 1
            inner_inputcommand_random(chosenNode)
        inner_inputcommand_random(root)

    def inputcommand_zipf(self):
        pass

so = SWOperator()
for i in range(1000):
    so.inputcommand_random(so.c.root)
so.c.wholeHuffmanEncode()
for i in range(20):
    print(so.c.randomEncode())