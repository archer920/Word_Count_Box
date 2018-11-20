from tkinter import *
from tkinter.ttk import Notebook

from components.ui.criteria.criteria_frames import CriteriaFrame
from components.ui.criteria.criteria_notebook import CriteriaNotebook
from components.ui.faq.faq_notebook import FaqNotebook
from components.ui.introduction.introduction import IntroductionFrame
from components.ui.product_frames.product_notebook import ProductNotebook


class BuyingGuide(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.note_book = Notebook(self)
        self.note_book.enable_traversal()

        self.introduction_frame = IntroductionFrame(master=self, word_count=IntroductionFrame.INTRO_WORDS)
        self.note_book.add(self.introduction_frame, text='Introduction')

        self.product_frames = ProductNotebook(master=self, num_products=10)
        self.note_book.add(self.product_frames, text='Products')

        self.criteria = CriteriaNotebook(master=self, criteria_label=CriteriaNotebook.CRITERIA_LABEL,
                                         required_words=CriteriaFrame.CRITERIA_WORDS, num_criteria=5)
        self.note_book.add(self.criteria, text='Criteria')

        self.other_factors = CriteriaNotebook(master=self, criteria_label=CriteriaNotebook.OTHER_FACTORS,
                                              required_words=CriteriaFrame.OTHER_FACTORS_WORDS, num_criteria=4)
        self.note_book.add(self.other_factors, text='Other Factors')

        self.faqs = FaqNotebook(master=self)
        self.note_book.add(self.faqs, text='FAQS')

        self.note_book.pack(expand=1, fill=BOTH)


if __name__ == '__main__':
    r = Tk()

    me = BuyingGuide(master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
