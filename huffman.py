from __future__ import annotations
import heapq
from typing import Optional
import random

class HuffmanNode():
    def __init__(self, cnt, leaf = None):
        self.obj = leaf
        self.cnt = cnt
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None
    def __lt__(self, other):
        return self.cnt < other.cnt


class HuffmanCoding:
    def __init__(self):
        self.tree = None
        self.encode_dict = {}
        self.decode_dict = {}
    
    # _list: cnt変数を持つインスタンスのリスト
    def encode(self, _list):
        nodes = []
        for obj in _list:
            nodes.append(HuffmanNode(obj.cnt, leaf=obj))
        heapq.heapify(nodes)
        while len(nodes) >= 2:
            min1 = heapq.heappop(nodes)
            min2 = heapq.heappop(nodes)
            tmpNode = HuffmanNode(min1.cnt + min2.cnt)
            tmpNode.left = min1
            tmpNode.right = min2
            heapq.heappush(nodes, tmpNode)
        self.tree = nodes[0]
        self.recursive_code(self.tree, '')

    def recursive_code(self, node, s):
        if node.obj:
            self.encode_dict[node.obj] = s
            self.decode_dict[s] = node.obj
            return
        self.recursive_code(node.right, s+"1")
        self.recursive_code(node.left, s+"0")
    
hc = HuffmanCoding()

# 挙動チェック用のクラス
class Container():
    pass
li = []
for i in range(10):
    C = Container()
    C.cnt = random.randint(1, 100)
    li.append(C)

hc.encode(li)
