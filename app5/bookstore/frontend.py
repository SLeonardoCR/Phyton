"""
A program that stores book information
Title, Author
Year, ISBN 

User can: 
View all records
Search an entry 
Add an entry
Update entry 
Delete
Close
"""
from tkinter import *
from backend import Database

database = Database("books.db")

class Windows(object):
    
    def __init__(self, window):
        self.window = window

        self.window.wm_title("BookStore")

        label1 = Label(window, text="Title")
        label1.grid(row=0, column=0)

        label2 = Label(window, text="Author")
        label2.grid(row=0, column=2)

        label3 = Label(window, text="Year")
        label3.grid(row=1, column=0)

        label4 = Label(window, text="ISBN")
        label4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.entry1 = Entry(window, textvariable=self.title_text)
        self.entry1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.entry2 = Entry(window, textvariable=self.author_text)
        self.entry2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.entry3 = Entry(window, textvariable=self.year_text)
        self.entry3.grid(row=1, column=1)

        self.ISBN_text = StringVar()
        self.entry4 = Entry(window, textvariable=self.ISBN_text)
        self.entry4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        scrollbar1 = Scrollbar(window)
        scrollbar1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=scrollbar1.set)
        scrollbar1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        button1 = Button(window, text="View all", width=12, command=self.view_command)
        button1.grid(row=2, column=3)

        button2 = Button(window, text="Search entry", width=12, command=self.search_command)
        button2.grid(row=3, column=3)

        button3 = Button(window, text="Add entry", width=12, command=self.add_command)
        button3.grid(row=4, column=3)

        button4 = Button(window, text="Update", width=12, command=self.update_command)
        button4.grid(row=5, column=3)

        button5 = Button(window, text="Delete", width=12, command=self.delete_command)
        button5.grid(row=6, column=3)

        button6 = Button(window, text="Close", width=12, command=window.destroy)
        button6.grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            self.entry1.delete(0, END)
            self.entry1.insert(END, selected_tuple[1])
            self.entry2.delete(0, END)
            self.entry2.insert(END, selected_tuple[2])
            self.entry3.delete(0, END)
            self.entry3.insert(END, selected_tuple[3])
            self.entry4.delete(0, END)
            self.entry4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.view_command()

    def update_command(self):
        database.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.view_command()

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.view_command()

window=Tk()
Windows(window)
window.mainloop()



