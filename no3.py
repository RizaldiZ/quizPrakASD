class Tree(object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None
 
        
A = Tree('1')
B = Tree('2')
C = Tree('3')
D = Tree('4')
E = Tree('5')
F = Tree('6')
G = Tree('7')

A.kiri = B ; A.kanan = C
B.kiri = D ; B.kanan = E
C.kiri = F ; C.kanan = G

def luarKanan(data):
    if data.kanan is not None:
        luarKanan(data.kanan)
    print(data.data)
def luarKiri(data):
    if data.kiri is not None:
        luarKiri(data.kiri)
    print(data.data)