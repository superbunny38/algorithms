class Node:
    def __init__(self,symbol=None,freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
    
class Solution:
    def huffmanCodes(self,S,f,N):
        store = []
        for letter,freq in zip(S,f):
            store.append(Node(symbol=letter,freq=freq))
        
        store.sort(key= lambda x:x.freq)
        
        while len(store)>1:
            store.sort(key=lambda x:x.freq)
            left_node = store.pop(0)
            right_node = store.pop(0)
            merged_node = Node(freq=left_node.freq+right_node.freq)
            merged_node.left,merged_node.right = left_node,right_node
            store.append(merged_node)
        
        huff_dict = dict()
        
        def encode(node,code,huff_dict):
            if node is not None:
                if node.symbol is not None:
                    huff_dict[node.symbol] = code
            
                encode(node.left,code+'0',huff_dict)
                encode(node.right,code+'1',huff_dict)
            else:
                return  
        encode(store[0],'',huff_dict)
        
        
        return huff_dict
    
S = "abcdef"
f = [5, 9, 12, 13, 16, 45]
N = 6

s = Solution().huffmanCodes(S=S,f=f,N=N)
print(s)