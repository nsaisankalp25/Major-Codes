# Encrypter in python
from tkinter import *
import random
def main():    
    rt = Tk()
    rt.geometry('500x400')
    rt.title("Encrypter")
    letters = 'abcdefghijklmnopqrstuvwxyz'

    def IndMixer() -> list:
        enLetters = []
        global ran_num
        ran_num = random.randint(1,26)
        print(ran_num)
        for i in letters:
            ind = letters.index(i) + ran_num
            if ind > 26: ind -= 26
            enLetters.append(letters[ind-1])
        return [ran_num] + enLetters
    newLets = IndMixer()

    def encrypter(txt, lets:list):
        print(txt)
        entxt = []
        ind = int(lets[0])
        del lets[0]
        for i in txt:
            if str(i).isalpha() == True:
                newind = int(lets.index(i.lower()) - ind)
                entxt.append(lets[newind])

            else:
                newind = int(lets.index("z") - ind)
                entxt.append(lets[newind])
        print(entxt := str(ran_num) + ''.join(entxt))

    def callfunc(a):
        ans_l = Label(rt, font = ("calibri", 15),
        text = f"Decrypted Text: {encrypter(txt = str(usr_txt_raw.get()),lets = IndMixer())}",).pack()

    user_label = Label(rt, text = "Enter text to get encrypted version",
    font = ("cambria", 15)).pack()

    usr_txt_raw = Entry(rt, font = ("helvetica", 20), width = 30)
    usr_txt_raw.pack()
    usr_txt_raw.bind("<Return>", callfunc)

    usr_sub = Button(rt, text = "Encrypt The text", font = ("cambria", 15),
    command = lambda: callfunc(None)).pack()
    rt.mainloop()


if __name__ == "__main__":
    main()