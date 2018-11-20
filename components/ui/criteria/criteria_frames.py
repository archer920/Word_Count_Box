from tkinter import *
from tkinter.ttk import Combobox

from components.application_configuration.allowed_criteria import ALLOWED_CRITERIA
from components.ui.common.progress_entry_frame import ProgressEntryFrame


class CriteriaFrame(Frame):
    CRITERIA_WORDS = 275
    OTHER_FACTORS_WORDS = 75

    def __init__(self, word_count: int, available_criteria: list = ALLOWED_CRITERIA, master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.criteria_options = Combobox(self, values=sorted(available_criteria))
        self.text = ProgressEntryFrame(master=self, required_word_count=word_count)

        self.criteria_options.pack(side='top', anchor='n', fill=X)
        self.text.pack(side='bottom', fill=BOTH, expand=YES)

    def get_text(self) -> str:
        return self.criteria_options.get() + '\n' + self.text.get_text()

    def clear_text(self) -> None:
        self.criteria_options.set('')
        self.text.clear_text()


if __name__ == '__main__':
    r = Tk()

    me = CriteriaFrame(master=r, word_count=CriteriaFrame.CRITERIA_WORDS)
    me.pack(fill=BOTH, expand=YES)

    def test_get_text() -> None:
        print(me.get_text())

    def test_clear_text() -> None:
        me.clear_text()

    get_btn = Button(master=r, text='Test Get', command=test_get_text)
    clear_btn = Button(master=r, text='Test Clear', command=test_clear_text)

    get_btn.pack(side='left', anchor='w')
    clear_btn.pack(side='right', anchor='e')

    mainloop()
