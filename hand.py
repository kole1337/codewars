class Hand:
    ORDER = 'A23456789TJQK'
    PTS   = {f:i for i,f in enumerate(ORDER,1)}
    
    def __init__(self, hand):
        self.h       = hand[:]
        self.score   = float('inf')
        self.discard = None
        self.study()
    
    def get_hand(self):   return self.h[:]
    def get_score(self):  return self.score
    
    def add_card(self,c):
        if not self.score: return c
        self.h.append(c)
        self.discard = c
        self.study()
        return self.discard

    @staticmethod
    def cardScore(c): return Hand.PTS[c[0]]

    @staticmethod
    def buildMeldOf(lst):
        target = lst[-1][0]
        meld   = [c for c in lst if c[0]==target]
        if len(meld)>=3:        yield [c for c in lst if c[0]!=target]
        if len(meld)==4:
            for i in range(4):  yield [c for c in lst if c[0]!=target or c==meld[i] ]
    
    @staticmethod
    def buildRunOf(lst):
        (face,col), r = lst[-1], [lst[-1]]
        s = { c for c in lst if c[1]==col and face!=c[0] }
        iFace = Hand.cardScore(lst[-1])-1
        while iFace:
            iFace -= 1
            nc = Hand.ORDER[iFace]+col
            if nc not in s: break
            r.append(nc)
            s.discard(nc)
            
        tailAce = 'A'+col
        tailing = face=='K' and tailAce in s
        sR      = set(r)
        while len(r)+tailing > 2:
            if tailing and len(r)>1:  yield [c for c in lst if c not in sR and c!=tailAce]
            if len(r)>2:              yield [c for c in lst if c not in sR]
            sR.discard(r.pop())
            
            
    def study(self):
        
        def dfs(lst):
            if len(lst)<3:                                             # end of search...
                end = sorted(out+lst, key=Hand.cardScore)
                if isDiscard and not end: return
                rem   = end.pop() if isDiscard else None
                score = sum(map(Hand.cardScore, end))
                if self.score > score:
                    self.score,self.discard = score,rem
            else:
                for genFunc in (self.buildMeldOf, self.buildRunOf):    # melds then runs, built on the current last card
                    for others in genFunc(lst):
                        dfs(others)
                        
                out.append(lst[-1])                                    # nothing doable with this card...
                dfs(lst[:-1])
                out.pop()
            
        isDiscard, out = len(self.h)==8, []
        dfs(sorted(self.h, key=Hand.cardScore))
        if isDiscard:
            self.h.remove(self.discard)
            
            
            #https://www.codewars.com/kata/5b75aa794eb8801bd0000033/train/python