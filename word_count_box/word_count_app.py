import json
import os

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from components.ui.smart_text import SmartText

CONFIG_FILE = 'word_counts.json'








class AddWordCountFrame(Frame):

    def __init__(self, update_cb=None, master=None, **kw):
        super().__init__(master, **kw)
        self.update_cb = update_cb

        label = Label(self, text='Add a label')
        count_label = Label(self, text='Add a word count')

        self.name_box = Entry(self)
        self.word_box = Entry(self)
        self.add_btn = Button(self, text='Add', command=self.on_add)

        label.grid(row=0, column=0, sticky='W')
        self.name_box.grid(row=0, column=1)

        count_label.grid(row=1, column=0, sticky='W')
        self.word_box.grid(row=1, column=1)
        self.add_btn.grid(row=1, column=2)

    def on_add(self):
        label = self.name_box.get()
        word_count = self.word_box.get()

        if self.__is_valid(label, word_count):
            self.__write_to_json(label, word_count)
            messagebox.showinfo('Added', 'Added {} : {}'.format(label, word_count))

            if self.update_cb:
                self.update_cb()

    @staticmethod
    def __is_valid(label, word_count):
        if not label:
            messagebox.showerror('Error', 'You need a label')
            return False
        if not word_count:
            messagebox.showerror('Error', 'Need a word count')
            return False

        if not word_count.isdigit():
            messagebox.showerror('Error', 'Only positive integers are allowed')
            return False

        word_num = int(word_count)
        if word_num == 0:
            messagebox.showerror('Error', 'Only positive integers are allowed')
            return False

        return True

    @staticmethod
    def __write_to_json(label, word_count):
        values = {}

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE) as fin:
                values = json.load(fin)

        values[label] = word_count

        with open(CONFIG_FILE, 'w') as fout:
            fout.write(json.dumps(values, indent=4, sort_keys=True))


class SelectFrame(Frame):

    def __init__(self, entry_frame, master=None, **kw):
        super().__init__(master, **kw)

        self.entry_frame = entry_frame
        self.values = {}
        self.combo_box = Combobox(self, values=sorted(self.values.keys()))
        self.refresh_values()

        self.select_btn = Button(self, text='Select', command=self.on_select)

        self.combo_box.pack(side='left', anchor='w')
        self.select_btn.pack(side='left', anchor='w')

    def refresh_values(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE) as fin:
                self.values = json.load(fin)
                if self.combo_box:
                    self.combo_box.config(values=sorted(self.values.keys()))

    def on_select(self):
        selection = self.combo_box.get()

        if selection in self.values:
            self.entry_frame.max_words = int(self.values[selection])
            self.entry_frame.on_entry()
        else:
            messagebox.showerror('Error', 'Please pick a value')


class MainWindow(Frame):

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.entry_frame = ProgressEntryFrame(max_words=100, master=master)
        self.select_frame = SelectFrame(entry_frame=self.entry_frame, master=master)
        self.add_word_count_frame = AddWordCountFrame(update_cb=self.select_frame.refresh_values, master=master)

        self.add_word_count_frame.pack(side='top', fill=BOTH, expand=TRUE)
        self.select_frame.pack(side='top', fill=BOTH, expand=TRUE)
        self.entry_frame.pack(side='top', fill=BOTH, expand=TRUE)


if __name__ == '__main__':
    me = MainWindow(master=Tk()).pack()
    mainloop()
