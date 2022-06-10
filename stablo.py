from red import Red

class TreeNode(object):
    __slots__='parent','children','data','value','closed_morris',"igrac","game_over","polje1","polje2","uklonjeno_polje"

    def __init__(self,data=None):
        self.parent=None
        self.children=[]
        self.data=data

        
        self.value=None #vrednost heuristike table
        self.closed_morris=False #da li je spojena trojka u tom potezu
        self.igrac=None #koji igrac je spojio trojku
        self.game_over=False #da li je kraj igre

        self.polje1=None #polje sa kog je pomjerena mica
        self.polje2=None #polje na koje je stavljena mica
        self.uklonjeno_polje=None #polje na kom je uklonjena mica
    
    def is_root(self):
        return self.parent is None
    
    def is_leaf(self):
        return len(self.children)==0
    
    def add_child(self,c):
        c.parent=self
        self.children.append(c)
    

    
class Tree(object):
    def __init__(self):
        self.root=None
    
    def is_empty(self):
        return self.root is None
    
    def depth(self,x):
        if x.is_root():
            return 0
        else:
            return 1+self.depth(x.parent)

    def _height(self,x):
        if x.is_leaf():
            return 0
        else:
            return 1+max(self.height(c) for c in x.children)
    
    def height(self):
        return self._height(self.root)
    
    def preorder(self,x):
        if not self.is_empty():
            print(x.data)
            for c in x.children:
                self.preorder(c)

    def postorder(self,x):
        if not self.is_empty():
            for c in x.children:
                self.postorder(c)
            print(x.data)
    
    def breadth_first(self):
        to_visit=Red()
        to_visit.dodaj(self.root)
        while not to_visit.is_empty():
            e=to_visit.izbaci()
            print(e.data)

            for c in e.children:
                to_visit.dodaj(c)
    

    