from tkinter import *
from tkinter.ttk import *

from components.ui.common.measured_entry_text import MeasuredEntryText


class ProgressEntryFrame(Frame):
    LABEL_TEXT = '{:.2f}% Complete: {} of {} words'

    def __init__(self, required_word_count: int, master=None, **kw) -> None:
        super().__init__(master, **kw)
        self.measured_entry = MeasuredEntryText(required_word_count=required_word_count, master=self)
        self.measured_entry.pack(side='top', anchor='w', fill=BOTH, expand=YES)

        self.progress_label = Label(master=self, text=ProgressEntryFrame.LABEL_TEXT.format(0.0, 0, self.measured_entry.required_word_count))
        self.progress_label.pack(side='left', anchor='s')

        self.progress = Progressbar(self, orient=HORIZONTAL,
                                    length=self.measured_entry.required_word_count, mode='determinate')
        self.progress.pack(side='right', anchor='s', fill=X, expand=YES)
        self.measured_entry.bind('<Key>', lambda e: self.on_entry())

    def on_entry(self) -> None:
        self.measured_entry.on_entry()
        percent = (self.measured_entry.word_count() / self.measured_entry.required_word_count) * 100
        self.progress['value'] = percent
        self.progress_label.config(
            text=ProgressEntryFrame.LABEL_TEXT.format(percent, self.measured_entry.word_count(), self.measured_entry.required_word_count))

    def get_text(self) -> str:
        return self.measured_entry.get_text()

    def clear_text(self) -> None:
        self.measured_entry.clear_text()


if __name__ == '__main__':
    r = Tk()
    me = ProgressEntryFrame(required_word_count=10, master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
