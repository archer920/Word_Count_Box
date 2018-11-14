from typing import *

from tkinter import *
from components.ui.smart_text import SmartText


class MeasuredEntryFrame(Frame):

    def __init__(self, required_word_count: int, master=None, **kw) -> None:
        super().__init__(master, **kw)
        self.required_word_count: int = required_word_count

        self.text = SmartText(self)
        self.text.pack(side='top', anchor='w', fill=BOTH, expand=YES)
        self.text.bind('<Key>', lambda e: self.on_entry())
        self.pack(fill=BOTH, expand=YES)

    def on_entry(self) -> None:
        if self.word_count() >= self.required_word_count:
            self.text.config(fg='red')
        else:
            self.text.config(fg='green')

    def word_count(self) -> int:
        return len(self.get_text().split(' '))

    def get_text(self) -> str:
        return self.text.get(1.0, END).rstrip().lstrip()


if __name__ == '__main__':
    r = Tk()
    me = MeasuredEntryFrame(required_word_count=10, master=r)
    mainloop()
