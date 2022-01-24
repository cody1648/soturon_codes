from huffman_encoder import HuffmanCoding
import random

hc = HuffmanCoding()
# 挙動チェック用のクラス
_dict = {
        'a': random.randint(1,100),
        }
print(_dict)
tmpDict = hc.makeHuffmanDict(_dict)
print(tmpDict)
print(hc.decode_dict)