from tkinter import *

from components.ui.common.smart_text import SmartText


class ProductOutputFrame(Frame):
    def __init__(self, master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.smart_text = SmartText(master=self)

        self.update_button = Button(self, text='Update')
        self.clear_button = Button(text='Clear')

        self.smart_text.pack(side='top', fill=BOTH, expand=YES)
        self.update_button.pack(side='bottom', anchor='se')
        self.clear_button.pack(side='bottom', anchor='se')

    def add_line(self, line: str) -> None:
        self.smart_text.insert(END, line)

    def clear(self) -> None:
        self.smart_text.delete(0, END)


if __name__ == '__main__':
    r = Tk()
    me = ProductOutputFrame(master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
