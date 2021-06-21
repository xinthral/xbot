"""
Interactive SQL Window
TKinter GUI allowing interaction between user and database
"""
import tkinter as tk
from tkinter.ttk import Treeview
from xsql import Database

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.display_child = None
        self.navibar_child = None
        self.setup()

    def create_window_menu(self):
        """ Builds menubar for main window """
        self.main_menu = tk.Menu(self)

        # File Menu
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label='New', command=None)
        self.file_menu.add_command(label='Open', command=None)
        self.file_menu.add_command(label='Save', command=None)
        self.file_menu.add_command(label='Save As..', command=None)
        self.file_menu.add_command(label='Close', command=None)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=window.quit)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)

        # Edit Menu
        self.edit_menu = tk.Menu(self.main_menu, tearoff=0)
        self.edit_menu.add_command(label='Cut', command=None)
        self.edit_menu.add_command(label='Copy', command=None)
        self.edit_menu.add_command(label='Paste', command=None)
        self.edit_menu.add_command(label='Delete', command=None)
        self.edit_menu.add_command(label='Select All', command=None)
        self.main_menu.add_cascade(label='Edit', menu=self.edit_menu)

        # Help Menu
        self.help_menu = tk.Menu(self.main_menu, tearoff=0)
        self.help_menu.add_command(label='About', command=None)
        self.main_menu.add_cascade(label='Help', menu=self.help_menu)

        self.parent.config(menu=self.main_menu)

    def setup(self):
        """ Initialize the build process """
        # Set Fixed size
        # self.parent.geometry("1100x600")
        # Restrict Resizability
        # self.parent.resizable(0, 0)
        # self.parent.attributes('-toolwindow', True)
        self.pack()
        self.create_window_menu()
        self.parent.iconbitmap('./media/images/logo.ico')
        self.display_child = DisplayFrame(self.parent, bg='yellow')
        self.display_child.pack(side='left', expand=True)
        self.navibar_child = NavibarFrame(self.parent, bg='red')
        self.navibar_child.pack(side='right', fill=tk.Y)

    def remove_display_child(self):
        """ Destroy the left frame """
        self.display_child.Destroy()

    def remove_navibar_child(self):
        """ Destroy the right frame """
        self.navibar_child.Destroy()

class CustomFrame(tk.Frame):

    _display_text = f"Enter the database name\n{Database._tables} : "

    def _entry_focusin(event, entry):
        if entry.get().startswith('Enter'):
            entry.delete(0, 'end')
            entry.insert(0, '')
            entry.config(bg='black', fg='green')

    def _entry_focusout(event, entry, text):
        if entry.get() == '':
            entry.insert(0, text)
            entry.config(bg='white', fg='grey')

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title = None
        self.options = {'padx': 5, 'pady': 5}
        self.set_window_title('MainFrame')

    def create_button(self, frame, text, **options):
        """ Generic Creation helper funciton """
        button = tk.Button(frame, text=text, **options)
        button.pack(**self.options)

    def create_entry(self, frame, text, **options):
        """ Generic Creation helper funciton """
        entry = tk.Entry(frame, text=text, **options)
        entry.pack(**self.options)

    def create_label(self, frame, text, **options):
        """ Generic Creation helper funciton """
        label = tk.Label(frame, text=text, **options)
        label.pack(**self.options)

    def set_window_title(self, title):
        """ Set the title text of the main window """
        self.winfo_toplevel().title(title)

class DisplayFrame(CustomFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        """ Initialize widgets in frame """
        self.create_label(self, 'Display', fg='green', bg='black')
        self.display_entry()
        self.output_entry()

    def display_entry(self):
        searchbox = tk.Entry(self, bd=1)
        searchbox.insert(0, CustomFrame._display_text)
        searchbox.bind('<FocusIn>', lambda event, i=searchbox: CustomFrame._entry_focusin(event, i))
        searchbox.bind('<FocusOut>', lambda event, j=searchbox, k=CustomFrame._display_text: CustomFrame._entry_focusout(event, j, k))
        searchbox.config(bg='white', fg='grey')
        searchbox.pack()

    def output_entry(self):
        entry = tk.Entry(self, bd=1)
        entry.bind('<FocusIn>', lambda event, i=entry: CustomFrame._entry_focusin(event, i))
        entry.bind('<FocusOut>', lambda event, j=entry, k='Lol': CustomFrame._entry_focusout(event, j, k))
        entry.config(bg='yellow', fg='grey')
        entry.pack()

class NavibarFrame(CustomFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        """ Initialize widgets in frame """
        self.create_button(self, text='Home', command=None)
        self.create_button(self, text='Quit', command=self.winfo_toplevel().quit)
        # for widget in self.winfo_children():
        #     widget.pack(**self.options)

if __name__ == '__main__':
    window = tk.Tk()
    app = MainFrame(window)
    app.mainloop()
