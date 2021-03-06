class GridSquare:

    def __init__(self,coords,button):
        self.col = coords[0]
        self.row = coords[1]
        self.button = button
        self.button['command'] = self.click
        self.isMine = False
        self.isMarked = False
        self.isCleared = False
        self.hasBeenZeroCleared = False
        self.clickMode = 'clear'
        self.adjacent = 0


    def click(self):
        if self.clickMode == 'clear':
            self.clear()

        elif self.clickMode == 'mark':
            self.mark()

        elif self.clickMode == 'unmark':
            self.unmark()

    def clear(self):
        self.isCleared = True
        self.button['fg'] = 'black'
        if self.isMine:
            self.button['text'] = '#' # you would lose here
        elif self.isCleared:
            self.button['text'] = self.adjacent

    def mark(self):
        self.button['text'] = 'P'
        self.button['fg'] = 'red'
        self.isMarked = True

    def unmark(self):
        self.button['text'] = '*'
        self.button['fg'] = 'black'
        self.isMarked = False
