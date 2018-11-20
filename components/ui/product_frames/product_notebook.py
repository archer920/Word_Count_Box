from tkinter import *
from tkinter.ttk import Notebook

from components.ui.product_frames.product_frame import ProductFrame


class ProductNotebook(Frame):

    def __init__(self, num_products: int, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.note_book = Notebook(self)
        self.note_book.enable_traversal()
        self.frames = []

        for i in range(0, num_products):
            pf = ProductFrame(master=self)
            self.note_book.add(pf, text='Product #{}'.format(i + 1))
            self.frames.append(pf)

        self.note_book.pack(expand=1, fill=BOTH)


if __name__ == '__main__':
    r = Tk()

    me = ProductNotebook(master=r, num_products=10)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
