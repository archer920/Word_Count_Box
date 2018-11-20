from tkinter import *

from components.ui.common.progress_entry_frame import ProgressEntryFrame


class MeasuredEntryFrame(Frame):

    def __init__(self, required_word_count: int, frame_label: str = '', master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.text_var = StringVar()
        self.title_entry = Entry(master=self, bg='black', fg='green', textvariable=self.text_var)
        self.title_entry.insert(0, frame_label)

        self.progress_entry_frame = ProgressEntryFrame(master=self, required_word_count=required_word_count)

        self.progress_entry_frame.pack(side='bottom', fill=BOTH, expand=YES)
        self.title_entry.pack(side='left', fill=X, expand=YES, anchor='n')

    def get_text(self) -> str:
        return self.title_entry.get() + '\n' + self.progress_entry_frame.get_text()

    def clear_text(self) -> None:
        self.text_var.set('')
        self.progress_entry_frame.clear_text()


if __name__ == '__main__':
    r = Tk()
    me = MeasuredEntryFrame(required_word_count=10, frame_label='Important Aspect 1', master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
