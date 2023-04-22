import random
import smtplib
import statistics
import time
import tkinter
import turtle as tr
import webbrowser
import datetime
from email.message import EmailMessage
from functools import lru_cache
from random import shuffle
from tkinter import *
from tkinter import Menu, filedialog, font, messagebox, ttk
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *
from tkinter.ttk import Combobox
import os
import googlesearch
from PIL import Image, ImageTk
from selenium import webdriver
from tkcalendar import Calendar

mc = '#E5FFD6'
rt = tkinter.Tk()
rt.title('Super System UI')
rt.geometry('1200x700') 
rt.minsize(1200, 700)
rt.maxsize(1200, 700)

try:
    rocka = Image.open(r"reqs\rock.png")
    rock_img = ImageTk.PhotoImage(rocka)

    scis = Image.open(r"reqs\scissors.png")
    sci_img = ImageTk.PhotoImage(scis)

    papers = Image.open(r"reqs\paper.png")
    paper_img = ImageTk.PhotoImage(papers)

    gmail_img = PhotoImage(file = r'reqs\gmail.png')
    gmail_img = gmail_img.subsample(7,7)

    cal_img = PhotoImage(file = r'reqs\cal.png')
    cal_img = cal_img.subsample(6,6)

    options_img = PhotoImage(file = r"reqs\options.png")
    options_img = options_img.subsample(16,16)

    games_img = PhotoImage(file = r"reqs\games.png")
    games_img = games_img.subsample(16,16)

    doc_img =  PhotoImage(file = r'reqs\doc.png')
    doc_img = doc_img.subsample(16,16)

    ss_img = PhotoImage(file = r'reqs\ss.png')
    ss_img = ss_img.subsample(2,2)

    settings_img = PhotoImage(file = r'reqs\settings.png')
    settings_img = settings_img.subsample(16,16)

    g_img = PhotoImage(file = r'reqs\google_img.png')
    g_img = g_img.subsample(16,16)

    time_file = r"reqs\clock.png"
    time_img = PhotoImage(file = time_file)
    time_img = time_img.subsample(16,16)
    hand_links = [
    r"reqs\one.png",
    r"reqs\two.png",
    r"reqs\three.png",
    r"reqs\four.png",
    r"reqs\five.png",
    r"reqs\six.png"
    ]

    one_img = PhotoImage(file = hand_links[0])
    one_img = one_img.subsample(7,7)

    two_img = PhotoImage(file = hand_links[1])
    two_img = two_img.subsample(7,7)

    three_img = PhotoImage(file = hand_links[2])
    three_img = three_img.subsample(7,7)

    four_img = PhotoImage(file = hand_links[3])
    four_img = four_img.subsample(7,7)

    five_img = PhotoImage(file = hand_links[4])
    five_img = five_img.subsample(7,7)

    six_img = PhotoImage(file = hand_links[5])
    six_img = six_img.subsample(7,7)

    oe_imgs = [one_img, two_img, three_img, four_img, five_img, six_img]
