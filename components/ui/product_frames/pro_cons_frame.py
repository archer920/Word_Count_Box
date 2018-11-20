from tkinter import *

from components.ui.measured_labeled_frame import MeasuredLabeledFrame


class ProConsFrame(Frame):
    PROS = 'Pro {}'
    CONS = 'Con {}'

    def __init__(self, frame_label: str, word_count: int, num_entries: int, master=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.frames = []

        for i in range(0, num_entries):
            self.frames.append(MeasuredLabeledFrame(master=self,
                                                    frame_label=frame_label.format(i + 1),
                                                    required_word_count=word_count))
        for f in self.frames:
            f.pack(side='top', fill=BOTH, expand=YES)

    def get_text(self) -> str:
        text = []
        for f in self.frames:
            text.append(f.progress_entry_frame.measured_entry.get_text())
        return '\n'.join(text)

    def clear_text(self) -> None:
        for f in self.frames:
            f.clear_text()


if __name__ == '__main__':
    r = Tk()

    pro = ProConsFrame(master=r, frame_label=ProConsFrame.PROS, word_count=10, num_entries=5)
    pro.pack(fill=BOTH, expand=YES)

    pro = ProConsFrame(master=r, frame_label=ProConsFrame.CONS, word_count=10, num_entries=2)
    pro.pack(fill=BOTH, expand=YES)

    mainloop()
