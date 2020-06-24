import tkinter as tk

class Tal:


    def __init__(self, root):
        self.root = root
        self.create_window_manage_side()
        self.create_aside()
        self.create_filter_side()
        self.create_main_side()
    
    def create_window_manage_side(self):
        self.window_manage_side = tk.Frame(self.root, bg='red', width=400, height=200)
        self.window_manage_side.grid(row=0, column=0)

    def create_aside(self):
        self.aside = tk.Frame(self.root, bg='green', width=400, height=800)
        self.aside.grid(row=1, column=0)

    def create_filter_side(self):
        self.filter_side = tk.Frame(self.root, bg='blue', width=1200, height=200)
        self.filter_side.grid(row=0, column=1)
    
    def create_main_side(self):
        self.main_side = tk.Frame(self.root, bg='purple', width=1200, height=800)
        self.main_side.grid(row=1, column=1)

root = tk.Tk()
root.title('Tal')
tal = Tal(root)

passstr = tk.StringVar()
passlen = tk.IntVar()
passlen.set(0)

root.geometry('1600x1000')

"""
tk.Label(root, text='Truc1', font='calibri 20 bold').pack()
tk.Label(root, text='Truc2').pack(pady=3)
tk.Entry(root, textvariable=passlen).pack(pady=3)
tk.Button(root, text='Truc3').pack(pady=7)
tk.Entry(root, textvariable=passstr).pack(pady=3)
tk.Button(root, text='Truc4').pack()
"""
root.mainloop()