except:
    rocka = Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\rock.png")
    rock_img = ImageTk.PhotoImage(rocka)

    scis = Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\scissors.png")
    sci_img = ImageTk.PhotoImage(scis)

    papers = Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\paper.png")
    paper_img = ImageTk.PhotoImage(papers)

    gmail_img = PhotoImage(file = r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\gmail.png')
    gmail_img = gmail_img.subsample(7,7)

    cal_img = PhotoImage(file = r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\cal.png')
    cal_img = cal_img.subsample(6,6)

    options_img = PhotoImage(file = r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\options.png")
    options_img = options_img.subsample(16,16)

    games_img = PhotoImage(file = r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\games.png")
    games_img = games_img.subsample(16,16)

    doc_img =  PhotoImage(file = r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\doc.png')
    doc_img = doc_img.subsample(16,16)

    ss_img = PhotoImage(file = r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\ss.png')
    ss_img = ss_img.subsample(2,2)

    settings_img = PhotoImage(file = r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\settings.png')
    settings_img = settings_img.subsample(16,16)

    g_img = PhotoImage(file = r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\google_img.png')
    g_img = g_img.subsample(16,16)

    time_file = r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\clock.png"
    time_img = PhotoImage(file = time_file)
    time_img = time_img.subsample(16,16)

    hand_links = [
    r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\one.png",
    r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\two.png",
    r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\three.png",
    r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\four.png",
    r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\five.png",
    r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\six.png"
    ]

    one_img = PhotoImage(file = hand_links[0])
    one_img = one_img.subsample(7,7)

    two_img = PhotoImage(file = hand_links[1])
    two_img = two_img.subsample(7,7)

    three_img = PhotoImage(file = hand_links[2])
    three_img = three_img.subsample(7,7)

    four_img = PhotoImage(file = hand_links[3])
    four_img = four_img.subsample(7,7)

    five_img = PhotoImage(file = hand_links[4])
    five_img = five_img.subsample(7,7)

    six_img = PhotoImage(file = hand_links[5])
    six_img = six_img.subsample(7,7)

    oe_imgs = [one_img, two_img, three_img, four_img, five_img, six_img]

def main_function():
    rt.config(cursor = 'plus', bg = mc)
    for widgets in rt.winfo_children():
        widgets.destroy()
    button_font = ('segoe ui', 13)
    main = Frame(rt,width = 1200,
    height = 650,cursor = "plus", bg = mc, border = 12)
    main.grid(row = 0, column = 0)
    taskbar = Frame(rt,bd = 2, bg = "#F0FF99", cursor = 'plus',
    width = 1200, height = 50)
    taskbar.grid(row = 1, column = 0)
    ss_l = Label(main, text = "Super System  ", image = ss_img, compound = RIGHT, font = ('montserrat', 30), bg = mc)
    ss_l.place(x = 320, y = 200)

    def gmail_def():
        button_gmail.configure(bg = '#4FFFA1')
        button_calculator.configure(bg = '#f0f0f0')
        options_b.configure(bg = '#f0f0f0')
        google_b.config(bg = '#f0f0f0')
        time_b.config(bg = '#f0f0f0')
        big_gmail_img = PhotoImage(file = 'gmail.png')
        big_gmail_img = big_gmail_img.subsample(4,4)
        for widgets in main.winfo_children():
            widgets.destroy()
        opened = Label(main, image = gmail_img)
        opened.place(x = 0, y = 0)
        file = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\info.txt')
        info = []
        for i in file:
            info.append(i)
        email = info[0]
        password = info[1]
        password.lstrip()
        def send_mail():
            to = to_e.get()
            subject = subject_e.get()
            body = body_e.get(1.0, END)
            msg = EmailMessage()    
            msg['Subject'] = subject
            msg['From'] = email
            msg['To'] = to
            msg.set_content(body)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email, password).send_message(msg)
            Mail_sent = Label(main, text = "Mail send successfully.", 
            font = ('calibri', 12), fg = 'blue', bg = mc)
            Mail_sent.place(x = 300, y = 325)
            to_e.delete(0, END)
            subject_e.delete(0, END)
            body_e.delete("1.0","end")        
        
        to_l = Label(main, text = 'To: ', font = ('consolas', 14), bg = mc, fg = 'black')
        to_l.place(x = 100, y = 0)
        to_e = Entry(main, font = ('consolas', 14), width  = 50, fg = 'black')
        to_e.place(x = 200, y = 0)

        subject_l = Label(main, text = 'Subject: ', font = ('consolas', 14), bg = mc
        , fg = 'black')
        subject_l.place(x = 100, y = 36)
        subject_e = Entry(main, font = ('consolas', 14), width  = 50, fg = 'black')
        subject_e.place(x = 200, y = 36)

        body_l = Label(main, text = 'Body: ', font = ('consolas', 14), bg = mc
        , fg = 'black')
        body_l.place(x = 100, y = 70)
        body_e = Text(main, font = ('montserrat', 14), width  = 39, height = 10
        , fg = 'black')
        body_e.place(x = 200, y = 70)

        send_b = Button(main, text = "Send Mail", fg = 'red', 
        font = ('quicksand', 12), command = send_mail)
        send_b.place(x = 200, y = 325)

    def cal_def():
        button_gmail.configure(bg = '#f0f0f0')
        button_calculator.configure(bg = '#4FFFA1')
        options_b.configure(bg = '#f0f0f0')
        google_b.config(bg = '#f0f0f0')
        time_b.config(bg = '#f0f0f0')
        for widgets in main.winfo_children():
            widgets.destroy()
        opened = Label(main, image = cal_img)
        opened.place(x = 0, y = 0)
        numbers_l = Label(main, text = "Enter the numbers: ",font = ('consolas', 13), bg = mc
        , fg = 'black')
        numbers_l.place(x = 100, y = 20)
        numbers_e = Entry(main, font = ('consolas', 14), width = 30, fg = 'black')
        numbers_e.place(x = 270, y = 20)
        numbers_float = []
        out_l = Label(main, text = '', font = ('calibri', 14), bg = mc, fg = 'black')
        out_l.place(x = 500, y = 200)
        def main_def():
            numbers = numbers_e.get()
            numbers = numbers.split(',')    
            try:
                for i in numbers:
                    numbers_float.append(float(i))
            except:
                print('didnt enter numbers')

        def out():
            numbers_e.delete(0, END)
            numbers_float.clear()

        def add_def():
            main_def()
            num = 0
            for i in numbers_float:
                num = i + num
            print(num)
            out_l.configure(text = f"Sum: {num}")
            out()
                    

        def sub_def():
            main_def()
            num = None
            for i in numbers_float:
                if num == None:
                    num = numbers_float[0]
                else:
                    num = num - i
            out_l.configure(text = f"Difference: {num}")
            out()

        def mul_def():
            main_def()
            num = None
            for i in numbers_float:
                if num == None:
                    num = numbers_float[0]
                else:
                    num = num * i
            print(num)
            out_l.configure(text = f"Product: {num}")
            out()

        def div_def():
            main_def()
            num = None
            for i in numbers_float:
                if num == None:
                    num = numbers_float[0]
                else:
                    num = num/i
            print(num)
            out_l.configure(text = f"Quotient: {num}")
            out()

        def power_def():
            main_def()
            num_1 = numbers_float[0]
            num_2 = numbers_float[1]
            out_l.configure(text = f"Result: {num_1**num_2}")
            out()

        def root_def():
            main_def()
            num1 = numbers_float[0]
            num2 = numbers_float[1]
            ans = num1**(1/num2)
            out_l.config(text = f"Result: {ans}")
            out()

        def mean_def():
            main_def()
            num = len(numbers_float)
            sum_nums = 0
            for i in numbers_float:
                sum_nums = sum_nums + i 
            ans = sum_nums/num
            out_l.config(text = f"Mean: {ans}")
            out()

        def med_def():
            main_def()
            out_l.config(text = f'Median: {statistics.median(numbers_float)}')
            out()

        def mode_def():
            main_def()
            out_l.config(text = f"Mode: {statistics.mode(numbers_float)}")

        add_b = Button(main, text = "Add", font = ('calibri', 13), bg = mc, fg = 'blue', command = add_def)
        add_b.place(x = 200, y =  80)

        sub_b = Button(main, text = "Subtract", font = ('calibri', 13), bg = mc, fg = 'blue', command = sub_def)
        sub_b.place(x = 260, y =  80)

        mul_b = Button(main, text = "Multiply", font = ('calibri', 13), bg = mc, fg = 'blue', command = mul_def)
        mul_b.place(x = 350, y =  80)

        div_b = Button(main, text = "Divide", font = ('calibri', 13), bg = mc, fg = 'blue', command = div_def)
        div_b.place(x = 200, y =  140)

        pow_b = Button(main, text = "Power", font = ('calibri', 13), bg = mc, fg = 'blue', command = power_def)
        pow_b.place(x = 265, y =  140)

        root_b = Button(main, text = "Root", font = ('calibri', 13), bg = mc, fg = 'blue', command = root_def)
        root_b.place(x = 350, y =  140)

        mean_b = Button(main, text = "Mean", font = ('calibri', 13), bg = mc, fg = 'blue', command = mean_def)
        mean_b.place(x = 200, y =  200)

        median_b = Button(main, text = "Median", font = ('calibri', 13), bg = mc, fg = 'blue', command = mean_def)
        median_b.place(x = 260, y =  200)    
        
        mode_b = Button(main, text = "Mode", font = ('calibri', 13), bg = mc, fg = 'blue', command = mode_def)
        mode_b.place(x = 350, y =  200)

    def close_def():
        rt.destroy()

    def options_def():
        button_gmail.configure(bg = '#f0f0f0')
        button_calculator.configure(bg = '#f0f0f0')
        options_b.configure(bg = '#4FFFA1')
        google_b.config(bg = '#f0f0f0')
        time_b.config(bg = '#f0f0f0')
        for widgets in main.winfo_children():
            widgets.destroy()    

        def rps_def():
            for widgets in main.winfo_children():
                widgets.destroy()
            point_l = Label(main, text = '', foreground = 'red', font = ('quicksand', 14))
            point_l.place(x = 575, y = 350)

            def rockdef():
                sam_l = Label(main, text = '<- You ', image = rock_img, compound = LEFT,
                fg = 'black')
                sam_l.place(x = 425, y = 200)
                r_img = random.randint(1,3)
                if r_img == 1:
                    rock_l = Label(main, image = rock_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    rock_l.place(x = 625, y = 200)
                    point_l.config(text = "It's a Tie")

                if r_img == 3:
                    sci_l = Label(main, image = sci_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    sci_l.place(x = 625, y = 200)
                    print('Gets 1 point')
                    point_l.config(text = 'You Won')
                    

                if r_img == 2:
                    paper_l = Label(main, image = paper_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    paper_l.place(x = 625, y = 200)
                    print('loses 1 point')
                    point_l.config(text = 'You Lost')

            def scidef():
                sam_l = Label(main, text = '<- You ', image = sci_img, compound = LEFT)
                sam_l.place(x = 425, y = 200)
                r_img = random.randint(1,3)
                if r_img == 1:
                    rock_l = Label(main, image = sci_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    rock_l.place(x = 625, y = 200)
                    print('Gets 1 point')
                    point_l.config(text = 'Its a Tie')

                if r_img == 3:
                    sci_l = Label(main, image = rock_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    sci_l.place(x = 625, y = 200)   
                    point_l.config(text = "You Lost")
                    

                if r_img == 2:
                    paper_l = Label(main, image = paper_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    paper_l.place(x = 625, y = 200)
                    point_l.config(text = "You Win")

            def paperdef():
                sam_l = Label(main, text = '<- You ', image = paper_img, compound = LEFT)
                sam_l.place(x = 425, y = 200)
                r_img = random.randint(1,3)
                if r_img == 1:
                    rock_l = Label(main, image = rock_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    rock_l.place(x = 625, y = 200)
                    point_l.config(text = 'You Won')

                if r_img == 3:
                    sci_l = Label(main, image = sci_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    sci_l.place(x = 625, y = 200)
                    point_l.config(text = 'You lost')

                if r_img == 2:
                    paper_l = Label(main, image = paper_img, compound = RIGHT, text = 'AI ->'
                    , fg = 'black')
                    paper_l.place(x = 625, y = 200)
                    point_l.config(text = "Its a Tie")
                
            rock_b = Button(main, image = rock_img, command = rockdef, fg = 'black')
            rock_b.place(x = 400, y = 400)
            paper_b = Button(main, image = paper_img, command = paperdef, fg = 'black')
            paper_b.place(x = 550, y = 400)
            sci_b = Button(main, image = sci_img, command = scidef, fg = 'black')
            sci_b.place(x = 700, y = 400)

        def ssdoc():
            for widgets in main.winfo_children():
                widgets.destroy()
            # SSDOC = Super System Document
            doc_frame = Frame(main)
            doc_frame.place(x = 300, y = 50)

            scroll_y = Scrollbar(doc_frame)
            scroll_y.pack(side = RIGHT, fill = Y)

            scroll_x = Scrollbar(doc_frame, orient = HORIZONTAL)
            scroll_x.pack(side = BOTTOM, fill = X)

            user = Text(doc_frame, width = 54, height = 19, font = ('courier', 20),fg = 'black', bg = '#FDFFD8', yscrollcommand = scroll_y.set, xscrollcommand = scroll_x.set)
            user.pack()

            scroll_y.config(command = user.yview)
            scroll_x.config(command = user.xview)

            def save_file():
                filename = filedialog.asksaveasfilename(title = 'Save File',
                filetypes = (("all files","*.*"), ('python files', '*.py')))
                file = open(filename, 'w')
                file.write(user.get(1.0, END))
                file.close()

            def open_file():
                def err_def():
                    try:
                        print(1)
                        filename = filedialog.askopenfilename(title = 'Open File', 
                        filetypes = (('all files', '*.*'), ("text files", "*.txt")))
                        file = open(filename, 'r')
                        print(11)
                        i = file.read()
                        print(2)
                        user.delete('1.0', "end")
                        print('here')
                        user.insert(INSERT, i)
                        print(3)
                    except:
                        err = messagebox.askretrycancel('Error', """Unable to open the file selected 
                                                    sorry for the inconvenience """)
                        if err == True:
                            err_def()
                    
                err_def()                

            def config_def():
                font_var = StringVar()
                color_var = StringVar()
                bg_var = StringVar()
                win = Toplevel(rt)
                win.config(cursor = 'target')
                win.title("Configure SS DOCs")
                win.geometry("500x200")
                win.minsize(500,200)
                win.maxsize(500,200)
                colors_tuple = ('red', 'green', 'yellow', 'orange', 'blue', 'cyan', 'purple', 'brown', 'magenta', 'black', 'white')
                def change():
                    try: 
                        size = int(size_e.get())    
                        color = color_var.get()
                        bg_col = bg_var.get()       
                        user.config(font = (font_var.get(), size), fg = color, bg = bg_col)
                        win.destroy()
                    except:
                        showsmg = messagebox.askokcancel("Error", "Sorry, Unable to change the font/font size")
                        if showsmg == 1:
                            win.destroy()
                        else:
                            win.destroy()
                    

                font_size_l = Label(win, text = 'Font Size')
                font_size_l.grid(row = 0, column = 0)
                size_e = Entry(win)
                size_e.grid(row = 1, column = 0)
                font_type_l = Label(win, text = "Font Type")
                font_type_l.grid(row = 0, column = 1) 
                font_com = ttk.Combobox(win, width = 27, textvariable = font_var)
                font_com['values'] = font.families()
                font_com.grid(row = 1, column = 1)

                font_color_l = Label(win, text = "Font Color")
                font_color_l.grid(row = 2, column = 0)
                font_color = Combobox(win, width = 27,textvariable = color_var)
                font_color.grid(row = 2, column = 1)
                font_color['values'] = colors_tuple
                bg_color_l = Label(win, text = 'Background Color')
                bg_color_l.grid(row = 3, column = 0)
                bg_color = Combobox(win, width = 27,textvariable = bg_var)
                bg_color.grid(row = 3, column = 1)
                bg_color['values'] = colors_tuple
                change_b = Button(win, text = "Apply and Close", command = change)
                change_b.grid(row = 10, column = 0)

            save_b = ttk.Button(main, text = "Save File", command = save_file)
            save_b.place(x = 310, y = 18)
            open_b = ttk.Button(main, text = "Open File", command = open_file)
            open_b.place(x = 400, y = 18)
            config_b = ttk.Button(main, text = "Configure", command = config_def)
            config_b.place(x = 480, y = 18)
                
        def contacts_def():
            for widgets in main.winfo_children():
                widgets.destroy()
            def add_def():
                def add_user_def():
                    name = name_ee.get()
                    name_ee.delete(0, END)
                    num = phno_ee.get()
                    phno_ee.delete(0, END)
                    address = address_ee.get()
                    address_ee.delete(0, END)
                    job = job_ee.get()
                    job_ee.delete(0, END)
                    nickname = nickname_ee.get()
                    nickname_ee.delete(0, END)
                    done = Label(main)
                    done.place(x = 600, y = 290)
                    if address == '':
                        address = 'None'
                    else:
                        pass
                    if job == '':
                        job = 'None'
                    else:
                        pass
                    if name == '' or num == '':
                        alert = messagebox.askokcancel("Invalid", "Reqesting to fill in all the fields(*)")
                        done.config(text = '')
                    else:
                        pass
                    if nickname == '':
                        nickname = None
                    else:
                        pass  
                    
                    char = '!@#$%^&\/*()[];"\',.<>?:+_=-`~'
                    if name in char or address in char or num in char or job in char :
                        alert = messagebox.askokcancel("Invalid", 
                        "Special charecters are not allowed")
                        
                    else:
                        with open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\contacts.txt', 'a') as file:
                            file.write(f"{name}, {num}, ({address}), {job}\n")
                            file.close()
                            done.config(text = "Successfully added contact.")

                    
                global name_ll, name_ee, address_ee, job_ee, nickname_ee
                global phno_ee, phno_ll, address_ll, job_ll, nickname_ll
                global add_user_b
                name_ll = Label(main, text = 'Name: *', bg = mc, 
                font = ('consolas', 14), fg = 'black')
                name_ee = Entry(main, bg = mc, font = ('ubuntu mono', 18), fg = 'black')
                name_ll.place(x = 400, y = 50)
                name_ee.place(x = 600, y = 50)
                phno_ll = Label(main, text = 'Contact Number: *', bg = mc,
                font = ('consolas', 14), fg = 'black')
                phno_ll.place(x = 400, y = 100)
                phno_ee = Entry(main, bg = mc, font = ('ubuntu mono', 18), fg = 'black')
                phno_ee.place(x = 600, y = 100)

                address_ll = Label(main, text = 'Address: ', font = ('consolas', 14)
                , bg = mc, fg = 'black')
                address_ll.place(x = 400, y = 150)
                address_ee = Entry(main, bg = mc, font = ('ubuntu mono', 18), fg = 'black')
                address_ee.place(x = 600, y = 150)
                nickname_ll = Label(main, text = 'Nickname: ', font = ('consolas', 14),
                bg = mc, fg = 'black')
                nickname_ll.place(x = 400, y = 200)
                nickname_ee = Entry(main, font = ('ubuntu mono', 18), fg = 'black')
                nickname_ee.place(x = 600, y = 200)
                job_ll = Label(main, text = 'Profession: ', font = ('consolas', 14)
                , bg = mc, fg = 'black')
                job_ll.place(x = 400, y = 250)
                job_ee = Entry(main, bg = mc, font = ('ubuntu mono', 18), fg = 'black')
                job_ee.place(x = 600, y = 250)

                add_user_b = ttk.Button(main, text = 'Add Contact', command = add_user_def)
                add_user_b.place(x = 500, y = 290)
                try:
                    rem_user_b.destroy()
                except:
                    pass

            def remove_def():
                def remove_user_def():
                    done = Label(main)
                    done.place(x = 600, y = 290)
                    name = name_e.get()
                    name_e.delete(0, END)
                    phno = phno_e.get()
                    phno_e.delete(0, END)
                    if name == '' or phno == '':
                        done.config(text = "Name and Ph.No should be entered")
                    else:
                        file = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\contacts.txt', 'r')
                        file_read = file.readlines()
                        # {name}, {num}, {address}, {job}\n
                        file.close()
                        into_file = []
                        for i in file_read:
                            i = i.strip()
                            print(i)
                            try:
                                i = i.split(',')
                            except:   
                                pass
                            print(i)
                            if name.strip() == i[0].strip() and phno.strip() == i[1].strip():
                                print('out of the list')
                            else:
                                into_file.append(i)
                            
                        print(into_file)
                        file_to = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\contacts.txt', 'w')
                        for i in into_file:
                            print(i)
                            for a in i:
                                file_to.write(a + ',')
                            file_to.write('\n')
                            

                name_l = Label(main, text = 'Name: *', bg = mc,
                        font = ('consolas', 14), fg = 'black')
                name_e = Entry(main, bg = mc, font = ('ubuntu mono', 18), fg = 'black')
                name_l.place(x = 400, y = 50)
                name_e.place(x = 600, y = 50)
                phno_l = Label(main, text = 'Contact Number: *', bg = mc,
                font = ('consolas', 14), fg = 'black')
                phno_l.place(x = 400, y = 100)
                phno_e = Entry(main, bg = mc, font = ('ubuntu mono', 18), fg = 'black')
                phno_e.place(x = 600, y = 100)
                try:
                    add_user_b.destroy()
                    name_ee.destroy()
                    address_ee.destroy()
                    job_ee.destroy()
                    nickname_ee.destroy()
                    phno_ee.destroy()
                    name_ll.destroy()
                    phno_ll.destroy()
                    address_ll.destroy()
                    job_ll.destroy()
                    nickname_ll.destroy()
                except:
                    pass
                global rem_user_b        
                rem_user_b = ttk.Button(main, text = 'Remove Contact', command = remove_user_def)
                rem_user_b.place(x = 500, y = 290)

            def view_def():
                for widgets in main.winfo_children():
                    widgets.destroy()
                contacts_view_t = Text(main, height = 20, width = 80, 
                font = ('segoe ui', 14), fg = 'blue', highlightbackground = '#FFA8FB')
                contacts_view_t.place(x = 200, y = 10)
                file = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\contacts.txt', 'r')
                file_read = file.readlines()
                # {name}, {num}, {address}, {job}\n
                file.close()
                for i in file_read:
                    i = i.strip()
                    try:
                        i = i.split(',')
                    except:   
                        pass
                    print(i)
                    contacts_view_t.insert(INSERT, 
                    f'Name: {i[0]} | Ph.Num: {i[1]} | Address: {i[2]} | Profession: {i[3]}\n')
                    contacts_view_t.insert(INSERT, "------------------------ \n")
                
                contacts_view_t.config(state = 'disabled')

            style = ('calibri', 13)
            add_b = Button(main, text = "Add Contact", font = style, bg = mc,
            activebackground = mc, command = add_def, fg = 'black')
            remove_b = Button(main, text = "Remove Contacts", font = style, bg = mc,
            activebackground = mc, command = remove_def, fg = 'black')
            view_b = Button(main, text = "View Contacts", font = style, bg = mc, 
            activebackground = mc, command = view_def, fg = 'black')
            view_b.place(x = 750, y = 10)
            add_b.place(x = 400, y = 10)
            remove_b.place(x = 575, y = 10)

        def settings_def():
            for widgets in main.winfo_children():
                widgets.destroy()
            def color_change():
                colors = askcolor(title = 'Theme Color Chooser')
                global mc
                mc = colors[1]
                r,g,b = colors[0]
                co_num = [r,g,b]
                co_num = sorted(co_num)
                print(co_num)
            
                def change_color(color, bg_color):
                    for wdg in main.children:
                        wdg = main.nametowidget(wdg)
                        if isinstance(wdg, Label):
                            wdg.config(fg=color)
                            wdg.config(bg = bg_color)
                        elif isinstance(wdg, Entry):
                            wdg.config(fg=color)
                            wdg.config(bg = bg_color)
                        elif isinstance(wdg, Button):
                            wdg.config(fg=color)
                            wdg.config(bg = bg_color)
                        elif isinstance(wdg, Text):
                            wdg.config(fg = color)
                            wdg.config(bg = bg_color)
                        else:
                            pass
                if co_num[0] + co_num[1] < 202:
                    change_color('#67F6FF', mc)

                else:
                    change_color('black', mc)
                rt.config(bg = colors[1])
                main.config(bg = colors[1])

            def change_log():
                for widgets in main.winfo_children():
                    widgets.destroy()

                version = '1.0'
                admin_log = f"""Official Version: {version} 
                            Super System Updates and content made by Sai
                            Change:
                                Updates:
                                    Callender
                                    Travel App

                                New Features:
                                    Google
                                     

                            Future Updates: 
                                Update 1.1.0 - Graphs and geometry"""
                                
                log_t = Text(main, width = 80, height = 25, font = ('roboto mono', 15))
                log_t.place(x = 200, y = 100)
                log_t.insert(INSERT, admin_log)
                log_t.config(state = 'disabled')


            mc_config = Button(main, text = 'Change Color Theme',
            bg = mc, activebackground = mc, font = ('abadi', 10), command = 
            color_change, fg = 'black')
            mc_config.place(x = 500, y = 200)

            mc_config = Button(main, text = 'View-Change-Log',
            bg = mc, activebackground = mc, font = ('abadi', 10), command = 
            change_log, fg = 'black')
            mc_config.place(x = 500, y = 240)

        def math_stuff():
            for widgets in main.winfo_children():
                widgets.destroy()

            def math_cal_def():
                
                for widgets in main.winfo_children():
                    widgets.destroy()
                operations = ['+', '-', '*', '/']
                shuffle(operations)
                nums = []
                num_total = random.randint(2, 8)
                global ans
                for i in range(num_total):
                    i = random.randint(1, 100)
                    nums.append(i)
                if len(nums) == 2:
                    ques_show = f"{nums[0]} {operations[0]} {nums[1]}" 
                    ans = eval(ques_show)
                
                elif len(nums) == 3:
                    ques_show = f"{nums[0]} {operations[0]} {nums[1]} {operations[1]} {nums[2]}"
                    ans = eval(ques_show)

                elif len(nums) == 4:
                    ques_show = f"{nums[0]} {operations[0]} {nums[1]} {operations[1]} {nums[2]} {operations[2]} {nums[3]}"           
                    ans = eval(ques_show)

                elif len(nums) == 5:
                    ques_show = f"{nums[0]} {operations[0]} {nums[1]} {operations[1]} {nums[2]} {operations[2]} {nums[3]} {operations[3]} {nums[4]}"
                    ans = eval(ques_show)

                elif len(nums) == 6:
                    ques_show = f"{nums[0]} {operations[0]} {nums[1]} {operations[1]} {nums[2]} {operations[2]} {nums[3]} {operations[3]} {nums[4]} {operations[2]} {nums[5]}"           
                    ans = eval(ques_show)

                elif len(nums) == 7:
                    ques_show = f"{nums[0]} {operations[0]} {nums[1]} {operations[1]} {nums[2]} {operations[2]} {nums[3]} {operations[3]} {nums[4]} {operations[3]} {nums[5]} {operations[0]} {nums[6]}"
                    ans = eval(ques_show)

                elif len(nums) == 8:
                    ques_show = f"{nums[0]} {operations[0]} {nums[1]} {operations[1]} {nums[2]} {operations[2]} {nums[3]} {operations[3]} {nums[4]} {operations[1]} {nums[5]} {operations[3]} {nums[6]} {operations[1]} {nums[7]}"
                    ans = eval(ques_show)

                else:
                    pass
                print(ques_show)
                print(round(ans, 3))
                global t_var
                t_var = StringVar()
                t_var.set("Math Questions")
                t_var1e = StringVar()
                t_var1e.set("Only Numbers allowed")
                t_var1 = StringVar()
                t_var1.set("Congrats! You've got it right")
                t_var2 = StringVar()
                t_var2.set(f"""Oops, You have not solved it right, its ok\nAnyways the answer is {round(ans, 3)} """)
                out_l3 = Label(main, textvariable = t_var , fg = '#F000FB', bg = mc, font = ('montserrat', 20))
                out_l3.place(x = 300, y = 150)
                def check_ans(e):
                    
                    try:
                        ans_user = round(float(ans_e.get()), 3)
                        print(ans_user)
                    except ValueError:
                        out_l31 = Label(main, textvariable = t_var1 , fg = '#F000FB', bg = mc, font = ('montserrat', 20))
                        out_l31.place(x = 300, y = 150)

                    if ans_user == ans:  
                        out_l32 = Label(main, textvariable = t_var1 , fg = '#F000FB', bg = mc, font = ('montserrat', 20))
                        out_l32.place(x = 300, y = 150)
                    else:
                        print(0)
                        out_l322 = Label(main, textvariable = t_var2 , fg = '#F000FB', bg = mc, font = ('montserrat', 20))
                        out_l322.place(x = 300, y = 150)

                    print(ans == ans_user)
                    ans_e.delete(0, END)
                    ques_l.config(text = "    \t\t\t\t\t")
                    math_cal_def()              

                def info_def():
                    t = '''Solve the question and write in the answer
                        If answer is in decimals, the first 3 decimals are necessary'''
                    tt = Label(main, text = t, bg = mc, fg = 'black')
                    tt.place(x = 400, y = 500)

                ques_l = Label(main, font = ('cambria', 23), bg = mc, fg = 'black')
                ques_l.place(x = 350, y = 280)
                ques_l.configure(text = " ")
                ques_l.config(text = ques_show + '\t\t\t')
                ans_l = Label(main, text = "Ans:", bg = mc, font = ('calibri', 21), fg = 'black')
                ans_l.place(x = 330, y = 340)
                ans_e = Entry(main, bg = mc, fg = 'black', font = ('cambria', 23))
                ans_e.place(x = 400, y = 340)
                ans_e.bind('<Return>', check_ans)
                sub_b = Button(main, text = "Submit", bg = mc, fg = 'black',
                font = ('calibri', 18), command = lambda: check_ans(None), height = 0)
                sub_b.place(x = 690, y = 340)
                info_b = Button(main, text = "Info", font = ('calibri', 18),
                bg = mc, fg = 'black', command = info_def)
                info_b.place(x = 707, y = 395)
            
            def fib_def():
                for widgets in main.winfo_children():
                    widgets.destroy()
                fib_show = Label(main, text = "Fibonacci Sequence.", 
                font = ('montserrat', 30), bg = mc, fg = 'orange')
                fib_show.place(x = 175, y = 50)

                def fib_ans(e):
                    err = Label(main, text  = "", bg = mc)
                    err.place(x = 700, y = 200)
                    try:
                        num = int(num_e.get())
                        err.config(text = "\t\t\t\t")
                        print(num)
                    except ValueError:
                        err.config(text = "Invalid Entry, try again")

                    list_ = []
                    @lru_cache(maxsize = 1000)
                    def fib_list(n) :
                        if type(n) != int:
                            list_.append("Only integers to be entered")

                        if n == 1:
                            return 1
                        elif n == 2:
                            return 2
                        elif n > 2:
                            return fib_list(n-1) + fib_list(n-2)
                    
                    for number in range(1, num):
                        list_.append(fib_list(number))

                    ans_t = Text(main, fg = 'purple', font = ('cambria', 14),
                    width = 20, height = 12)
                    ans_t.place(x = 400, y = 300)

                    for i in list_:
                        ans_t.insert(INSERT, f'{i}, \n')
                                     
                
                num_e = Entry(main, font = ('cambria', 18), fg  = 'blue')
                num_e.place(x = 400, y = 200)
                num_l = Label(main, text = "Enter the Number: ", bg = mc, fg = 'black',
                font = ('calibri', 13))
                num_l.place(x = 250, y = 205)
                sub_b = Button(main, text = 'Enter', bg = mc, fg = 'red', 
                font = ('cambria', 13), command = lambda: fib_ans(1))
                sub_b.place(x = 620, y = 200)
                num_e.bind('<Return>', fib_ans)


            def col_def():
                for widgets in main.winfo_children():
                    widgets.destroy()
                col_show = Label(main, text = "Collatz Conjecture.", 
                font = ('montserrat', 30), bg = mc, fg = 'orange')
                col_show.place(x = 175, y = 50)

                def col_check(e):
                    err = Label(main, text  = "", bg = mc)
                    err.place(x = 700, y = 200)
                    ans_t = Text(main, fg = 'purple', font = ('cambria', 14),
                    width = 20, height = 12)
                    ans_t.place(x = 400, y = 300)

                    try:
                        num = int(num_e.get())
                        err.config(text = "\t\t\t\t")
                        print(num)
                    except ValueError:
                        err.config(text = "Invalid Entry, try again")
                        
                    col_list = []
                    while True:
                        try:
                            if num == 1:
                                break
                            elif num%2 == 0:
                                # even number
                                go = num/2
                                col_list.append(go)
                                num = go
                                continue
                            else:
                                go = (num*3)+1
                                col_list.append(go)
                                num = go     
                        except:
                            pass
                            print('except')
                    for i in col_list:
                        ans_t.insert(INSERT,f'{int(i)},\n')

                    ans_t.insert(INSERT, "\n")
                    ans_t.insert(INSERT, "-+-+-+-+-+-+-+-+-+-+-+-")
                    ans_t.insert(INSERT, "\n")
                    ans_t.insert(INSERT, f"No of Steps: {len(col_list)}")

                col_l = Label(main, text = "Collatz Conjuncture", font = ('montserrat', 30),
                bg = mc, fg = 'orange')
                col_l.place(x = 300, y = 50)
                num_l = Label(main, text = "Enter Number: ", font = ('calibri', 13),
                bg = mc, fg = 'black')
                num_l.place(x = 300, y = 200)
                num_e = Entry(main, font = ('cambria', 13))
                num_e.place(x = 410, y = 200)
                num_e.bind("<Return>", col_check)
                sub_b = Button(main, text = "Enter", font = ('calibri', 13), bg = mc, 
                fg = 'black', command =  lambda: col_check(1))
                sub_b.place(x = 600, y = 200)
                


            math_b_cal = Button(main, text = 'Math Questions', font = ('cambria', 13),
            bg = mc, fg = 'black', command = math_cal_def)
            math_b_cal.place(x = 300, y = 100)
            fib_b = Button(main, text = 'Fibonacci Sequence', font = ('cambria', 13),
            bg = mc, fg = 'black', command = fib_def)
            fib_b.place(x = 450, y = 100)
            col_b = Button(main, text = "Collatz Conjecture", font = ('cambria', 13), 
            fg = 'black', bg = mc, command = col_def)
            col_b.place(x = 625, y = 100)
            
        def pt_def():
                        
            rt_table = tkinter.Toplevel()
            rt_table.title('Periodic Table')
            rt_table.geometry('1000x600')
            mc2 = '#FFD6FA'
            rt_table.config(bg = mc2)
            

            file = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\elements.txt', 'r')
            elements_list = []

            def search(key):
                get_user = search_e.get()
                search_e.delete(0, END)
                for i in elements_list:
                    i = i.split()
                    if get_user in i:
                        err.config(text = "\t\t\n\t\t\n\t\t\n")
                        put2 = Label(rt_table, text = "\t\t\n\t\t\n\t\t\n",
                        font = ('calibri', 18), bg = mc2)
                        put2.place(x = 200, y = 60)
                        put = Label(rt_table, text = f"Number: {i[0]}\nSymbol: {i[1]}\nName: {i[2]}",
                        font = ('montserrat', 14), fg = 'blue', bg = mc2)
                        put.place(x = 200, y = 60)
                        break
                    else:
                        err.config(text = 'Incorrect Input(s)')
                        continue

            for i in file:
                i = i.rstrip()
                i = i.lstrip()
                i = i.replace('\n', ' ')
                i = i.replace('\t', ' ')
                elements_list.append(i)
                
            style = ('calibri', 20)
            style2 = ('calibri', 17)
            for a in range(1, 16):
                Label(rt_table, text = "     ", font = style, bg = mc2).grid(row = 0, column = a)

            def btnclick(num):
                num = str(num)
                for i in elements_list:
                    i = i.split()
                    if num in i:
                        err.config(text = "\t\t\n\t\t\n\t\t\n")
                        put2 = Label(rt_table, text = "\t\t\n\t\t\n\t\t", 
                        font = ('calibri', 22), bg = mc2)
                        put2.place(x = 200, y = 60)
                        put = Label(rt_table, text = f"Number: {i[0]}\nSymbol: {i[1]}\nName: {i[2]}",
                        font = ('montserrat', 14), fg = 'blue', bg = mc2)
                        put.place(x = 200, y = 60)
                        break
                    else:
                        err.config(text = 'Incorrect Input(s)')
                        continue

            Button(rt_table, text = "1", font = style,
            command=lambda:btnclick(1), bg = mc2).grid(row = 0, column = 0)
            Button(rt_table, text = '2', font = style,
            command=lambda:btnclick(2), bg = mc2).grid(row = 0, column = 17)
            Button(rt_table, text = '3', font = style,
            command=lambda:btnclick(3), bg = mc2).grid(row = 1, column = 0)
            Button(rt_table, text = "4", font = style,
            command=lambda:btnclick(4), bg = mc2).grid(row = 1, column = 1)
            Button(rt_table, text = '11', font = style,
            command=lambda:btnclick(11), bg = mc2).grid(row = 2, column = 0)
            Button(rt_table, text = "12", font = style,
            command =lambda:btnclick(12), bg = mc2).grid(row = 2, column = 1)
            Button(rt_table, text = "55", font = style,
            command =lambda:btnclick(55), bg = mc2).grid(row = 5, column = 0)
            Button(rt_table, text = "56", font = style,
            command =lambda:btnclick(56), bg = mc2).grid(row = 5, column = 1)
            Button(rt_table, text = "87", font = style,
            command =lambda:btnclick(87), bg = mc2).grid(row = 6, column = 0)
            Button(rt_table, text = "88", font = style,
            command =lambda:btnclick(88), bg = mc2).grid(row = 6, column = 1)
            Label(rt_table, text = "**", font = style, bg = mc2).grid(row = 5, column = 2)
            Label(rt_table, text = "**", font = style, bg = mc2).grid(row = 6, column = 2)

            first = [5,6,7,8,9,10]
            second = [13,14,15,16,17,18]
            third = [ab for ab in range(19, 37)]
            fort_tableh = [ae for ae in range(37,55)]
            fifth = [aa2 for aa2 in range(72,87)]
            sixth = [aa3 for aa3 in range(104, 119)]
            seventh = [a4 for a4 in range(57, 72)]
            eighth = [a5 for a5 in range(89, 104)]

            button_dict = {}

            for i in first:   
                def action(x=i): 
                    btnclick(str(x))    
                    
                button_dict[i] = Button(rt_table, text = i, font = style,
                                command = action, bg = mc2).grid(row = 1, column = i+7)

            for ii in second:
                def action(x = ii): 
                    btnclick(str(x))
                
                button_dict[ii] = Button(rt_table, text = ii, font = style,
                               command = action, bg = mc2).grid(row = 2, column = ii-1)

            for i2 in third:
                def action(x = i2): 
                    btnclick(str(x))
                
                button_dict[i2] = Button(rt_table, text = i2, font = style,
                        command = action, bg = mc2).grid(row = 3, column = i2-19)

            for i3 in fort_tableh:
                def action(x = i3):
                    btnclick(str(x))

                button_dict[i3] = Button(rt_table, text = i3, font = style,
                             command = action, bg = mc2).grid(row = 4, column = i3-37)

            for i4 in fifth:
                def action(x = i4):
                    btnclick(str(x))

                button_dict[i3] = Button(rt_table, text = i4, font = style,
                               command = action, bg = mc2).grid(row = 5, column = i4-69)

            for i5 in sixth:
                def action(x = i5):
                    btnclick(str(x))

                button_dict[i3] = Button(rt_table, text = i5, font = style2 ,
                            command = action, bg = mc2).grid(row = 6, column = i5-101)

            for i6 in seventh:
                def action(x = i6):
                    btnclick(str(x))

                button_dict[i3] = Button(rt_table, text = i6, font = style,
                               command = action, bg = mc2).grid(row = 8, column = i6-56)

            for i7 in eighth:
                def action(x = i7):
                    btnclick(str(x))

                button_dict[i3] = Button(rt_table, text = i7, font = style2,
                            command = action, bg = mc2).grid(row = 9, column = i7-88)

            emp = Label(rt_table, text = "", font = style, bg = mc2)
            emp.grid(row = 7, column = 0)
            err = Label(rt_table,text = '', fg = 'red', bg = mc2)
            err.place(x = 200, y = 60)

            search_l = Label(rt_table, text = "Search any Periodic element: ", 
            font = style, bg = mc2)
            search_l.place(x = 100, y = 20)

            search_e = Entry(rt_table, font = style)
            search_e.place(x = 450, y = 20)
            search_e.bind('<Return>', search)
            rt_table.mainloop()

        def calender_def():
            def show_events():
                change_list = []
                def update_def():
                    user_change = event_t.get(1.0, END)
                    user_change = user_change.strip()
                    w = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\cal.txt', 'a')
                    try:
                        get_change = file1.replace(f'"{change_list[0]}": "{change_list[1]}"',
                        f'"{change_list[0]}": "{user_change}"\n')
                        file_to_go = file1.replace(file1, get_change)
                        w.truncate()
                        w.write(file_to_go)
                        w.close()
                    except:
                        get_change = f'"{date}": "{user_change}"\n'
                        file_to_go = file1.replace(file1, get_change)
                        
                        w.write(file_to_go)
                        w.close()


                event_t = Text(main, fg = 'black', font = ('quicksand', 13),
                width = 25, height = 10)
                event_t.place(x = 300, y = 350)
                update_b = ttk.Button(main, text = "Update", command = update_def)
                update_b.place(x = 600, y = 350)
                #mm/dd/yyyy
                '{"7/6/2021": "gyegyueguygfefefef"}'
                file_open = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\cal.txt', 'r+')
                file1 = file_open.read()
                file = file1.splitlines()
                date = cal.get_date()
                print(date)       
                for i in file:
                    i = i.replace("{", '')
                    i = i.replace('}', '')
                    i = i.replace(':', '')
                    i = i.strip()
                    ii = i.split()
                    list_a = [a.replace('"', '') for a in ii]
                    print(list_a)
                    """{"7/6/21": "gyegyueguygfefefef"}
                        {"7/6/22": "gtjioyegyueguygfefefef"}
                        {"5/7/19": "gueguygfefefef"}
                        """               
                    print(list_a[0])
                    print(date)
                    if list_a[0] == date.strip():
                        event_t.insert(INSERT, list_a[1:])
                        change_list.append(list_a)
           
                    file_open.close()
            cal = Calendar(main, selectmode = 'day', year = 2021, month = 7,
            day = 30, font = ('cambria', 20))
            cal.place(x = 300, y = 0)
            event_b = ttk.Button(main, text = "Show Event", command = show_events)
            event_b.place(x = 800, y = 100)

        def ticket_def():
            ticket_frame = Frame(main, width = 800, height = 600, bg = mc)
            ticket_frame.place(x = 400, y = 150)
            style = ('segoe ui', 15)
            style2 = ('calibri', 13)
            fromcities = StringVar()
            tocities = StringVar()
            timevar = StringVar()
            modevar = StringVar()
            typevar = StringVar()
            type2var = StringVar()
            time_dep_var_d = IntVar()
            time_dep_var_m = StringVar()
            main_list = []

            cars_available = ('Uber','Ola','Wajahati','RTA','Super car')
            car_seats = ('Normal','Super','Delux','Ultra','Shared')
            bus_types = ('Bus trans','Yahoo','Wajahati','RTA','sleeper Busses')
            bus_seats = ('Normal','Super','Delux', 'Sleeper')
            Air_types = ('Indigo','Emirates','AirIndia','Ethihad','United')
            Air_seats = ('Economy','Business','First')
            ship_types = ('Maersk','Mediterranean \nShipping.Co',
                        'Evergreen Line','COSCO Shipping','Orient Overseas')
            ship_seats = ('Economy','Business','First', 'Super')
            #ORDER: Name, Dep city, Des city, Time, Vehicle, MM/YYYY, DD, vehicle name, class


            def proceed(e):
                def next_def():
                    main_list.append(fromcities.get())
                    main_list.append(tocities.get())
                    main_list.append(timevar.get())
                    main_list.append(modevar.get())
                    main_list.append(time_dep_var_m.get())
                    main_list.append(time_dep_var_d.get())
                    main_list.append(type2var.get())
                    #('Car', 'Bus', 'Airplane', 'Ship')

                    for widgets in ticket_frame.winfo_children():
                        widgets.destroy()
                        
                    def submitdef():
                        
                        main_list.append(typevar.get())
                        main_list.append(type2var.get())
                        print(main)
                        for widgets in ticket_frame.winfo_children():
                            widgets.destroy()
                        def old_ticket():
                            Label(ticket_frame, text = f"Passenger Name: {main_list[0]}").grid(row = 0, column = 0)
                            Label(ticket_frame, text = f"from-to: {main_list[1]}-{main_list[2]}").grid(row = 1, column = 0)
                            Label(ticket_frame, text = f"Time: {main_list[3]}").grid(row = 0, column = 1)
                            Label(ticket_frame, text = f"Transporation: {main_list[7]}").grid(row = 2, column = 0)
                            Label(ticket_frame, text = f"Date: {main_list[6]}/{main_list[5]}").grid(row = 2, column = 1)
                            Label(ticket_frame, text = f"Class: {main_list[8]}").grid(row = 3, column = 0)
                            Label(ticket_frame, text = "Travel Booking.com").grid(row = 3, column = 1)

                        style3 = ('calibri', 20)
                        #['Sai', 'Ajman', 'Umm Al Quwain', '0:30 AM', 'Ship', '2/2021', 4, '', 'Orient Overseas', 'Business']
                        # 0       1            2              3        4       5         6   7   8                    9
                        
                        def show_ticket():
                            ticket_frame2 = Toplevel(main)
                            image1 = Image.open("ticket.png")
                            test = ImageTk.PhotoImage(image1)
                            label1 = tkinter.Label(ticket_frame2, image=test)
                            label1.image = test
                            label1.grid(row = 0, column = 0)
                            
                            l1 = Label(ticket_frame2, text = main_list[0], bg = '#d3a35e', font = style3)
                            l1.place(x = 350, y = 47)
                            l2 = Label(ticket_frame2, text = main_list[1], bg = '#d3a35e', font = style3)
                            l2.place(x = 50, y = 150)
                            l3 = Label(ticket_frame2, text = main_list[2], bg = '#d3a35e', font = style3)
                            l3.place(x = 600, y = 150)
                            l4 = Label(ticket_frame2, text = main_list[3], bg = '#d3a35e', font = style3)
                            l4.place(x = 100, y = 210)
                            l5 = Label(ticket_frame2, text = f'{main_list[6]}/{main_list[5]}', bg = '#d3a35e', font = style3)
                            l5.place(x = 100, y = 250)
                            l6 = Label(ticket_frame2, text = main_list[8], bg = '#d3a35e', font = style3)
                            l6.place(x = 180, y = 340)
                            l7 = Label(ticket_frame2, text = main_list[9], bg = '#d3a35e', font = style3)
                            l7.place(x = 630, y = 330)
                            l8 = Label(ticket_frame2, text = main_list[4], bg = '#d3a35e', font = style3)
                            l8.place(x = 650, y = 220)
                            ticket_frame2.mainloop()
                        show_b = Button(ticket_frame, text = "Show Ticket.", fg = 'black', 
                        font = style, command = show_ticket, bg = mc)
                        show_b.grid(row = 50, column = 50)

                    if modevar.get().lower() == 'car':

                        print('car is selected')
                        type_l = Label(ticket_frame, text = "Select a car company ", font = style2, bg = mc)
                        type_l.grid(row = 0, column = 0)
                        type_c = ttk.Combobox(ticket_frame, width = 15, textvariable = typevar)
                        type_c['values'] = cars_available
                        type_c.grid(row = 0, column = 1)
                        type_c.current()
                        
                        type_c2_l = Label(ticket_frame, text = "Select Comfort: ", font = style2, bg = mc)
                        type_c2_l.grid(row = 1, column = 0)
                        type_c2 = ttk.Combobox(ticket_frame, width = 15, textvariable = type2var)
                        type_c2['values'] = car_seats
                        type_c2.grid(row = 1, column = 1)
                        type_c2.current()

                        sub_b = Button(ticket_frame, text = "Submit", command =  submitdef, bg = mc)
                        sub_b.grid(row = 2, column = 1)


                    elif modevar.get().lower() == 'bus':
                        print('bus has been selected')

                        type_l = Label(ticket_frame, text = "Select a bus company ", font = style2, bg = mc)
                        type_l.grid(row = 0, column = 0)
                        type_c = ttk.Combobox(ticket_frame, width = 15, textvariable = typevar)
                        type_c['values'] = bus_types 
                        type_c.grid(row = 0, column = 1)
                        type_c.current()
                        
                        type_c2_l = Label(ticket_frame, text = "Select Comfort: ", font = style2, bg = mc)
                        type_c2_l.grid(row = 1, column = 0)
                        type_c2 = ttk.Combobox(ticket_frame, width = 15, textvariable = type2var)
                        type_c2['values'] = bus_seats
                        type_c2.grid(row = 1, column = 1)
                        type_c2.current()

                        sub_b = Button(ticket_frame, text = "Submit", command =  submitdef, bg = mc)
                        sub_b.grid(row = 2, column = 1) 
                    
                    elif modevar.get().lower() == 'airplane':

                        print('airplane has been selected')
                        type_l = Label(ticket_frame, text = "Select a Airline company ", font = style2, bg = mc)
                        type_l.grid(row = 0, column = 0)
                        type_c = ttk.Combobox(ticket_frame, width = 18, textvariable = typevar)

                        type_c.grid(row = 0, column = 1)  
                        type_c.current()
                        
                        type_c2_l = Label(ticket_frame, text = "Select Comfort: ", font = style2, bg = mc)
                        type_c2_l.grid(row = 1, column = 0)
                        type_c2 = ttk.Combobox(ticket_frame, width = 15, textvariable = type2var)
                        type_c2['values'] = Air_seats 
                        type_c2.grid(row = 1, column = 1)
                        type_c2.current()

                        sub_b = Button(ticket_frame, text = "Submit", command =  submitdef, bg = mc)
                        sub_b.grid(row = 2, column = 1) 
                    
                    elif modevar.get().lower() == 'ship':
                        print('Ship has been selected')
                            
                        type_l = Label(ticket_frame, text = "Select a Ship company ", font = style2, bg = mc)
                        type_l.grid(row = 0, column = 0)
                        type_c = ttk.Combobox(ticket_frame, width = 20, textvariable = typevar)
                        type_c['values'] = ship_types 
                        type_c.grid(row = 0, column = 1)
                        type_c.current()
                        
                        type_c2_l = Label(ticket_frame, text = "Select Comfort: ", font = style2, bg = mc)
                        type_c2_l.grid(row = 1, column = 0)
                        type_c2 = ttk.Combobox(ticket_frame, width = 15, textvariable = type2var)
                        type_c2['values'] = ship_seats 
                        type_c2.grid(row = 1, column = 1)
                        type_c.current()

                        sub_b = Button(ticket_frame, text = "Submit", command =  submitdef, bg = mc)
                        sub_b.grid(row = 2, column = 1) 

                    else:
                        print(f'{modevar}this has been selected')

                name = name_e.get()
                main_list.append(name)
                name_e.destroy()
                name_l.destroy()
                intro.config(text = f"Hello {name}, please fill this form.", bg = mc)
                from_l = Label(ticket_frame, text = "Select departure city to \n to destination city", 
                font = style2, bg = mc)
                from_l.grid(row = 1, column = 0)
                cities = (
                "Abu Dhabi", 
                "Dubai", 
                "Sharjah", 
                "Ajman", 
                "Fujairah", 
                "Umm Al Quwain",
                "Al Ain")
                
                fromcities.set("Departure City")
                tocities.set('Destination City')
                timevar.set('Time')
                modevar.set('Transport type')
                city_select = ttk.Combobox(ticket_frame, width = 15, textvariable = fromcities)
                city_select['values'] = cities
                city_select.grid(row = 1, column = 1)
                city_select.current()

                to_l = Label(ticket_frame, text = "-To-", bg = mc)
                to_l.grid(row = 1, column = 2)
                city_select2 = ttk.Combobox(ticket_frame, width = 15, textvariable = tocities)
                city_select2['values'] = cities
                city_select2.grid(row = 1, column = 3) 
                city_select2.current()
                time = ttk.Combobox(ticket_frame, width = 15, textvariable = timevar)
                time_list = [] 

                for i in range(24):
                    if i >= 12:
                        time_list.append(f"{str(i)}:00 PM")
                        time_list.append(f"{str(i)}:15 PM")
                        time_list.append(f"{str(i)}:30 PM")
                        time_list.append(f"{str(i)}:45 PM")
                    else:
                        time_list.append(f"{str(i)}:00 AM")
                        time_list.append(f"{str(i)}:15 AM")
                        time_list.append(f"{str(i)}:30 AM")
                        time_list.append(f"{str(i)}:45 AM")


                time_tuple = tuple(time_list)

                time['values'] = time_tuple
                time.grid(row = 2, column = 1)
                time.current() 
                time_l = Label(ticket_frame, text = "Select Time of Departure", font = style2)
                time_l.grid(row = 2, column = 0)

                month_list = []
                for i in range(1, 12):
                    month_list.append(f'{i}/2021')
                month = tuple(month_list)
                day_list = []
                for i in range(1, 31):
                    day_list.append(i)
                day = tuple(day_list)
                


                dep_l = Label(ticket_frame, text = "Select Date of \nDeparture: ", font = style2)
                dep_l.grid(row = 3, column = 0)
                time_dep_var_d.set('Day')
                time_dep_var_m.set('MM/YYYY')

                time_d = ttk.Combobox(ticket_frame, width = 14, textvariable = time_dep_var_d)
                time_d['values'] = day
                time_d.grid(row = 3, column = 1)    
                time_d.current()

                time_m = ttk.Combobox(ticket_frame, width = 12, textvariable = time_dep_var_m)
                time_m['values'] = month
                time_m.grid(row = 3, column = 2)
                time_m.current()

                
                mode_l = Label(ticket_frame, text = "Select Mode of Transportation", font = style2)
                mode_l.grid(row = 4, column = 0)

                time = ttk.Combobox(ticket_frame, width = 15, textvariable = modevar)
                time['values'] = ('Car', 'Bus', 'Airplane', 'Ship')
                time.grid(row = 4, column = 1)
                time.current()

                next_b = Button(ticket_frame, text = "Next -->", font = style2, command = next_def)
                next_b.grid(row = 5, column = 2)
                


            intro = Label(ticket_frame, text = "Welcome to \nTravel Booking.com", font = style)
            intro.grid(row = 0, column = 0)
            name_l = Label(ticket_frame, text = "Enter Name: ", font = style)
            name_l.grid(row = 1, column = 0)
            name_e = Entry(ticket_frame, font = style)
            name_e.grid(row = 1, column = 1)
            name_e.bind("<Return>", proceed)
            ticket_frame.mainloop()

        def graph_def():
            for w in main.winfo_children():
                w.destroy()
            def bar_def():
                for wid in main.winfo_children():
                    wid.destroy()

                def main_turtle_draw():
                    win = tr.Screen()
                    win.bgcolor("#D7FF8C")
                    win.title("Graph draw")
                    win.setup(1000,700)
                    tt = tr.Turtle()
                    tt.penup()
                    tt.goto(-400,-300)


                    #border loop
                    tt.pendown()
                    tt.pensize(5)
                    tt.speed(100)

                    for i in range(2):
                        tt.forward(800)
                        tt.left(90)
                        tt.forward(600)
                        tt.left(90)
                        print(i)

                    tt.pensize(2)
                        
                    for i in range(10):
                        tt.forward(40)
                        tt.left(90)
                        tt.forward(600)
                        tt.right(90)
                        tt.forward(40)
                        tt.right(90)
                        tt.forward(600)
                        tt.left(90)
                        print(i)

                    for i in range(10):
                        tt.left(90)
                        tt.forward(30)
                        tt.left(90)
                        tt.forward(800)
                        tt.right(90)
                        tt.forward(30)
                        tt.right(90)
                        tt.forward(800)
                        print(i)

                        
                    def sidenum():
                        tt.penup()
                        tt.pencolor('dark orange')
                        tt.goto(-400,-300)
                        tt.setheading(180)
                        tt.forward(35)
                        tt.right(90)
                        itsnum = 5

                        for i in range(20):
                            tt.write(itsnum, font = ('Arial', 12))
                            tt.forward(30)
                            itsnum = (itsnum+5)

                    def a1def():
                        try:
                            f1 = float(i1.get())
                            f1 = (f1*6)
                            tt.penup()
                            tt.goto(-400,-300)
                            tt.pendown()
                            tt.pencolor('red')
                            tt.fillcolor('pink')
                            tt.begin_fill()
                            tt.pensize(4)
                            tt.forward(40)
                            tt.left(90)
                            tt.forward(f1)
                            tt.right(90)
                            tt.forward(40)
                            tt.right(90)
                            tt.forward(f1)
                            tt.goto(-400,-300)
                            tt.setheading(0)
                            tt.end_fill()
                            tt.penup()
                            tt.right(90)
                            tt.forward(30)
                            tt.left(90)
                            tt.forward(40)
                            f1 = f1/6
                            tt.write(f1, font = ('quicksand', 10))
                            sidenum()

                            



                        except ValueError:
                            print(' Not a number input')
                            err = Label(rt_g, text = 'Pls enter a valid number')
                            err.grid(row = 12, column = 0)


                    def a2def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None
                            else:
                                f1 = f1*6
                                f2 = f2*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()#isover
                                tt.setheading(0)
                                tt.penup()
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                sidenum()

                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a valid number')
                            err.grid(row = 22, column = 0)

                    def a3def():

                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())

                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None
                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)#
                                tt.penup()#
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                sidenum()


                                
                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a valid number')
                            err.grid(row = 22, column = 0)
                    def a4def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())

                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None

                            elif f4 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f4 = None
                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                f4 = f4*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)#here is the next one!
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f4)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f4)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)
                                tt.penup()#
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                f4 = f4/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f4, font = ('quicksand', 10))
                                sidenum()

                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a number')
                            err.grid(row = 22, column = 0)

                    def a5def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())
                            f5 = float(i5.get())

                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None

                            elif f4 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f4 = None
                            
                            elif f5 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f5 = None
                            
                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                f4 = f4*6
                                f5 = f5*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)#here is the next one!
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f4)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f4)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f5)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f5)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)
                                tt.penup()#####Its here !!!!!!!!!!!!!!!!
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                f4 = f4/6
                                f5 = f5/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f4, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f5, font = ('quicksand', 10))
                                sidenum()
                                
                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a number')
                            err.grid(row = 22, column = 0)

                    def a6def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())
                            f5 = float(i5.get())
                            f6 = float(i6.get())

                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None

                            elif f4 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f4 = None
                            
                            elif f5 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f5 = None
                            
                            elif f6 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f6 = None

                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                f4 = f4*6
                                f5 = f5*6
                                f6 = f6*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)#here is the next one!
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f4)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f4)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f5)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f5)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f6)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f6)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)
                                tt.penup()#####Its here !!!!!!!!!!!!!!!!
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                f4 = f4/6
                                f5 = f5/6
                                f6 = f6/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f4, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f5, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f6, font = ('quicksand', 10))
                                sidenum()



                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a number')
                            err.grid(row = 22, column = 0)

                    def a7def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())
                            f5 = float(i5.get())
                            f6 = float(i6.get())
                            f7 = float(i7.get())

                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None

                            elif f4 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f4 = None
                            
                            elif f5 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f5 = None
                            
                            elif f6 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f6 = None
                            
                            elif f7 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f7 = None

                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                f4 = f4*6
                                f5 = f5*6
                                f6 = f6*6
                                f7 = f7*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)#here is the next one!
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f4)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f4)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f5)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f5)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f6)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f6)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f7)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f7)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)
                                tt.penup()#####Its here !!!!!!!!!!!!!!!!
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                f4 = f4/6
                                f5 = f5/6
                                f6 = f6/6
                                f7 = f7/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f4, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f5, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f6, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f7, font = ('quicksand', 10))
                                sidenum()

                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a number')
                            err.grid(row = 22, column = 0)


                    def a8def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())
                            f5 = float(i5.get())
                            f6 = float(i6.get())
                            f7 = float(i7.get())
                            f8 = float(i8.get())      
                            
                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None

                            elif f4 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f4 = None
                            
                            elif f5 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f5 = None
                            
                            elif f6 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f6 = None
                            
                            elif f7 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f7 = None

                            elif f8 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f8 = None

                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                f4 = f4*6
                                f5 = f5*6
                                f6 = f6*6
                                f7 = f7*6
                                f8 = f8*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)#here is the next one!
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f4)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f4)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f5)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f5)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f6)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f6)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f7)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f7)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f8)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f8)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)
                                tt.penup()#####Its here !!!!!!!!!!!!!!!!
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                f4 = f4/6
                                f5 = f5/6
                                f6 = f6/6
                                f7 = f7/6
                                f8 = f8/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f4, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f5, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f6, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f7, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f8, font = ('quicksand', 10))
                                sidenum()



                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a number')
                            err.grid(row = 22, column = 0)


                    def a9def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())
                            f5 = float(i5.get())
                            f6 = float(i6.get())
                            f7 = float(i7.get())
                            f8 = float(i8.get())
                            f9 = float(i9.get())

                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None

                            elif f4 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f4 = None
                            
                            elif f5 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f5 = None
                            
                            elif f6 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f6 = None
                            
                            elif f7 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f7 = None

                            elif f8 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f8 = None

                            elif f9 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f9 = None

                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                f4 = f4*6
                                f5 = f5*6
                                f6 = f6*6
                                f7 = f7*6
                                f8 = f8*6
                                f9 = f9*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)#here is the next one!
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f4)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f4)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f5)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f5)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f6)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f6)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f7)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f7)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f8)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f8)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f9)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f9)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)
                                tt.penup()#####Its here !!!!!!!!!!!!!!!!
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                f4 = f4/6
                                f5 = f5/6
                                f6 = f6/6
                                f7 = f7/6
                                f8 = f8/6
                                f9 = f9/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f4, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f5, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f6, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f7, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f8, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f9, font = ('quicksand', 10))
                                sidenum()

                                
                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a number')
                            err.grid(row = 22, column = 0)


                    def a10def():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())
                            f5 = float(i5.get())
                            f6 = float(i6.get())
                            f7 = float(i7.get())
                            f8 = float(i8.get())
                            f9 = float(i9.get())
                            f10 = float(i10.get())

                            if f1 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f1 = None
                            elif f2 > 100:
                                err = Label(rt_g, text = 'Maximum value is 100')
                                err.grid(row = 13, column = 0)
                                f2 = None

                            elif f3 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f3 = None

                            elif f4 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f4 = None
                            
                            elif f5 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f5 = None
                            
                            elif f6 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f6 = None
                            
                            elif f7 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f7 = None

                            elif f8 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f8 = None

                            elif f9 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f9 = None

                            elif f10 > 100:
                                err = Label(rt_g, text = 'Maximum Value is 100',)
                                err.grid(row = 13, column = 0)
                                f10 = None

                            else:
                                f1 = f1*6
                                f2 = f2*6
                                f3 = f3*6
                                f4 = f4*6
                                f5 = f5*6
                                f6 = f6*6
                                f7 = f7*6
                                f8 = f8*6
                                f9 = f9*6
                                f10 = f10*6
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.pendown()
                                tt.pencolor('red')
                                tt.fillcolor('pink')
                                tt.begin_fill()
                                tt.pensize(4)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f1)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f1)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f2)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f2)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f3)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f3)#here is the next one!
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f4)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f4)
                                tt.left(90)
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f5)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f5)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f6)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f6)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f7)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f7)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f8)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f8)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f9)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f9)
                                tt.left(90)#####
                                tt.forward(40)
                                tt.left(90)
                                tt.forward(f10)
                                tt.right(90)
                                tt.forward(40)
                                tt.right(90)
                                tt.forward(f10)
                                tt.penup()
                                tt.goto(-400,-300)
                                tt.end_fill()
                                tt.setheading(0)
                                tt.penup()#####Its here !!!!!!!!!!!!!!!!
                                tt.right(90)
                                tt.forward(30)
                                tt.left(90)
                                tt.forward(45)
                                f1 = f1/6
                                f2 = f2/6
                                f3 = f3/6
                                f4 = f4/6
                                f5 = f5/6
                                f6 = f6/6
                                f7 = f7/6
                                f8 = f8/6
                                f9 = f9/6
                                f10 = f10/6
                                tt.write(f1, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f2, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f3, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f4, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f5, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f6, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f7, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f8, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f9, font = ('quicksand', 10))
                                tt.forward(80)
                                tt.write(f10, font = ('quicksand', 10))
                                tt.penup()
                                tt.goto(-400,-300)
                                sidenum()

                        except ValueError:
                            print('Not a number input')
                            err = Label(rt_g, text = 'Pls enter a number')
                            err.grid(row = 25, column = 0)


                    rt_g = tkinter.Tk()
                    rt_g.geometry("480x415")
                    l1 = Label(rt_g,text = 'Enter the Value of BAR 1', font = ('open sans', 15))
                    l1.grid(row = 0, column = 0)
                    i1 = Entry(rt_g, font = ('open sans', 15))
                    i1.grid(row = 0, column = 1)

                    l2 = Label(rt_g,text = 'Enter the Value of BAR 2', font = ('open sans', 15))
                    l2.grid(row = 1, column = 0)
                    i2 = Entry(rt_g, font = ('open sans', 15))
                    i2.grid(row = 1, column = 1)

                    l3 = Label(rt_g,text = 'Enter the Value of BAR 3', font = ('open sans', 15))
                    l3.grid(row = 3, column = 0)
                    i3 = Entry(rt_g, font = ('open sans', 15))
                    i3.grid(row = 3, column = 1)

                    l4 = Label(rt_g,text = 'Enter the Value of BAR 4', font = ('open sans', 15))
                    l4.grid(row = 4, column = 0)
                    i4 = Entry(rt_g, font = ('open sans', 15))
                    i4.grid(row = 4, column = 1)

                    l5 = Label(rt_g,text = 'Enter the Value of BAR 5', font = ('open sans', 15))
                    l5.grid(row = 5, column = 0)
                    i5 = Entry(rt_g, font = ('open sans', 15))
                    i5.grid(row = 5, column = 1)

                    l6 = Label(rt_g,text = 'Enter the Value of BAR 6', font = ('open sans', 15))
                    l6.grid(row = 6, column = 0)
                    i6 = Entry(rt_g, font = ('open sans', 15))
                    i6.grid(row = 6, column = 1)

                    l7 = Label(rt_g,text = 'Enter the Value of BAR 7', font = ('open sans', 15))
                    l7.grid(row = 7, column = 0)
                    i7 = Entry(rt_g, font = ('open sans', 15))
                    i7.grid(row = 7, column = 1)

                    l8 = Label(rt_g,text = 'Enter the Value of BAR 8', font = ('open sans', 15))
                    l8.grid(row = 8, column = 0)
                    i8 = Entry(rt_g, font = ('open sans', 15))
                    i8.grid(row = 8, column = 1)

                    l9 = Label(rt_g,text = 'Enter the Value of BAR 9', font = ('open sans', 15))
                    l9.grid(row = 9, column = 0)
                    i9 = Entry(rt_g, font = ('open sans', 15))
                    i9.grid(row = 9, column = 1)

                    l10 = Label(rt_g,text = 'Enter the Value of BAR 10', font = ('open sans', 15))
                    l10.grid(row = 10, column = 0)
                    i10 = Entry(rt_g, font = ('open sans', 15))
                    i10.grid(row = 10, column = 1)



                    a1 = Button(rt_g, text = 'Submit 1 Bar', font = ('open sans', 10), command = a1def, fg = 'purple', bg = 'yellow')
                    a2 = Button(rt_g, text = 'Submit 2 Bars', font = ('open sans', 10), command = a2def, fg = 'Green', bg = 'orange')
                    a3 = Button(rt_g, text = 'Submit 3 Bars', font = ('open sans', 10), command = a3def, fg = 'purple', bg = 'yellow')
                    a4 = Button(rt_g, text = 'Submit 4 Bars', font = ('open sans', 10), command = a4def, fg = 'Green', bg = 'orange' )
                    a5 = Button(rt_g, text = 'Submit 5 Bars', font = ('open sans', 10), command = a5def, fg = 'purple', bg = 'yellow')
                    a6 = Button(rt_g, text = 'Submit 6 Bars', font = ('open sans', 10), command = a6def, fg = 'Green', bg = 'orange' )
                    a7 = Button(rt_g, text = 'Submit 7 Bars', font = ('open sans', 10), command = a7def, fg = 'purple', bg = 'yellow')
                    a8 = Button(rt_g, text = 'Submit 8 Bars', font = ('open sans', 10), command = a8def, fg = 'Green', bg = 'orange' )
                    a9 = Button(rt_g, text = 'Submit 9 Bars', font = ('open sans', 10), command = a9def, fg = 'purple', bg = 'yellow' )
                    a10 = Button(rt_g, text = 'Submit 10 Bars', font = ('open sans', 10), command = a10def, fg = 'Green', bg = 'orange')

                    a1.place(x = 0, y = 300)
                    a2.place(x = 90, y = 300)
                    a3.place(x = 180, y = 300)
                    a4.place(x = 270, y = 300)
                    a5.place(x = 360, y = 300)
                    a6.place(x = 0, y = 325)
                    a7.place(x = 90, y = 325)
                    a8.place(x = 180, y = 325)
                    a9.place(x = 270, y = 325)
                    a10.place(x = 360, y = 325)

                    def defst():
                        try:
                            f1 = float(i1.get())
                            f2 = float(i2.get())
                            f3 = float(i3.get())
                            f4 = float(i4.get())
                            f5 = float(i5.get())
                            f6 = float(i6.get())
                            f7 = float(i7.get())
                            f8 = float(i8.get())
                            f9 = float(i9.get())
                            f10 = float(i10.get())
                            lista = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
                            meann = statistics.mean(lista)
                            modee = statistics.mode(lista)
                            rangg = max(lista)-min(lista)
                            medi = statistics.median(lista)
                            mean = ' Mean: ' + str(meann) 
                            rang = ' Range: ' + str(rangg) 
                            mode = ' Mode: ' + str(modee)
                            med = ' Median: ' + str(medi)
                            
                            meanl = Label(rt_g, text = mean, font = ('Helvitica', 11), bg = 'orange', fg = 'green')
                            model = Label(rt_g, text = mode, font = ('Helvitica', 11), bg = 'yellow', fg = 'red')
                            rangl = Label(rt_g, text = rang, font = ('Helvitica', 11), bg = 'orange', fg = 'green')
                            medl = Label(rt_g, text = med, font = ('helvitica', 11), bg ='yellow', fg = 'red' )
                            medl.place(x = 300, y = 400)
                            meanl.place(x = 0, y = 400)
                            model.place(x = 100, y = 400)
                            rangl.place(x = 200, y = 400)
                            print('executed here successfully!')
                        except ValueError:
                            print('error in the open try and except place!')

                    stats = Button(rt_g, text = 'Statistics', font = ('Helvetica', 10), command = defst, bg = 'black', fg = 'white')
                    stats.place(x = 0, y = 360)
                    print('the code is right here!')

                    win.mainloop()
                    rt_g.mainloop()
            
                main_turtle_draw()

            bar_b = Button(main, text = "Bar Graph", font = ('roboto mono', 12),
            bg = mc, activebackground = mc, command = bar_def, fg = 'black')
            bar_b.place(x = 400, y = 200)

        '''def hand_cricket_def():
            for wins in main.winfo_children():
                wins.destroy()
            
            def toss_def():
                intro2 = Label(main, text = "Toss: YOU vs AI", font = ('calibri', 14), bg = mc)
                intro2.place(x = 30, y = 250)

                def win_def(get_):
                    for widgets in main.winfo_children():
                        widgets.destroy()
                    def start_game_def(num_):
                        # win = 0
                        # loss = 1
                        num_o = num_overs.get()
                        bob = bat_bowl_str.get()
                        for wins in main.winfo_children():
                            wins.destroy()
                        if num_ == 0:
                            ran_show = random.randint(0,5)
                            if bob == 'Batting':
                                pass
                        
                                def win_choose_def2(num2):
                                    while True:
                                        com_num = random.randint(0, 5)
                                        img_oe = Label(main, text = "", font = ('calibri', 15), bg = mc,
                                            image = oe_imgs[num2])
                                        img_oe.place(x = 250, y = 100)
                                        
                                        if com_num == num2:
                                            nope = Label(main, text = "Its a TIE", font = ('segoe ui', 13),
                                            bg = mc, fg = 'orange')
                                            nope.place(x = 200, y  = 250)

                        one_l = Button(main, text = "", image = one_img, 
                        font = ('montserrat', 20), bg = mc, command = lambda: win_choose_def(0))
                        two_l = Button(main, text = "", image = two_img, 
                        font = ('montserrat', 20), bg = mc, command = lambda: win_choose_def(1))
                        three_l = Button(main, text = "", image = three_img, 
                        font = ('montserrat', 20), bg = mc, command = lambda: win_choose_def(2))
                        four_l = Button(main, text = "", image = four_img, 
                        font = ('montserrat', 20), bg = mc, command = lambda: win_choose_def(3))
                        five_l = Button(main, text = "", image = five_img,
                        font = ('montserrat', 20), bg = mc, command = lambda: win_choose_def(4))
                        six_l = Button(main, text = "", image = six_img, 
                        font = ('montserrat', 20), bg = mc, command = lambda: win_choose_def(5))
                        one_l.place(x = 0, y = 400)
                        two_l.place(x = 100, y = 400)
                        three_l.place(x = 200, y = 400)
                        four_l.place(x = 300, y = 400) 
                        five_l.place(x = 400, y = 400)
                        six_l.place(x = 500, y = 400)
                        
                        if num == 0:
                            pass
                            #odd
                        else:
                            pass
                            #even


                    if get_ == 1:
                        print("wins")
                        rel = Label(main, text = "You Won", 
                        font = ('segoe ui', 18), bg = mc)
                        rel.place(x = 300, y = 30)
                        num_overs = IntVar()
                        #num_overs
                        
                        overs_e = ttk.Combobox(main, width = 25, textvariable = num_overs
                        ,font = ('segoe ui', 11))
                        overs_e['values'] = (1,2,3,4,5,6)
                        overs_e.place(x = 400, y = 100)
                        overs_l = Label(main, font = ('cambria', 13), text = "Numbers of Overs: ", bg = mc)
                        overs_l.place(x = 250, y = 100)
                        bob_l = Label(main, text = "Batting or bowling?", bg = mc, font = ('segoe ui', 13))
                        bob_l.place(x = 250, y = 200)
                        bat_bowl_str = StringVar()
                        bob_com = ttk.Combobox(main, width = 27, textvariable = bat_bowl_str,
                         font = ('segoe ui', 11))
                        bob_com['values'] = ("Batting", "Bowling")
                        #bat_bowl_str
                        bob_com.place(x = 400, y = 200)
                        start_game_b = Button(main, text = "Start Game!",font = ('quicksand', 15),
                        bg = mc, activebackground = mc, command = lambda: start_game_def(0))
                        start_game_b.place(x = 500, y = 500)
                        bat_bowl_str.set("Batting")
                        num_overs.set(1)
                
                                          
                    else:
                        print('loses')
                        rel = Label(main, text = "You Lost. Wait till the opponent starts the game", 
                        font = ('segoe ui', 18), bg = mc)
                        rel.place(x = 300, y = 30)
                        ran_overs = random.randint(1,6)
                        bob_ran = random.randint(1,2)
                        if bob_ran == 1:
                            time.sleep(3)
                            show = Label(main, text = f"""Opponent has choosen Bowling
                            Number of overs: {ran_overs}""", font = ('montserrat', 14))
                            show.place(x = 200, y = 200)
                            time.sleep(3)
                            start_game_def(1)
                        else:
                            time.sleep(3)
                            show = Label(main, text = f"""Opponent has choosen Batting
                            Number of overs: {ran_overs}""", font = ('montserrat', 14))
                            show.place(x = 200, y = 200)
                            time.sleep(3)
                            start_game_def(1)

                def rps_def2():
                    for widgets in main.winfo_children():
                        widgets.destroy()
                    point_l = Label(main, text = '', foreground = 'red', font = ('quicksand', 14))
                    point_l.place(x = 575, y = 350)

                    def rockdef2():
                        sam_l = Label(main, text = '<- You ', image = rock_img, compound = LEFT,
                        fg = 'black')
                        sam_l.place(x = 425, y = 200)
                        r_img = random.randint(1,3)
                        if r_img == 1:
                            rock_l = Label(main, image = rock_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            rock_l.place(x = 625, y = 200)
                            point_l.config(text = "It's a Tie")

                        if r_img == 3:
                            sci_l = Label(main, image = sci_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            sci_l.place(x = 625, y = 200)
                            print('Gets 1 point')
                            win_def(0)
                            

                        if r_img == 2:
                            paper_l = Label(main, image = paper_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            paper_l.place(x = 625, y = 200)
                            print('loses 1 point')
                            win_def(1)

                    def scidef2():
                        sam_l = Label(main, text = '<- You ', image = sci_img, compound = LEFT)
                        sam_l.place(x = 425, y = 200)
                        r_img = random.randint(1,3)
                        if r_img == 1:
                            rock_l = Label(main, image = sci_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            rock_l.place(x = 625, y = 200)
                            print('Gets 1 point')
                            point_l.config(text = 'Its a Tie')

                        if r_img == 3:
                            sci_l = Label(main, image = rock_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            sci_l.place(x = 625, y = 200)   
                            win_def(1)
                            

                        if r_img == 2:
                            paper_l = Label(main, image = paper_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            paper_l.place(x = 625, y = 200)
                            win_def(0)

                    def paperdef2():
                        sam_l = Label(main, text = '<- You ', image = paper_img, compound = LEFT)
                        sam_l.place(x = 425, y = 200)
                        r_img = random.randint(1,3)
                        if r_img == 1:
                            rock_l = Label(main, image = rock_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            rock_l.place(x = 625, y = 200)
                            win_def(0)

                        if r_img == 3:
                            sci_l = Label(main, image = sci_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            sci_l.place(x = 625, y = 200)
                            win_def(1)

                        if r_img == 2:
                            paper_l = Label(main, image = paper_img, compound = RIGHT, text = 'AI ->'
                            , fg = 'black')
                            paper_l.place(x = 625, y = 200)
                            point_l.config(text = "Its a Tie")
                        
                    rock_b = Button(main, image = rock_img, command = rockdef2, fg = 'black')
                    rock_b.place(x = 400, y = 400)
                    paper_b = Button(main, image = paper_img, command = paperdef2, fg = 'black')
                    paper_b.place(x = 550, y = 400)
                    sci_b = Button(main, image = sci_img, command = scidef2, fg = 'black')
                    sci_b.place(x = 700, y = 400)
                    
                rps_def2()
            
            intro = Label(main, text = "Hand Cricket", font = ('cambria', 30),
            bg = mc)
            intro.place(x = 400, y = 0)
            od_ev_l = Label(main, text = "Are you ready for Rock-paper-scissors Start?", bg = mc, font = ('quicksand', 15))
            od_ev_l.place(x = 200, y = 100)
            od_b_y = Button(main, text = "Yes", command = toss_def, bg = mc, 
            activebackground = mc, font = ('montserrat', 14))
            od_b_y.place(x = 200, y = 200)
            od_b_n = Button(main, text = "No", bg = mc, activebackground = mc,
            command = options_def, font = ('montserrat', 14))
            od_b_n.place(x = 200, y = 300)'''

        opened = Label(main, image = options_img)
        opened.place(x = 0, y = 0)
        math_b = Button(main, text = "Math",command = math_stuff,
        compound = RIGHT, font = ('calibri', 13), bg = mc, fg = 'black')
        math_b.place(x = 40, y = 130)
        rps_l = Button(main, text = "Rock-Papers-Scissors",
        font = ('abadi', 12), bg = mc, compound = RIGHT, activebackground = mc,
        command = rps_def, fg = 'black')
        rps_l.place(x = 40, y = 80)
        docs = Label(main, text = 'SS Inbuits', image = doc_img, font = ('calibri', 13),
        bg = mc, compound = RIGHT, fg = 'black')
        docs.place(x = 25, y = 30)
        docs_b = Button(main, text = "SS-DOCs",
        font = ('abadi', 12), bg = mc, compound = RIGHT, activebackground = mc,
        command = ssdoc, fg = 'black')
        docs_b.place(x = 40, y = 340)
        contacts = Button(main, text = "Contacts", activebackground = mc,
        command = contacts_def, bg = mc, font = ('abadi', 12), fg = 'black')
        contacts.place(x = 40, y = 390)
        period_table_b = Button(main, text = "Periodic Table", bg = mc, fg = 'black',
        font = ('abadi', 12), command = pt_def)
        period_table_b.place(x = 40, y = 180)
        calender_b = Button(main, text = "Callender", bg = mc, fg = 'black',
        font = ('abadi', 12), command = calender_def, activebackground = mc)
        calender_b.place(x = 40, y = 220)
        ticket_b = Button(main, text = "Travels", bg = mc, fg = 'black',
        font = ('abadi', 12), command = ticket_def, activebackground = mc)
        ticket_b.place(x = 40, y = 260)
        graph_b = Button(main, text = "Graphs", font = ('abadi', 12), command = graph_def,
        bg = mc, activebackground = mc, fg = 'black')
        graph_b.place(x = 40, y = 300)
        #oe_b = Button(main, text = "Hand Cricket (Not Functional)", font = ('abadi', 12),
        #bg = mc, activebackground = mc, fg = 'black')
        #oe_b.place(x = 250, y = 80)
        settings_b = Button(main, text = "Settings", activebackground = mc, 
        bg = mc, command = settings_def, font = ('calibri'),
        image = settings_img, compound = RIGHT, fg = 'black')
        settings_b.place(x = 25, y = 600)

    def google_def():
        for widgets in main.winfo_children():
            widgets.destroy()

        button_gmail.configure(bg = '#f0f0f0')
        button_calculator.configure(bg = '#f0f0f0')
        options_b.configure(bg = '#f0f0f0')
        google_b.config(bg = '#4FFFA1')
        time_b.config(bg = '#f0f0f0')

        def google_search_def(e):
            print('Nothing in there.')
            search_to = search_user.get(1.0, END)
            print(search_to)
            if search_to.strip() == '':
                pass
            else:
                g_frame = Frame(main, width = 500, height = 500, border = 12, bg = mc)
                g_frame.place(x = 500, y = 50)
                my_canvas = Canvas(g_frame, height = 500, width = 575)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                my_scrollbar = ttk.Scrollbar(g_frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
                ans_frame = Frame(my_canvas, width = 575, height = 500, bg = mc)
                my_canvas.create_window((0,0), window=ans_frame, anchor="nw")
                num = -1
                for j in googlesearch.search(search_to, tld="com", num=20, stop=20, pause=2):
                    def open_web(link = j):
                        webbrowser.open(link)
                    num += 1
                    if num % 2 == 0:
                        if len(j) > 50:
                            Button(ans_frame, text = j.strip(), font = ('calibri', 10), 
                            command = open_web, anchor = 'e', 
                            fg = '#DB4437', activeforeground = '#DB4437').pack( anchor = 'w')
                        else:
                            Button(ans_frame, text = j.strip(), font = ('calibri', 12), 
                            command = open_web, anchor = 'e', 
                            fg = '#DB4437', activeforeground = '#DB4437').pack( anchor = 'w')

                    else:
                        if len(j) > 50:
                            Button(ans_frame, text = j.strip(), font = ('calibri', 10), 
                            command = open_web, anchor = 'e', 
                            fg = '#0F9D58', activeforeground = '#0F9D58').pack( anchor = 'w')
                        else:
                            Button(ans_frame, text = j.strip(), font = ('calibri', 12), 
                            command = open_web, anchor = 'e', 
                            fg = '#0F9D58', activeforeground = '#0F9D58').pack( anchor = 'w')  


        def open_google():
            path = 'C:\Program Files (x86)\chromedriver.exe'
            driver = webdriver.Chrome(path)
            driver.get("https://www.google.com")
            inp = driver.find_element_by_name('q')
            inp.send_keys(search_user.get(1.0, END))                    

        search_user = Text(main, font = ("segoe ui", 16), fg = 'black',
        width = 30, height = 3)
        search_user.place(x = 100, y = 200)     
        search_user_l = Label(main, text = "Google Search: ", font = ("montserrat", 30), fg = '#0F9D58',
        bg = mc)
        search_user_l.place(x = 125, y = 100)
        search_user.bind("<Control-Shift-Return>", google_search_def)
        search_b = Button(main, text = "Search!", font = ('roboto mono', 14), bg = mc, 
        fg = '#4285F4', command = lambda: google_search_def('e'),
        activeforeground = '#4285F4', activebackground = mc)
        search_b.place(x = 175, y = 325)
        google_open_b = Button(main, text = "Open Google", font = ('roboto mono', 12),
        bg = mc, activebackground = mc, command = open_google, activeforeground = '#DB4437', fg = '#DB4437')
        google_open_b.place(x = 175, y = 375)


    def time_clock():
        for widgets in main.winfo_children():
            widgets.destroy()

        button_gmail.configure(bg = '#f0f0f0')
        button_calculator.configure(bg = '#f0f0f0')
        options_b.configure(bg = '#f0f0f0')
        google_b.config(bg = '#f0f0f0')
        time_b.config(bg = '#4FFFA1')
        show_l = Label(main, text = " ", bg = mc, image = time_img)
        show_l.place(x = 0, y = 0)
        tl = Label(main, text = "TIME", bg = mc, font = ('calibri', 45), fg = '#0F9D58')
        tl.place(x = 500, y = 100)
        time_l = Label(main, text = "", bg = mc, font = ('consolas', 35), fg = '#DB4437')
        time_l.place(x = 200, y = 250)
        
        format_string_time = '%A, %d %B %Y, %H:%M:%S'#.%f"'
        def show_time_def():
            a_datetime_datetime = datetime.datetime.now()
            current_time_string = a_datetime_datetime.strftime(format_string_time)      
            time_l.config(text = current_time_string)
            time.sleep(1)
            time_l.after(100, show_time_def)
        show_time_def()

    button_gmail = Button(taskbar, text = "Gmail", image = gmail_img, 
    compound = LEFT, padx = 18, font = button_font, fg = '#FF5100',
    activeforeground = '#FF5100', width=80, command = gmail_def)
    button_gmail.grid(row = 0, column = 1)

    button_calculator = Button(taskbar, text = "Calculator", image = cal_img,
    compound = LEFT, activeforeground = '#FF5100', fg = '#FF5100', width = 100,
    padx = 20, command = cal_def, font = button_font)
    button_calculator.grid(row = 0, column = 0)

    options_b = Button(taskbar, text = "Apps", image = options_img,
    compound = LEFT, activeforeground = 'brown', fg = 'brown', width = 100,
    padx = 10,  font = button_font, command = options_def)
    options_b.grid(row = 0, column = 4)

    google_b = Button(taskbar, text = "Google", image = g_img,
    compound = LEFT, activeforeground = 'brown', fg = 'brown', width = 100,
    padx = 10,  font = button_font, command = google_def)
    google_b.grid(row = 0, column = 5)

    time_b = Button(taskbar, text = "Time", image = time_img,
    compound = LEFT, activeforeground = 'brown', fg = 'brown', width = 100,
    padx = 10,  font = button_font, command = time_clock)
    time_b.grid(row = 0, column = 6)

    quit_b = Button(taskbar, activeforeground = 'red', fg = 'red', 
    width = 5, text = "×", font = ('calibri', 15),
    padx = 5, command = close_def)
    quit_b.grid(row = 0, column = 7)


def login_def():
    # version: 1.1
    def check(e):
        password = password_e.get()
        file = open(r'C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\Super UI system\reqs\info.txt', 'r')
        read_file = file.read()
        read_file = read_file.split()
        user_pass = read_file[2]
        err = Label(rt, text = "", font = ('ubuntu mono', 10), fg = 'red')
        if password == user_pass:
            main_function()
        else:
            err.config(text = "Invalid Password")
            err.place(x = 500, y = 400)

    user = Label(rt, text = "Super UI Login", font = ('montserrat', 20))
    user.place(x = 300, y = 0)
    password_e = Entry(rt, font = ('roboto mono', 18), show = '*')
    password_e.place(x = 500, y = 300)
    enter = Button(rt, text = "Login", font = ('quicksand', 13),
    command = lambda: check(1))
    rt.bind('<Return>', check)
    enter.place(x = 590, y = 330)
    ver_l = Label(rt, text = "Version: 1.1")
    ver_l.place(x = 800, y = 300)

#login_def()
main_function()
rt.mainloop()
