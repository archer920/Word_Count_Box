from tkinter import *
from tkinter.ttk import *

from components.ui.measured_entry_frame import MeasuredEntryFrame


class ProgressEntryFrame(MeasuredEntryFrame):
    LABEL_TEXT = '{:.2f}% Complete: {} of {} words'

    def __init__(self, required_word_count : int, master=None, **kw) -> None:
        super().__init__(required_word_count, master, **kw)
        self.progress_label = Label(text=ProgressEntryFrame.LABEL_TEXT.format(0.0, 0, self.required_word_count))
        self.progress_label.pack(side='left', anchor='w', fill=X, expand=YES)

        self.progress = Progressbar(self, orient=HORIZONTAL, length=self.required_word_count, mode='determinate')
        self.progress.pack(side='right', anchor='e', fill=X, expand=YES)

    def on_entry(self) -> None:
        super().on_entry()
        percent = (self.word_count() / self.required_word_count) * 100
        self.progress['value'] = percent
        self.progress_label.config(
            text=ProgressEntryFrame.LABEL_TEXT.format(percent, self.word_count(), self.required_word_count))


if __name__ == '__main__':
    r = Tk()
    me = ProgressEntryFrame(required_word_count=10, master=r)
    mainloop()
