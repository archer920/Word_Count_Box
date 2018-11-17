from tkinter import *

from components.ui.progress_entry_frame import ProgressEntryFrame


class MeasuredEntryFrame(Frame):

    def __init__(self, required_word_count: int, frame_label: str = '', master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.title_entry = Entry(master=self, bg='black', fg='green')
        self.title_entry.insert(0, frame_label)

        self.progress_entry_frame = ProgressEntryFrame(master=self, required_word_count=required_word_count)

        self.progress_entry_frame.pack(side='bottom', fill=BOTH, expand=YES)
        self.title_entry.pack(side='left', fill=X, expand=YES, anchor='n')


if __name__ == '__main__':
    r = Tk()
    me = MeasuredEntryFrame(required_word_count=10, frame_label='Important Aspect 1', master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()