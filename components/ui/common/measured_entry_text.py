from tkinter import *

from components.ui.common.smart_text import SmartText


class MeasuredEntryText(SmartText):
    HEIGHT_OFFSET = 10

    def __init__(self, required_word_count: int, master=None, **kw) -> None:
        expected_height = int(required_word_count / MeasuredEntryText.HEIGHT_OFFSET)
        if expected_height == 0:
            expected_height = 1

        super().__init__(master=master, height=expected_height, **kw)
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

    def change_required_words(self, required_word_count: int) -> None:
        expected_height = int(required_word_count / MeasuredEntryText.HEIGHT_OFFSET)
        if expected_height == 0:
            expected_height = 1
        self.configure(height=expected_height)

if __name__ == '__main__':
    r = Tk()
    me = MeasuredEntryText(required_word_count=20, master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
