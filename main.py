import random
import sys

class roj(object):
    
    board = []
    revealed = []
    width = 20
    height = 10
    
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        for y in range(self.height):
            self.board.append([])
            self.revealed.append([])
            for x in range(self.width):
                self.board[y].append(random.choice(["*", " ", " ", " ", " ", " ", " "]))
                self.revealed[y].append(False)
        self.countBoard()
    
    def showBoard(self, showAll=False):
        print("\n  ", end="")
        for x in range(self.width):
            print(str(x%10), end="")
        print("")
        for y in range(self.height):
            print(str(y%10), end=" ")
            for x in range(self.width):
                if not self.revealed[y][x] and not showAll:
                    print("X", end="")
                elif self.board[y][x] == "0":
                    print(" ", end="")
                else:
                    print(self.board[y][x], end="")
            print("")
    
    def isValid(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def getLocal(self, x, y):
        local = []
        for yy in range(-1, 2):
            for xx in range(-1, 2):
                if self.isValid(x+xx, y+yy):
                    local.append((self.board[y+yy][x+xx], (x+xx, y+yy)))
        return local
    
    def checkLocal(self, x, y):
        n = 0
        for p, _ in self.getLocal(x, y):
            if p == "*":
                n += 1
        return n

    def countBoard(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.board[y][x] == "*":
                    self.board[y][x] = str(self.checkLocal(x, y))
    
    def reveal(self, x, y, searched=[]):
        for p, (xp, yp) in self.getLocal(x, y):
            if (xp, yp) in searched:
                pass
            elif p == "0":
                self.revealed[yp][xp] = True
                searched.append((xp, yp))
                self.reveal(xp, yp, searched)
            elif p == "*":
                pass
            else:
                self.revealed[yp][xp] = True
    
    

r = roj(30, 20)
r.showBoard(True)
while True:
    r.showBoard()
    inp = input(">> ")
    split = inp.split(",")
    r.reveal(int(split[0]), int(split[1]))

