def plants_and_zombies(lawn,zombies):
    PvZ = Game(lawn, zombies)
    end = PvZ.run()
    return end
    
class Game:
    
    def __init__(self, lawn, zombies):
        self.lawn = [list(e) for e in lawn]
        self.end_f = len(lawn[0])
        self.l = len(lawn)
        self.zombies = { (y,t+(self.end_f-1)):h for t,y,h in zombies }
        self.gameOver = 0
        
    def _action(self):
        for func, shoot in zip((lambda x:x not in ' S', lambda x:x == 'S'), ( ((0,1),), ((-1,1),(0,1),(1,1)) ) ):
            for y in range(self.end_f-1,-1,-1):
                for x in range(self.l):
                    if func(self.lawn[x][y]):
                        st = self.lawn[x][y]
                        self._make_shooting(x,y, shoot, (1 if st == 'S' else int(st)) )
        self._moveZone()
            
    def _make_shooting(self, X_,Y_, typeS, damage ):
        for x,y in typeS:
            for _ in range(damage):
                X, Y = X_, Y_
                while Y<self.end_f-1 and -1<X<self.l:
                    X, Y = X+x, Y+y
                    if self.zombies.get((X,Y)):
                        self.zombies[(X,Y)] -= 1
                        break
        
    def _moveZone(self):
        tz = {}
        for (x,y),h in self.zombies.items():
            if h:
                tz[(x, y-1)] = h
                self._terminated(x, y-1)
                if not y: self.gameOver = 1
        self.zombies = tz
    
    def _terminated(self, x, y):
        if y<self.end_f and  self.lawn[x][y] != ' ': self.lawn[x][y] = ' '
                
    def run(self, timer = 0):
        while not self.gameOver:
            self._action()
            timer += 1
            if not self.zombies: return
        return timer
    
#https://www.codewars.com/kata/5a5db0f580eba84589000979/train/python