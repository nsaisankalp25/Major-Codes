from itertools import cycle
from tkinter import *
from tkinter.font import BOLD
letters = 'abcdefghijklmnopqrstuvwxyz'

def decrypter(raw:str):
    numlst = "0123456789"
    if raw[0] in numlst and raw[1] in numlst:
        ind = int(raw[:2])
        raw = raw[2:]
    elif raw[0] in numlst and raw[1] not in numlst:
        ind = int(raw[0])
        raw = raw[1:]
    else:
        print("Something is wrong")
    print(raw)
    print(ind)
    print("_")
    nlst = []
    for i in raw:
        curLet = letters.index(i)
        for ii in cycle(letters):
            if letters.index(ii) == curLet:
                to_iter = curLet + ind 
                for num, iii in enumerate(cycle(letters)):
                    if num == to_iter:
                        nlst.append(iii)
                        break
                break
        while curLet != 0:
            curLet -= 1
    print("".join(nlst))
    return ("".join(nlst)).replace('z', ' ')
 

def callfunc(a):
    ans_l = Label(rt, text = f"Decrypted Text: {decrypter(user_entry.get())}", fg = '#0049FF',
    bg = bgc,width = 30, height = 0,font = ("calibri", 20, BOLD))
    ans_l.place(x = 60, y = 180)
rt = Tk()
strvar = StringVar()
rt.title("Python Decrypter")
rt.geometry("800x400")
bgc = '#FCFFDD'
rt.config(bg = bgc)
info_l = Label(rt, text = "Decrypter is an application used to Decrypt Encrypted Text", 
    fg = '#FF6400', bg = bgc, font = ("montserrat", 18)).place(x = 20, y = 10)
enter_txt_l = Label(rt, text = "Enter the Encrypted text: ", 
    fg = '#002DBA', bg = bgc, font = ("cambria", 16)).place(x = 10, y = 80)
user_entry = Entry(rt, font = ("cascadia mono", 16), fg = '#FF00D8', 
    bg = 'white')
user_entry.bind("<Return>", callfunc)
user_entry.place(x = 250, y = 80, height = 35, width = 400)

sub_b = Button(rt, text = "Decrypt Text", fg = '#009F29', bg = bgc,
    font = ('consolas', 15, BOLD), activebackground = bgc, command = lambda: callfunc(None),
    activeforeground = "#009F29").place(x = 100, y = 120)

rt.mainloop()