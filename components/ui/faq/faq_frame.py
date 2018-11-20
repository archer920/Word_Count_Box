from tkinter import *

from components.ui.common.measured_entry_frame import MeasuredEntryFrame


class FaqFrame(Frame):
    FAQ_WORDS = 75

    def __init__(self, word_count: int, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.review_area = MeasuredEntryFrame(master=self,
                                              frame_label='',
                                              required_word_count=word_count)
        self.review_area.pack(side='top', fill=BOTH, expand=YES)

    def get_text(self):
        return self.review_area.get_text() + '\n'

    def clear_text(self):
        self.review_area.clear_text()


if __name__ == '__main__':
    r = Tk()

    me = FaqFrame(master=r, word_count=FaqFrame.FAQ_WORDS)
    me.pack(fill=BOTH, expand=YES)

    def test_get_text() -> None:
        print(me.get_text())

    def test_clear_text() -> None:
        me.clear_text()

    get_btn = Button(master=r, text='Test Get', command=test_get_text)
    clear_btn = Button(master=r, text='Test Clear', command=test_clear_text)

    get_btn.pack(side='left', anchor='w')
    clear_btn.pack(side='right', anchor='e')

    mainloop()