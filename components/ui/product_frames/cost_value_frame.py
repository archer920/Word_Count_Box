from tkinter import *

from components.ui.common.measured_labeled_frame import MeasuredLabeledFrame


class CostValueFrame(Frame):
    LABEL = 'Cost and Value'

    def __init__(self, word_count: int, master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.review_area = MeasuredLabeledFrame(master=self,
                                                frame_label=CostValueFrame.LABEL,
                                                required_word_count=word_count)
        self.review_area.pack(side='top', fill=BOTH, expand=YES)

    def get_text(self) -> str:
        return self.review_area.get_text() + '\n'

    def clear_text(self) -> None:
        self.review_area.clear_text()


if __name__ == '__main__':
    r = Tk()

    me = CostValueFrame(master=r, word_count=60)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
