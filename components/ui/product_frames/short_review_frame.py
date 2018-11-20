from tkinter import *

from components.ui.measured_entry_frame import MeasuredEntryFrame


class ShortReviewFrame(Frame):

    def __init__(self, label: str, word_count: int, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.review_area = MeasuredEntryFrame(master=self,
                                              frame_label=label,
                                              required_word_count=word_count)
        self.review_area.pack(side='top', fill=BOTH, expand=YES)

    def get_text(self):
        return self.review_area.get_text() + '\n'

    def clear_text(self):
        self.review_area.clear_text()


if __name__ == '__main__':
    r = Tk()

    me = ShortReviewFrame(master=r, label='Product', word_count=60)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
