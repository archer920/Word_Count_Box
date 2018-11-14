from tkinter import *

from components.ui.smart_text import SmartText


class MeasuredEntryText(SmartText):

    def __init__(self, required_word_count: int, master=None, **kw) -> None:
        super().__init__(master=master, **kw)
        self.required_word_count: int = required_word_count
        self.bind('<Key>', lambda e: self.on_entry())

    def on_entry(self) -> None:
        if self.word_count() >= self.required_word_count:
            self.config(fg='red')
        else:
            self.config(fg='green')

    def word_count(self) -> int:
        return len(self.get_text().split(' '))

    def get_text(self) -> str:
        return self.get(1.0, END).rstrip().lstrip()


if __name__ == '__main__':
    r = Tk()
    me = MeasuredEntryText(required_word_count=10, master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
