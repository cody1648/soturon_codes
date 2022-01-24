'''
参考：https://k-yuya.hatenablog.com/entry/2018/07/18/231731
'''

from __future__ import annotations
import heapq
from typing import Optional

class HuffmanNode():
    def __init__(self, cnt, value = None):
        self.value = value
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
    
    def makeHuffmanDict(self, _dict) -> dict:
        nodes = []
        for val, cnt in _dict.items():
            nodes.append(HuffmanNode(cnt, val))
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
        return self.encode_dict

    def recursive_code(self, node, s) -> None:
        if node.value:
            self.encode_dict[node.value] = s
            self.decode_dict[s] = node.value
            return
        self.recursive_code(node.right, s+"1")
        self.recursive_code(node.left, s+"0")