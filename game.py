class GridSquare:

    def __init__(self,coords,button):
        self.col = coords[0]
        self.row = coords[1]
        self.button = button
        self.button['command'] = self.click
        self.isMine = False
        self.isMarked = False
        self.isCleared = False
        self.clickMode = 'clear'
        self.adjacent = 0


    def click(self):
        if self.clickMode == 'clear':
            self.isCleared = True
            self.button['fg'] = 'black'

            if self.isMine:
                self.button['text'] = '#' # you would lose here
            elif self.isCleared:
                self.button['text'] = self.adjacent

        elif self.clickMode == 'mark':
            self.button['text'] = 'P'
            self.button['fg'] = 'red'
            self.isMarked = True

        elif self.clickMode == 'unmark':
            self.button['text'] = '*'
            self.button['fg'] = 'black'
            self.isMarked = False
