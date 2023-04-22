import os
import time
import tkinter
import tkinter.filedialog as fd
import random
import string

class password:
    def __init__(self, user_password):
        self.user_password = user_password
        print(self.user_password)
        self.help_list = []
        self.help_list2 = [False]
    

    def check_pass(self, usr_itout, password_user_sent) -> str:
        if usr_itout == True:
            self.user_password = password_user_sent
        elif usr_itout == False:
            self.user_password = self.user_password
        self.pass_len = len(self.user_password)
        self.case_up = []
        self.special_chars = []
        self.num_list = []
        self.contains_space = False
        self.isletter = []
        self.total = []
        for i in self.user_password:
            i = str(i)  
            if i.isnumeric():
                self.num_list.append(True)
            else:
                pass
            if i.isupper():
                self.case_up.append(True)
            else:
                pass
            if i in "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/\"":
                self.special_chars.append(True)
            else:
                pass
            if i == ' ':
                self.contains_space = True
            else:
                pass
            if i.isalpha(): 
                self.isletter.append(True)

        self.num_list = len(self.num_list)
        self.isletter = len(self.isletter)
        self.special_chars = len(self.special_chars)
        self.case_up = len(self.case_up)

        def checker():
            def Usr_check():
                def len_check():
                    if self.pass_len > 1 and self.pass_len < 4:
                        print("Length of password is VERY WEAK")
                        self.total.append(0)

                    elif self.pass_len > 4 and self.pass_len < 8:
                        print("Length of password is WEAK")
                        self.total.append(1)

                    elif self.pass_len > 8 and self.pass_len < 11:
                        print("Length of password is ACCEPTABLE")
                        self.total.append(2)

                    elif self.pass_len > 11 and self.pass_len < 15:
                        self.total.append(3)
                        print("Length of password is NORMAL")

                    elif self.pass_len > 15 and self.pass_len < 18:
                        self.total.append(4)
                        print("Length of password is STRONG")

                    elif self.pass_len > 18:
                        print("Length of password is VERY STRONG")
                        self.total.append(5)
                    
                def num_check():
                    
                    if self.num_list == 0:
                        self.total.append(0)
                        print("More than 2 numbers are expected to be in the password")
                    elif self.num_list == 1:
                        self.total.append(1)
                        print("More than 2 numbers are expected to be in the password")
                                
                    elif self.num_list == 2:
                        self.total.append(2)
                        print("Amount of numbers is good, but expected more numbers")
                    
                    elif self.num_list == 3:
                        self.total.append(4)
                        print("Amount of numbers is great")
                    
                    elif self.num_list >= 4:
                        self.total.append(5)
                        print("Amount of numbers is perfect")

                def case_check():
                    if self.case_up == 0:
                        self.total.append(0)
                        print("Atleast 2 Upper Case letters expected")
                    elif self.case_up == 1:
                        self.total.append(2)
                        print("Only 1 Upper Case letter Found, Expected more")
                    elif self.case_up == 2:
                        self.total.append(3)
                        print("Number of Upper Case letters is OK")
                    elif self.case_up == 3:
                        self.total.append(4)
                        print("Number of Upper Case letters is GREAT")
                    elif self.case_up >= 5:
                        print("Number of Upper Case Letters is PERFECT")
                        self.total.append(5)

                def special_check():
                    if self.special_chars == 0:
                        print("Expected 2+ Special charecters")
                        self.total.append(0)
                    elif self.special_chars == 1:
                        print("Expected 2+ Special charecters")
                        self.total.append(2)
                    elif self.special_chars == 2:
                        print("Amount of Special charecters is GOOD")
                        self.total.append(4)
                    elif self.special_chars >= 3:
                        print("Amount of Special charecters is PERFECT")
                        self.total.append(5)

                def space_check():
                    if self.contains_space == True:
                        print("Space not allowed in Password")
                        self.total.append(0)
                    else:
                        self.total.append(5)

                space_check()
                num_check()
                len_check()
                case_check()
                special_check()
            
            def True_check():
                def len_check():
                    if self.pass_len > 1 and self.pass_len < 4:

                        self.total.append(0)

                    elif self.pass_len > 4 and self.pass_len < 8:

                        self.total.append(1)

                    elif self.pass_len > 8 and self.pass_len < 11:

                        self.total.append(2)

                    elif self.pass_len > 11 and self.pass_len < 15:
                        self.total.append(3)


                    elif self.pass_len > 15 and self.pass_len < 18:
                        self.total.append(4)


                    elif self.pass_len > 18:

                        self.total.append(5)
                    
                def num_check():
                    
                    if self.num_list == 0:
                        self.total.append(0)

                    elif self.num_list == 1:
                        self.total.append(1)

                                
                    elif self.num_list == 2:
                        self.total.append(2)

                    
                    elif self.num_list == 3:
                        self.total.append(4)

                    
                    elif self.num_list >= 4:
                        self.total.append(5)

                def case_check():
                    if self.case_up == 0:
                        self.total.append(0)
                    elif self.case_up == 1:
                        self.total.append(2)

                    elif self.case_up == 2:
                        self.total.append(3)

                    elif self.case_up == 3:
                        self.total.append(4)

                    elif self.case_up >= 5:

                        self.total.append(5)

                def special_check():
                    if self.special_chars == 0:

                        self.total.append(0)
                    elif self.special_chars == 1:

                        self.total.append(2)
                    elif self.special_chars == 2:

                        self.total.append(4)
                    elif self.special_chars >= 3:

                        self.total.append(5)

                def space_check():
                    if self.contains_space == True:
                        self.total.append(0)
                    else:
                        self.total.append(5)

                space_check()
                num_check()
                len_check()
                case_check()
                special_check()
            if usr_itout == False:
                Usr_check()
            elif usr_itout == True:
                True_check()

        checker()

        self.total_sum = sum(self.total)
        self.total_sum = ((self.total_sum/len(self.total)*5)*10)/2.5
        if usr_itout == True:
            try:
                self.help_list.clear()
            except:
                pass
            try:
                self.help_list2.clear()
            except:
                pass


            self.help_list.append(self.total_sum)
            self.help_list2.append(True)
        elif usr_itout == False:
            print(f'Total Acceptance Rate: {self.total_sum}%')

    def generate_pass(self):
        if self.help_list2[0] == False:
            print("A Strong password will be generated soon...")
            time.sleep(1)
        elif self.help_list2[0] == True:
            pass
        else:
            pass
        list_pass = []
        def pass_make():
            for i in range(17):
                ran = random.choice(string.ascii_letters + string.digits + "!@$%&_")
                list_pass.append(ran)
        pass_make()
        self.check_pass(True, "".join(list_pass))
        if self.help_list[0] > 90:
            print("Password: " + "".join(list_pass))
        else:
            self.generate_pass()

