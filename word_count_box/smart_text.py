from tkinter import *


class SmartText(Text):
    def __init__(self, master=None, cnf={}, fg='green', bg='black',
                 insertbackground='white', padx=10, pady=10, wrap=WORD, **kw):
        super().__init__(master, cnf, fg=fg, bg=bg,
                         insertbackground=insertbackground, wrap=wrap, padx=padx, pady=10, **kw)
        self._key_bindings()


    def undo(self):
        print('undo')
        pass

    def redo(self):
        print('redo')
        pass

    def cut(self):
        print('cut')
        pass

    def copy(self):
        print('copy')
        pass

    def paste(self):
        print('paste')
        pass

    def select_all(self):
        print('select all')
        self.tag_add(SEL, '1.0', END + '-1c')
        self.mark_set(INSERT, '1.0')
        self.see(INSERT)

    def focus_next(self):
        print('Next Item')

    def focus_previous(self):
        print('Previous Item')

    def _key_bindings(self):
        self.bind('<Command-a>', lambda e: self.select_all())
        self.bind('<Control-a>', lambda e: self.select_all())

        self.bind('<Command-z>', lambda e: self.undo())
        self.bind('<Control-z>', lambda e: self.undo())

        self.bind('<Command-y>', lambda e: self.redo())
        self.bind('<Control-y>', lambda e: self.redo())

        self.bind('<Command-x>', lambda e: self.cut())
        self.bind('<Control-x>', lambda e: self.cut())

        self.bind('<Command-c>', lambda e: self.copy())
        self.bind('<Control-c>', lambda e: self.copy())

        self.bind('<Command-v>', lambda e: self.paste())
        self.bind('<Control-v>', lambda e: self.paste())

        self.bind('<Control-Tab>', lambda e: self.focus_next())
        self.bind('<Shift-Tab>', lambda e: self.focus_previous())


if __name__ == '__main__':
    tk = Tk()
    st = SmartText(tk).pack()
    mainloop()
