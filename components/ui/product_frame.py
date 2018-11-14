from tkinter import *

from components.application_configuration.product_frame_configuration import ProductFrameConfiguration
from components.ui.measured_entry_frame import MeasuredEntryFrame
from components.ui.scrolled_frame import VerticalScrolledFrame


class _ProductFrame(Frame):

    def __init__(self, pfc: ProductFrameConfiguration, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.introduction = MeasuredEntryFrame(master=self,
                                               frame_label=pfc.introduction_title,
                                               required_word_count=pfc.introduction_word_count)

        self.aspects = []
        for i in range(1, pfc.num_aspects + 1):
            aspect = MeasuredEntryFrame(master=self,
                                        frame_label=pfc.aspect_label(i),
                                        required_word_count=pfc.aspect_word_count)
            self.aspects.append(aspect)

        self.cost_value = MeasuredEntryFrame(master=self,
                                             frame_label=pfc.cost_value_title,
                                             required_word_count=pfc.cost_value_count)

        self.pros = []
        for i in range(1, pfc.num_pros + 1):
            pro = MeasuredEntryFrame(master=self,
                                     frame_label=pfc.pro_label(i),
                                     required_word_count=pfc.pro_word_count)
            self.pros.append(pro)

        self.cons = []
        for i in range(1, pfc.num_cons + 1):
            con = MeasuredEntryFrame(master=self,
                                     frame_label=pfc.con_label(i),
                                     required_word_count=pfc.con_word_count)
            self.cons.append(con)

        widgets = [self.introduction, *self.aspects, self.cost_value, *self.pros, *self.cons]
        for w in widgets:
            w.pack(side='top', fill=BOTH, expand=YES)


class ProductFrame(Frame):

    def __init__(self, pfc: ProductFrameConfiguration, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.scroll_frame = VerticalScrolledFrame(master)
        self.scroll_frame.pack(fill=BOTH, expand=YES)

        self.pfc_frame = _ProductFrame(pfc=pfc, master=self.scroll_frame.interior)
        self.pfc_frame.pack(fill=BOTH, expand=YES)


if __name__ == '__main__':
    r = Tk()
    pfc = ProductFrameConfiguration(introduction_title='Product',
                                    introduction_word_count=60,
                                    num_aspects=2, aspect_label_template='Important Aspect {}', aspect_word_count=30,
                                    cost_value_title='Cost and Value', cost_value_count=30,
                                    num_pros=5, pro_label_template='Pro {}', pro_word_count=10,
                                    num_cons=2, con_label_template='Con {}', con_word_count=10)
    me = ProductFrame(master=r, pfc=pfc)
    me.pack(fill=BOTH, expand=YES)
    mainloop()
