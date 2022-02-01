from logging import root
from anytree import *
from anytree.exporter import *
from anytree.importer import *
import numpy as np

def average_length(descendants_tuple):
    length = 0
    cnt = 0
    tmpTuple = tuple(map(lambda x: len(x.name), descendants_tuple))
    std_tuple = np.std(tmpTuple)
    length = np.mean(tmpTuple)
    return length,std_tuple

def maketree_test(file_name, average_strlen=None):
    importer = JsonImporter()
    root = importer.read(open(file_name, 'r'))
    for n in root.descendants:
        n.name = 'aaa'
    print(RenderTree(root))
    exporter = JsonExporter(indent=2, sort_keys=True)
    return exporter.export(root)