from tkinter import *
from tkinter.ttk import Notebook

from components.ui.criteria.criteria_frames import CriteriaFrame
from components.ui.faq.faq_frame import FaqFrame


class FaqNotebook(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.note_book = Notebook(self)
        self.note_book.enable_traversal()
        self.frames = []

        for i in range(0, 5):
            cf = FaqFrame(master=self, word_count=75)
            self.note_book.add(cf, text='Faq #{}'.format(i + 1))
            self.frames.append(cf)

        self.note_book.pack(expand=1, fill=BOTH)


if __name__ == '__main__':
    r = Tk()

    me = FaqNotebook(master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
