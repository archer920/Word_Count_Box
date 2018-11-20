import random
from tkinter import *


class ProductCriteriaFrame(Frame):
    def __init__(self, master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.entries_vars = []
        self.entries = []

        for i in range(0, 5):
            sr = StringVar(value=str(random.randint(70, 100)))
            self.entries_vars.append(sr)
            self.entries.append(Entry(master=self, textvariable=sr))

        for i in range(0, len(self.entries)):
            self.entries[i].grid(row=i, column=0)

        self.button = Button(self, text='Shuffle', command=lambda : self.shuffle())
        self.button.grid(row=6, column=1)

    def shuffle(self) -> None:
        for sv in self.entries_vars:
            sv.set(str(random.randint(70, 100)))


if __name__ == '__main__':
    r = Tk()

    me = ProductCriteriaFrame(master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
