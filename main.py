from Tkinter import *
from random import randint
import game as G

class TK(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master.title("Minesweeper")
        self.grid()
        self.setup()

    def winCheck(self):
        marked = 0
        cleared = 0
        for i in range(8):
            for j in range(8):
                sq = self.playGrid[i][j]
                if sq.isMarked:
                    marked += 1
                if sq.isCleared:
                    cleared += 1
        if marked + cleared == 64:
            for i in range(8):
                for j in range(8):
                    self.playGrid[i][j].button['fg'] = 'green'
        else:
            self.WIN['fg'] = 'red'

    def doNothing(self):
        pass

    def clearMode(self):
        self.CLEAR['fg'] = 'blue'
        self.MARK['fg'] = 'black'
        self.UNMARK['fg'] = 'black'
        for i in range(8):
            for j in range(8):
                square = self.playGrid[i][j]
                square.clickMode = 'clear'

    def markMode(self):
        self.MARK['fg'] = 'blue'
        self.CLEAR['fg'] = 'black'
        self.UNMARK['fg'] = 'black'
        for i in range(8):
            for j in range(8):
                square = self.playGrid[i][j]
                square.clickMode = 'mark'

    def unmarkMode(self):
        self.MARK['fg'] = 'black'
        self.CLEAR['fg'] = 'black'
        self.UNMARK['fg'] = 'blue'
        for i in range(8):
            for j in range(8):
                square = self.playGrid[i][j]
                square.clickMode = 'unmark'

    def setMine(self):
        target = [randint(0,7),randint(0,7)]
        self.playGrid[target[0]][target[1]].isMine = True if self.playGrid[target[0]][target[1]].isMine == False else self.setMine()

    def setup(self):

        # initialize variables
        self.playGrid = [[],[],[],[],[],[],[],[]]

        # make grid of buttons
        for x in range(8):
            for y in range(8):
                tmpButton = Button(self)
                tmpButton['text'] = '*'
                tmpButton['command'] = self.doNothing
                tmpButton.grid(row=y,column=x)
                tmpSquare = G.GridSquare([x,y],tmpButton)
                self.playGrid[y].append(tmpSquare)

        # set mines
        for i in range(10):
            self.setMine()

        # assign values to all buttons
        for i in range(8):
            for j in range(8):
                sq = self.playGrid[i][j]
                value = 0

                for row in [sq.row-1,sq.row,sq.row+1]:
                    for col in [sq.col-1,sq.col,sq.col+1]:

                        if row <= 8 and row >= 0 and col <= 8 and col >= 0:
                            try:
                                if self.playGrid[row][col].isMine:
                                    value += 1
                            except: pass #out of bobunds

                sq.adjacent = value

        # reset grid clickmode
        for i in range(8):
            for j in range(8):
                square = self.playGrid[i][j]
                square.clickMode = 'clear'

        # make UI buttons
        self.CLEAR = Button(self)
        self.CLEAR['text'] = 'Mode: CLEAR'
        self.CLEAR['command'] = self.clearMode
        self.CLEAR['fg'] = 'blue'
        self.CLEAR.grid(row=9,column=0,columnspan=4,sticky=W+E)

        self.NEW  = Button(self)
        self.NEW  ['text'] = 'New Grid'
        self.NEW  ['command'] = self.setup
        self.NEW.grid(row=9,column=4,columnspan=4,sticky=W+E)

        self.MARK  = Button(self)
        self.MARK ['text'] = 'Mode: MARK '
        self.MARK ['command'] = self.markMode
        self.MARK.grid(row=10,column=0,columnspan=4,sticky=W+E)

        self.WIN = Button(self)
        self.WIN['text'] = 'I think I won!'
        self.WIN['command'] = self.winCheck
        self.WIN.grid(row=10,column=4,columnspan=4,sticky=W+E)

        self.UNMARK  = Button(self)
        self.UNMARK ['text'] = 'Mode: UNMARK'
        self.UNMARK ['command'] = self.unmarkMode
        self.UNMARK.grid(row=11,column=0,columnspan=4,sticky=W+E)

        self.QUIT = Button(self)
        self.QUIT['text'] = 'QUIT'
        self.QUIT['command'] = quit
        self.QUIT['fg'] = 'red'
        self.QUIT.grid(row=11,column=4,columnspan=4,sticky=W+E)

root = Tk()
app = TK(master=root)
app.mainloop()
