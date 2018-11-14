from tkinter import *


class SmartText(Text):
    def __init__(self, master=None, next_widget=None, previous_widget=None, cnf={}, fg='green', bg='black', undo=True,
                 insertbackground='white', padx=10, pady=10, wrap=WORD, **kw):
        super().__init__(master, cnf, fg=fg, bg=bg, undo=undo,
                         insertbackground=insertbackground, wrap=wrap, padx=padx, pady=pady, **kw)
        self.next_widget = next_widget
        self.previous_widget = previous_widget
        self._key_bindings()

    def select_all(self):
        self.tag_add(SEL, '1.0', END + '-1c')
        self.mark_set(INSERT, '1.0')
        self.see(INSERT)

    def focus_next(self):
        if self.next_widget:
            self.next_widget.focus_set()

    def focus_previous(self):
        if self.previous_widget:
            self.previous_widget.focus_set()

    def _key_bindings(self):
        self.bind('<Command-a>', lambda e: self.select_all())
        self.bind('<Control-a>', lambda e: self.select_all())

        self.bind('<Control-Tab>', lambda e: self.focus_next())
        self.bind('<Shift-Tab>', lambda e: self.focus_previous())


if __name__ == '__main__':
    f = Frame(Tk())
    st = SmartText(f)
    st2 = SmartText(f)
    st3 = SmartText(f)

    st.next_widget = st2

    st2.next_widget = st3
    st2.previous_widget = st

    st3.previous_widget = st2

    st.grid(row=0, column=0)
    st2.grid(row=0, column=1)
    st3.grid(row=0, column=2)

    f.pack()
    mainloop()
