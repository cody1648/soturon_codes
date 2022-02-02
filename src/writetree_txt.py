from anytree import *
from anytree import importer
from anytree.importer import *
import tkinter
from tkinter import filedialog
from os import path


importer = JsonImporter(dictimporter=DictImporter(nodecls=Node))
idir = 'C:\\Users\\Kodai\\python_test\\' #初期フォルダ
filetype = [("すべて","*")] #拡張子の選択
file_path = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
root = importer.read(open(file_path,'r'))
f = open('cmdTree\\' + path.splitext(path.basename(file_path))[0] + '.txt', 'w', encoding='utf-8')
for pre, _ , node in RenderTree(root):
    f.write('%s%s\n' % (pre, node.name))