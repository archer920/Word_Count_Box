from tkinter import *

from components.ui.progress_entry_frame import ProgressEntryFrame


class MeasuredLabeledFrame(Frame):

    def __init__(self, required_word_count: int, frame_label: str, master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.label = Label(master=self, text=frame_label, bg='black', fg='green')
        self.progress_entry_frame = ProgressEntryFrame(master=self, required_word_count=required_word_count)

        self.progress_entry_frame.pack(side='bottom', fill=BOTH, expand=YES)
        self.label.pack(side='left', fill=X, expand=YES, anchor='n')


if __name__ == '__main__':
    r = Tk()
    me = MeasuredLabeledFrame(required_word_count=10, frame_label='Cost Value', master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
