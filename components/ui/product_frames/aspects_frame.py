from tkinter import *

from components.ui.measured_entry_frame import MeasuredEntryFrame


class AspectFrame(Frame):
    ASPECT_LABEL = 'Important Aspect {}'

    def __init__(self, word_count: int, master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.aspect_one = MeasuredEntryFrame(master = self,
                                             frame_label=AspectFrame.ASPECT_LABEL.format(1),
                                             required_word_count=word_count)
        self.aspect_two = MeasuredEntryFrame(master=self,
                                             frame_label=AspectFrame.ASPECT_LABEL.format(2),
                                             required_word_count=word_count)

        self.aspect_one.pack(side='top', fill=BOTH, expand=YES)
        self.aspect_two.pack(side='top', fill=BOTH, expand=YES)

    def get_text(self) -> str:
        return self.aspect_one.get_text() + '\n\n' + self.aspect_two.get_text() + '\n'

    def clear_text(self) -> None:
        self.aspect_one.clear_text()
        self.aspect_two.clear_text()


if __name__ == '__main__':
    r = Tk()

    me = AspectFrame(master=r, word_count=60)
    me.pack(fill=BOTH, expand=YES)
    mainloop()