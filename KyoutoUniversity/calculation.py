import tkinter as tk

current_number = 0
first_term = 0
second_term = 0
result = 0

def do_plus():
    global current_number
    global first_term

    first_term = current_number
    current_number = 0

def do_equal():
    global second_term
    global result
    global current_number
    second_term = current_number
    result = first_term + second_term
    current_number = 0

class MyFrame(tk.Frame):
    def __init__(self, master: None):
        super().__init__(master)

        b1 = tk.Button(self,text="1", command=lambda:self.key(1))
        b2 = tk.Button(self,text='2', command=lambda:self.key(2))
        b3 = tk.Button(self,text='3', command=lambda:self.key(3))
        b4 = tk.Button(self,text='4', command=lambda:self.key(4))
        b5 = tk.Button(self,text='5', command=lambda:self.key(5))
        b6 = tk.Button(self,text='6', command=lambda:self.key(6))
        b7 = tk.Button(self,text='7', command=lambda:self.key(7))
        b8 = tk.Button(self,text='8', command=lambda:self.key(8))
        b9 = tk.Button(self,text='9', command=lambda:self.key(9))
        b0 = tk.Button(self,text='0', command=lambda:self.key(0))
        bc = tk.Button(self,text='C', command=self.clear)
        bp = tk.Button(self,text='+', command=self.plus)
        be = tk.Button(self,text="=", command=self.equal)

        b1.grid(row=3,column=0)
        b2.grid(row=3,column=1)
        b3.grid(row=3,column=2)
        b4.grid(row=2,column=0)
        b5.grid(row=2,column=1)
        b6.grid(row=2,column=2)
        b7.grid(row=1,column=0)
        b8.grid(row=1,column=1)
        b9.grid(row=1,column=2)
        b0.grid(row=4,column=0)
        bc.grid(row=1,column=3)
        be.grid(row=4,column=3)
        bp.grid(row=2,column=3)

        self.e = tk.Entry(self)
        self.e.grid(row=0, column=0, columnspan=4)

    def key(self, n):
        global current_number
        current_number = current_number * 10 + n
        self.show_number(current_number)

    def clear(self):
        global current_number
        current_number = 0
        self.show_number(current_number)

    def plus(self):
        do_plus()
        self.show_number(current_number)

    def equal(self):
        do_equal()
        self.show_number(result)

    def show_number(self,num):
        self.e.delete(0,tk.END)
        self.e.insert(0,str(num))

root = tk.Tk()
f = MyFrame(root)
f.pack()
root.mainloop()