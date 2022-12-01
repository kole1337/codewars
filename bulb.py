from itertools import count


class Bulb(set):
    def __init__(self,x,y): super().__init__() ; self.pos = x,y
    def __hash__(self):     return hash(self.pos)
    def __eq__(self,o):     return self.pos == o.pos
    def __str__(self):      return "({},{})".format(*self.pos)
    
    
def switch_bulbs(s):
    
    def findNeighs(x,y):
        for dx,dy in moves:
            for n in count(1):
                i,j = pos = x+n*dx, y+n*dy
                if not(0<=i<X and 0<=j<Y): break
                if pos in bulbs:           yield bulbs[pos] ; break
                
    
    def solveDFS():
        if len(path)==len(bulbs): return 1
        
        cnds = set(path[-1] if path else bulbs.values())
        while cnds:
            b = min(cnds, key=len)
            if not b and len(path)!=len(bulbs)-1: break
            cnds.discard(b)
            path.append(b)
            for neigh in b: neigh.discard(b)
            if solveDFS(): return 1
            for neigh in b: neigh.add(b)
            path.pop()
    
    #---------------------------------------------------------------
    
    moves = [ (dx,dy) for dx in range(-1,2) for dy in range(-1,2) if dx or dy ]
    board = list( map(list, re.sub(r'[-+|]+','',s).strip().splitlines()) )
    X,Y   = len(board), len(board[0])
    bulbs = { (x,y): Bulb(x,y) for x,r in enumerate(board) for y,c in enumerate(r) if c=='B' }
    for b in bulbs.values(): 
        b.update(findNeighs(*b.pos))
        
    path  = []
    return solveDFS() and [b.pos for b in path]

#https://www.codewars.com/kata/5a96064cfd57777828000187/train/python