#Periodic Table
class periodic_table():
    def __init__(self):
        def help_table(num: int):
            if num == 1:
                info = """
                The Atomic number is the number of protons in the nucleus of an atom
                The Atomic name is the name given to an Element in the periodic table
                The Atomic symbol is the abbreviation given to the Elements in the periodic table
                The Periodic table was invented by Dmitri Mendeleev in the year 1869,
                but the table has gone through multiple changes
                """
                print(info)
            else:
                break_state = []
                
                print("Bot: Enter Symbol or Name or Number to get the Element")            
                self.user_in = input("User: ")
                for i in elements_list:
                    i.strip('\n')
                    i = i.split()
                    if self.user_in.lower() in i:
                        i = str(i).replace("'", "").replace("[", '').replace(']', '')
                        break_state.append(i)
                    else:
                        break_state.append(True)
                self.break_state2 = False
                for i in break_state:
                    if i != True:
                        print(f"Bot: {i}")
                        self.break_state2 = False
                        break
                    else:
                        self.break_state2 = True
                if self.break_state2 == True:                    
                    print(f"Bot: Couldn't find anything that matches {self.user_in}")

        self.file_open = open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\reqs\elements.txt", 'r')
        self.file = self.file_open.readlines()
        elements_list = []                
        for i in self.file:
            i = i.rstrip()
            i = i.lstrip()
            i = i.replace('\n', ' ')
            i = i.replace('\t', ' ')
            elements_list.append(i)
        for i in elements_list:
            print(i)

        print("Bot: Any Help with the table? ")
        self.yrn = input("User: ")
        if self.yrn.lower().strip() == 'yes' or self.yrn.lower().strip() == "yeah" or self.yrn.lower().strip() == 'yep':
            self.info_string = """ Bot:
            Enter 1 to know about the periodic table
            Enter 2 to search any elements -> """
            self.what_help = input(self.info_string)
            try:
                self.what_help = int(self.what_help)
            except ValueError:
                print(f"Bot: Expected Numbers (1,2) but got {self.what_help}")
            help_table(self.what_help)
        else:
            print("ok")

