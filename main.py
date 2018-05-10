from Tkinter import *
from random import randint
import game as G

class TK(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.setup()

    def winCheck(self):
        for i in range(self.D):
            for j in range(self.D):
                sq = self.playGrid[i][j]
                if sq.isMarked:
                    self.marked += 1
                if sq.isCleared:
                    self.cleared += 1
        self.master.title("Marks Remaining: "+str(self.totalMines-self.marked) if self.totalMines-self.marked >= 0 else "You Marked Too Many!")
        if self.cleared == (self.D*self.D)-self.totalMines:
            for i in range(self.D):
                for j in range(self.D):
                    if not self.playGrid[i][j].isMine:
                        self.playGrid[i][j].button['fg'] = 'green'
        else:
            for i in range(self.D):
                for j in range(self.D):
                    sq = self.playGrid[i][j]
                    if sq.isMine and sq.isCleared:
                        for k in range(self.D):
                            for l in range(self.D):
                                self.playGrid[k][l].button['fg'] = 'red'
            root.after(200,self.winCheck)

    def clearSurrounding(self,sq):

        sq.hasBeenZeroCleared = True

        for row in [sq.row-1,sq.row,sq.row+1]:
            for col in [sq.col-1,sq.col,sq.col+1]:

                if row in range(self.D) and col in range(self.D):
                    #try:
                    if (not self.playGrid[row][col].isMarked) or (not self.playGrid[row][col].isCleared):
                        self.playGrid[row][col].clear()
                    #except: print "Excepted",row,col #out of bobunds

    def clearZeros(self):

        for i in range(self.D):
            for j in range(self.D):

                sq = self.playGrid[i][j]
                if (not sq.hasBeenZeroCleared):
                    if (sq.adjacent == 0):
                        if (sq.isCleared):
                            self.clearSurrounding(sq)

        root.after(200,self.clearZeros)

    def doNothing(self):
        pass

    def clearMode(self):
        self.winCheck()
        self.CLEAR['fg'] = 'blue'
        self.MARK['fg'] = 'black'
        self.UNMARK['fg'] = 'black'
        for i in range(self.D):
            for j in range(self.D):
                square = self.playGrid[i][j]
                square.clickMode = 'clear'

    def markMode(self):
        self.winCheck()
        self.MARK['fg'] = 'blue'
        self.CLEAR['fg'] = 'black'
        self.UNMARK['fg'] = 'black'
        for i in range(self.D):
            for j in range(self.D):
                square = self.playGrid[i][j]
                square.clickMode = 'mark'

    def unmarkMode(self):
        self.winCheck()
        self.MARK['fg'] = 'black'
        self.CLEAR['fg'] = 'black'
        self.UNMARK['fg'] = 'blue'
        for i in range(self.D):
            for j in range(self.D):
                square = self.playGrid[i][j]
                square.clickMode = 'unmark'

    def setMine(self):
        target = [randint(0,self.D-1),randint(0,self.D-1)]
        if self.playGrid[target[0]][target[1]].isMine == False:
            self.playGrid[target[0]][target[1]].isMine = True
        else:
            self.setMine()

    def setup(self):

        # initialize variables
        self.playGrid = []
        self.totalMines = 10
        self.D = 16
        self.mines = 0
        self.cleared = 0
        self.marked = 0

        # make grid of buttons
        for x in range(self.D):
            self.playGrid.append([])
            for y in range(self.D):
                tmpButton = Button(self)
                tmpButton['text'] = '*'
                tmpButton['command'] = self.doNothing
                tmpButton.grid(row=x,column=y)
                tmpSquare = G.GridSquare([x,y],tmpButton)
                self.playGrid[x].append(tmpSquare)

        # set mines
        n = 0
        while n < self.totalMines:
            self.setMine()
            n += 1

        # assign values to all buttons
        for i in range(self.D):
            for j in range(self.D):
                sq = self.playGrid[i][j]
                value = 0

                for row in range(sq.row-1,sq.row+2):
                    for col in range(sq.col-1,sq.col+2):

                        if row in range(self.D) and col in range(self.D):
                            if self.playGrid[row][col].isMine:
                                value += 1

                sq.adjacent = value

        # reset grid clickmode
        for i in range(self.D):
            for j in range(self.D):
                square = self.playGrid[i][j]
                square.clickMode = 'clear'

        # make UI buttons and labels
        self.CLEAR = Button(self)
        self.CLEAR['text'] = 'Mode: CLEAR'
        self.CLEAR['command'] = self.clearMode
        self.CLEAR['fg'] = 'blue'
        self.CLEAR.grid(row=self.D+1,column=0,columnspan=4,sticky=W+E)

        self.NEW  = Button(self)
        self.NEW  ['text'] = 'New Grid'
        self.NEW  ['command'] = self.setup
        self.NEW.grid(row=self.D+1,column=4,rowspan=4,columnspan=self.D-4,sticky=N+S+W+E)

        self.MARK  = Button(self)
        self.MARK ['text'] = 'Mode: MARK '
        self.MARK ['command'] = self.markMode
        self.MARK.grid(row=self.D+3,column=0,columnspan=4,sticky=W+E)

        self.UNMARK  = Button(self)
        self.UNMARK ['text'] = 'Mode: UNMARK'
        self.UNMARK ['command'] = self.unmarkMode
        self.UNMARK.grid(row=self.D+4,column=0,columnspan=4,sticky=W+E)

root = Tk()
app = TK(master=root)
app.after(200,app.winCheck)
app.after(100,app.clearZeros)
app.mainloop()
