from tkinter import *

class Gui:
    def __init__(self):
        self.execution = False

    def lunch(self):
        root = Tk()
        root.title('Motlab PIV')

        root.mainloop()

        return self.execution
