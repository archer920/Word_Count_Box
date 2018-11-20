from tkinter import *
from tkinter.ttk import Notebook

from components.application_configuration.product_review_configuration import DEFAULT_PRODUCT_CONFIGURATION
from components.ui.product_frames.aspects_frame import AspectFrame
from components.ui.product_frames.cost_value_frame import CostValueFrame
from components.ui.product_frames.criteria_rating_frame import ProductCriteriaFrame
from components.ui.product_frames.pro_cons_frame import ProConsFrame
from components.ui.product_frames.product_output_frame import ProductOutputFrame
from components.ui.product_frames.short_review_frame import ShortReviewFrame


class ProductFrame(Frame):

    def __init__(self, product_review_configuration=DEFAULT_PRODUCT_CONFIGURATION, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.note_book = Notebook(self)
        self.note_book.enable_traversal()

        self.short_summary = ShortReviewFrame(master=self,
                                              label=product_review_configuration.short_review_title,
                                              word_count=product_review_configuration.short_review_word_count)
        self.note_book.add(self.short_summary, text='Short Summary')

        self.criteria_rating = ProductCriteriaFrame(master=self)
        self.note_book.add(self.criteria_rating, text='Product Criteria')

        self.aspects = AspectFrame(master=self,
                                   word_count=product_review_configuration.aspect_word_count)
        self.note_book.add(self.aspects, text='Important Aspects')

        self.cost_value = CostValueFrame(master=self,
                                         word_count=product_review_configuration.cost_value_count)
        self.note_book.add(self.cost_value, text='Cost and Value')

        self.pros = ProConsFrame(master=self, frame_label=ProConsFrame.PROS,
                                 word_count=product_review_configuration.pro_word_count,
                                 num_entries=product_review_configuration.num_pros)
        self.note_book.add(self.pros, text='Pros')

        self.cons = ProConsFrame(master=self, frame_label=ProConsFrame.CONS,
                                 word_count=product_review_configuration.con_word_count,
                                 num_entries=product_review_configuration.num_cons)
        self.note_book.add(self.cons, text='Cons')

        self.output_frame = ProductOutputFrame(self)
        self.output_frame.update_button.configure(command=self.update_review)
        self.output_frame.clear_button.configure(command=self.clear)
        self.note_book.add(self.output_frame, text='Product Review')

        self.note_book.pack(expand=1, fill=BOTH)

        self.short_summary.review_area.progress_entry_frame.measured_entry.next_widget = self.aspects.aspect_one.title_entry

    def update_review(self) -> None:
        self.output_frame.add_line(self.short_summary.get_text() + '\n')
        self.output_frame.add_line(self.aspects.get_text() + '\n')
        self.output_frame.add_line(self.cost_value.get_text() + '\n')
        self.output_frame.add_line(self.pros.get_text() + '\n\n')
        self.output_frame.add_line(self.cons.get_text() + '\n')

    def clear(self) -> None:
        self.output_frame.smart_text.clear_text()
        self.short_summary.clear_text()
        self.aspects.clear_text()
        self.cost_value.clear_text()
        self.pros.clear_text()
        self.cons.clear_text()


if __name__ == '__main__':
    r = Tk()

    me = ProductFrame(master=r)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
