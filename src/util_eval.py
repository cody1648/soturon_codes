from compressor import *
from anytree import *
from anytree.exporter import *
from anytree.importer import *
import numpy as np

def average_length(descendants_tuple):
    print('length:' + str(len(descendants_tuple)))
    length = 0
    cnt = 0
    # <cr>を除いて考えたい
    tmpList = list(map(lambda x: None if x.name == '<cr>' else len(x.name), descendants_tuple))
    tmpList = [i for i in tmpList if i != None]
    print(len(tmpList))
    std_length = np.std(tmpList)
    length = np.mean(tmpList)
    return length,std_length

def maketree_test(file_name, average_strlen=None):
    importer = JsonImporter()
    root = importer.read(open(file_name, 'r'))

    def inner_func(node):
        if node.is_leaf:
            return
        for i, n in enumerate(node.children):
            n.name = str(i + 1)
            inner_func(n)
    
    inner_func(root)
    exporter = JsonExporter(indent=2, sort_keys=True)
    return exporter.export(root)