#File Explorer and Open    
class open_file():
    def __init__(self):
        print('Bot: Enter the name of the application to be opened')
        print("Bot: Shortcuts to open \n Enter 1 to open PPT \n 2: Word Doc \n 3: Excel \n 4: NotePad \n 5: Google Chrome \n 6: IE, MS-EDGE \n 7: Calculator \n 8: Command Prompt \n 9: MS-Paint \n 10: Python Interpreter Shell \n 0: File Selector")
        self.user_inp = input("User: ")
        self.user = self.user_inp.lower().split()
        def realistic(opened):
            print(f"Bot: Opening {opened}")
            time.sleep(0.5)
            print("Bot: .")
            time.sleep(0.5)
            print("Bot: .")
            time.sleep(0.5)
            print("Bot: .")
            time.sleep(0.5)

        if self.user_inp == '1' or "ppt" in self.user or 'power point' in self.user_inp.lower():
            realistic('Microsoft Power Point Presentation')
            os.startfile("POWERPNT")
        elif self.user_inp == '2' or 'word doc' in self.user_inp or 'word' in self.user:
            realistic("Microsoft Word Document")
            os.startfile("WINWORD")
        elif self.user_inp == '3' or 'excel' in self.user:
            realistic("Microsoft Excel Sheets")
            os.startfile("EXCEL")
        elif self.user_inp == '4' or 'notepad' in self.user:
            realistic("NotePad")
            os.startfile('notepad')
        elif self.user_inp == '5' or 'chrome' in self.user or 'google' in self.user:
            realistic("Google Chrome")
            os.startfile('chrome')
        elif self.user_inp == '6' or 'ie' in self.user or 'edge' in self.user or 'msedge' in self.user:
            realistic("Microsoft Edge")
            os.startfile("msedge")
        elif self.user_inp == '7' or 'cal' in self.user or 'calculator' in self.user:
            realistic("Calculator")
            os.startfile('calc')
        elif self.user_inp == '8' or 'cmd' in self.user or 'command prompt' in self.user_inp.lower():
            realistic("Command Prompt")
            os.startfile('cmd')
        elif self.user_inp == '9' or 'paint' in self.user or 'ms paint' in self.user_inp.lower():
            realistic("Microsoft Paint")
            os.startfile("mspaint")
        elif self.user_inp == '0' or 'file selector' in self.user:
            realistic('File Selector')
            rt = tkinter.Tk().withdraw()
            filename = fd.askopenfile()
            try:
                os.startfile(filename.name)
            except:
                print("Bot: There was an error in opening the file, please try again.")
        elif self.user_inp == '10' or 'python' in self.user:
            os.startfile("C:\\Users\\Vinod-2018\\Desktop\\TOTAL SAI THINGS\\sai stuff\\Sai Programming\\Python\\New folder\\Lib\\idlelib\\idle.pyw")
        else:
            try:
                realistic(self.user_inp)
                try:
                    os.startfile(self.user_inp)
                except: 
                    print("Bot: There was an error in opening the file or the file doesn't exist")
            except os.error:
                print(f"Bot: No such application called: {self.user_inp}")
                print("Bot: Do you want to try again? (y\\n) ")
                self.yrn = input("User: ")
                if self.yrn == 'y' or self.yrn == 'yes':
                    open_file()
                else:
                    print("Bot: Sorry that I wasn't able to open...")
