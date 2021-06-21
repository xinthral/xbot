"""
Interactive SQL Window
TKinter GUI allowing interaction between user and database
"""
import tkinter as tk
from xsql import Database

class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.geometry("800x600")
        self.title = 'Console'
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Initiliaze instance methods
        self.create_window_menu()
        self.create_framework()

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
        self.file_menu.add_command(label='Exit', command=root.quit)
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

    def create_framework(self):
        """ Build main window frame layout """
        span = 20
        self.navibar_frame = NaviBarFrame(self)
        self.display_frame = DisplayFrame(self)
        self.console_frame = ConsoleFrame(self)
        self.style_framework()

    def set_window_title(self, title):
        """ Set the title text of the main window """
        self.winfo_toplevel().title(title)

    def style_framework(self):
        """ Apply style to the framework """
        self.set_window_title('Console')
        self.console_frame.config(bg='red')
        self.display_frame.config(bg='white')
        self.navibar_frame.config(bg='blue')

class NaviBarFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=tk.RIGHT, fill=tk.Y)
        self.create_widgets()

    def create_button_home(self):
        """ Create Button """
        self.go_home = tk.Button(self, fg='green')
        self.go_home['text'] = 'Go Home'
        self.go_home['command'] = self.pressed_button_home
        self.go_home.pack()

    def create_button_quit(self):
        """ Create Button """
        self.quit = tk.Button(self, text='Exit', fg='red', command=self.winfo_toplevel().destroy)
        self.quit.pack()

    def create_widgets(self):
        """ Build All Widgets """
        self.create_button_home()
        self.create_button_quit()

    def pressed_button_home(self):
        """ Execution of button event """
        print('Home Button Pressed!')
        self.set_window_title('Home')

    def set_window_title(self, title):
        """ Set the title text of the main window """
        # self.winfo_toplevel().title(title)
        self.parent.set_window_title(title)

class DisplayFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.output_box = None
        self.scrollbar = None
        self.pack(side=tk.TOP, fill=tk.Y)
        self.create_widgets()

    def create_button_search(self):
        """ Create Button """
        self.go_search = tk.Button(self, fg='green')
        self.go_search['text'] = 'Search'
        self.go_search['command'] = self.pressed_button_search
        self.go_search.pack()

    def create_entrybox(self):
        """ Create entry box for text input """
        self.user_search = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.user_search)
        self.entry.pack()

    def create_label(self):
        """ Create a label for the console window """
        self.entry_label = tk.Label(self, text='Console: ')
        self.entry_label.pack(side=tk.TOP)

    def create_scrollbar(self):
        """ Create vertical scrollbar """
        if self.scrollbar != None: self.scrollbar.pack_forget()
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_textbox(self, output=[]):
        """ Create Textbox area """
        self.create_scrollbar()
        if self.output_box != None: self.output_box.pack_forget()
        self.output_box = tk.Listbox(self, bg='black', fg='green', width=25, height=10, yscrollcommand=self.scrollbar.set)
        for i in range(len(output)):
            self.output_box.insert('end', f"{i+1}: {output[i]}")
        self.output_box.pack(fill=tk.X)

    def create_widgets(self):
        """ Build All Widgets """
        self.create_label()
        self.create_entrybox()
        self.create_button_search()

    def pressed_button_search(self):
        """ Execution of button event """
        print(f"Searchin for {self.user_search.get()}!")
        self.set_window_title('Search')

    def set_window_title(self, title):
        """ Set the title text of the main window """
        self.winfo_toplevel().title(title)

class ConsoleFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.scrollbar = None
        self.output_box = None
        self.pack(side=tk.BOTTOM, fill=tk.X)
        self.create_widgets()

    def create_scrollbar(self):
        """ Create vertical scrollbar """
        if self.scrollbar != None: self.scrollbar.pack_forget()
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_textbox(self, output=[]):
        """ Create Textbox area """
        self.create_scrollbar()
        if self.output_box != None: self.output_box.pack_forget()
        self.output_box = tk.Listbox(self, bg='black', fg='green', width=25, height=10, yscrollcommand=self.scrollbar.set)
        for i in range(len(output)):
            self.output_box.insert('end', f"{i+1}: {output[i]}")
        self.output_box.pack(fill=tk.X)

    def create_widgets(self):
        """ Build All Widgets """
        self.create_textbox()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(parent=root)
    app.mainloop()
