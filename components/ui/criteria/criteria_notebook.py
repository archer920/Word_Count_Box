from tkinter import *
from tkinter.ttk import Notebook

from components.ui.criteria.criteria_frames import CriteriaFrame


class CriteriaNotebook(Frame):
    CRITERIA_LABEL = 'Criteria {}'
    OTHER_FACTORS = 'Other Factors {}'

    def __init__(self, criteria_label: str, num_criteria: int, required_words: int, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.note_book = Notebook(self)
        self.note_book.enable_traversal()
        self.frames = []

        for i in range(0, num_criteria):
            cf = CriteriaFrame(master=self, word_count=required_words)
            self.note_book.add(cf, text=criteria_label.format(i + 1))
            self.frames.append(cf)

        self.note_book.pack(expand=1, fill=BOTH)


if __name__ == '__main__':
    r = Tk()

    me = CriteriaNotebook(master=r,criteria_label=CriteriaNotebook.CRITERIA_LABEL, num_criteria=5, required_words=CriteriaFrame.CRITERIA_WORDS)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
