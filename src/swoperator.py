from encodings import utf_8
from json import JSONEncoder
import math
from flask import Blueprint
from matplotlib import pyplot as plt
import random
from anytree import *
import tkinter
from tkinter import filedialog
import compressor
class SWOperator:
    def __init__(self):
        idir = 'C:\\Users\\Tanabe Koudai\\codes\\lab\\huffman\\src\\cmdTree' #初期フォルダ
        filetype = [("すべて","*")] #拡張子の選択
        file_path = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
        print(file_path)
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

    def inputcommand_zipf(self, root):
        def inner_inputcommand_zipf(node):
            if node.is_leaf:
                return '<End>'
            children = node.children
            prob_list = []
            prob_max = 1
            for i in range(len(children)):
                prob_list.append(prob_max / (i + 1))
            chosenNode = random.choices(children, prob_list, k=1)[0]
            chosenNode.cnt += 1
            return chosenNode.name + ' ' + inner_inputcommand_zipf(chosenNode)
        cmd = inner_inputcommand_zipf(root)


def test():
    for i in range(10):
        for i in range(1000):
            so.inputcommand_random(so.c.root)
        so.c.wholeHuffmanEncode()
        # print(RenderTree(so.c.root, maxlevel=3))

        ITER = 500
        sumLength = 0
        for i in range(ITER):
            tmp = so.c.randomEncode()
            # print(tmp + (round(len(tmp[0])/tmp[1], 2),))
            sumLength += len(tmp[0])/tmp[1]
        randomLength = str(round(sumLength/ITER, 2))

        so.c.clearCnt()

        for i in range(1000):
            so.inputcommand_zipf(so.c.root)
        so.c.wholeHuffmanEncode()
        # print(RenderTree(so.c.root, maxlevel=3))

        ITER = 500
        sumLength = 0
        for i in range(ITER):
            tmp = so.c.randomEncode_zipf()
            # print(tmp + (round(len(tmp[0])/tmp[1], 2),))
            sumLength += len(tmp[0])/tmp[1]
        zipfLength = str(round(sumLength/ITER, 2))

        so.c.clearCnt()

        print('random: ' + randomLength)
        print('zipf: ' + zipfLength)

def iter_test_zipf():
    nowIter = 0
    iter_list = []
    length_list = []

    for i in range(1000):
        nowIter += 10
        for i in range(10):
            so.inputcommand_zipf(so.c.root)
        so.c.wholeHuffmanEncode()
        iter_list.append(nowIter)
        # print(RenderTree(so.c.root, maxlevel=3))
        
        ITER = 1000
        sumLength = 0
        for i in range(ITER):
            tmp = so.c.randomEncode_zipf()
            # print(tmp + (round(len(tmp[0])/tmp[1], 2),))
            sumLength += len(tmp[0])/tmp[1]
        zipfLength = round(sumLength/ITER, 2)
        length_list.append(zipfLength)
        print(nowIter)
    so.c.clearCnt()
    return iter_list, length_list


def iter_test_random():
    nowIter = 0
    iter_list = []
    length_list = []

    for i in range(1000):
        nowIter += 10
        for i in range(10):
            so.inputcommand_random(so.c.root)
        so.c.wholeHuffmanEncode()
        iter_list.append(nowIter)
        # print(RenderTree(so.c.root, maxlevel=3))
        
        ITER = 1000
        sumLength = 0
        for i in range(ITER):
            tmp = so.c.randomEncode()
            # print(tmp + (round(len(tmp[0])/tmp[1], 2),))
            sumLength += len(tmp[0])/tmp[1]
        randomLength = round(sumLength/ITER, 2)
        length_list.append(randomLength)
        print(nowIter)
    so.c.clearCnt()
    return iter_list, length_list


so = SWOperator()
for i in range(100000):
    so.inputcommand_random(so.c.root)
so.c.wholeHuffmanEncode()
for i in range(20):
    tmp = so.c.randomEncode()
    print(tmp + (round(len(tmp[0])/tmp[1], 2),))
