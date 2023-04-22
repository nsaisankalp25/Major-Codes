import os
import colorama
from colorama import Fore, Style
import platform
import datetime
colorama.init(convert = True, autoreset = True)
print(Fore.BLUE + "New Updates about to Release, view the change log")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Python Terminal || Version == 0.9.9")
# SUCESS!
help_info = """
This terminal is made in Python 3.
Simple yet efficient terminal has many functions:
-------------------------------------
show - returns all the files and folders in the current directory
BREAK/QUIT/CLOSE -  closes the terminal
open 'xyz' - open with the specific file name opens that file ('xyz' = file); 
    > Note: xyz needs to be covered in SINGLE QUOTES
get - returns the specified information
    > 'info'/'help' - gives the information about the terminal
    > 'time'/'day'/'date' - gives the day-date-time
    > 'cwd'/'link' - gives the link of the current working directory
    > system-info - returns the information of the current local machine
goto xyz - changes the working directory to xyz
file - changes the specified information about the selected file
    > rename - renames the file (file rename 'xyz' to 'new_xyz')
    > delete - deletes the file (file delete 'xyz')
-------------------------------------
PYTHON TERMINAL MADE BY Sai Sankalp
-------------------------------------
VERSION == 0.9.9; Beta Version
-------------------------------------
"""

while True:
    cd = os.getcwd()
    user = input(Fore.YELLOW + Style.BRIGHT + "User:> ")
    user_items = user.split()
    open_thing = user[6: -1]
    new_thing = user[4:].strip().lower()
    if user_items.__len__() == 1:
        if user == "show":
            files = os.listdir(cd)
            print(Fore.RESET + Fore.CYAN + "Showing all the files and folders in the current working directory")
            for i, ii in enumerate(files):
                print(Fore.LIGHTMAGENTA_EX + f"{i}: {ii}")
        elif user == "BREAK" or user == "QUIT" or user == 'CLOSE':
            yrnclose = input(Fore.MAGENTA + "Are you sure you want to close [y/n]: ")
            if yrnclose.lower() in ['n', 'no']:
                print(Fore.GREEN + "Operation cancelled ")
            elif yrnclose.lower() in ['y', 'yes']:
                print(Fore.LIGHTBLUE_EX + "Terminal Session Ended -- Python Terminal || Version == 0.9.9")
                break
            else:
                print(Fore.MAGENTA + "Operation cancelled")
        elif user in ['cls', 'clear', 'clr']:
            try:
                try:
                    os.system('cls')
                except:
                    os.system('clear')
            except OSError:
                print(Fore.RED + "AN ERROR HAS OCCURED WHILE CLEARING THE SCREEN; PLEASE TRY AGAIN ")
        else:
            print(Fore.RED + "STATEMENT ENTERED IS NOT VALID; TRY AGAIN \n (check the statement again or enter 'help' to get help about the termial)")
    elif user_items[0] == "open":
        if open_thing in os.listdir():
            print(f"Opening {open_thing}...")
            os.system(f'"{open_thing}"')
            
        else:
            print(Fore.LIGHTRED_EX + f"File {open_thing} not found in the directory")

    elif user_items[0] == 'file':
        file_items = user.strip()
        file_items = file_items.split("'")
        print(file_items)
        old_name = file_items[1]
        if user_items[1] == 'rename':
            new_name = file_items[3]
            if old_name not in os.listdir():
                print(Fore.LIGHTRED_EX + f"File {old_name} not found")
            else:
                try:
                    os.rename(old_name, new_name)
                    print(Fore.CYAN + f"Successfully changed the file name to {new_name}")
                except OSError:
                    print(Fore.RED + "AN ERROR HAS OCCURED WHILE RENAMEING THE FILE; PLEASE TRY AGAIN ")
        elif user_items[1] == "delete":
            if old_name not in os.listdir():
                print(Fore.LIGHTRED_EX + f"File {old_name} not found")
            else:
                try:
                    yrn = input(Fore.BLUE + "Are you sure you want to delete the file? [y/n]: ")
                    if yrn.lower() in ['y', 'yes']:        
                        os.remove(old_name)
                        print(Fore.LIGHTMAGENTA_EX + f"Successfully removed {old_name}")
                    elif yrn.lower() in ['n', 'no']:
                        print(Fore.GREEN + "Operation cancelled ")
                    else:
                        print(Fore.LIGHTBLUE_EX + "Operation cancelled ")
                except OSError:
                    print(Fore.RED + "AN ERROR HAS OCCURED WHILE DELETING THE FILE; PLASE TRY AGAIN")
        else:
            print(Fore.LIGHTRED_EX + "Check the help prompt (type 'info' or 'help' to get help)")

    elif user_items[0] == 'new':
        if new_thing in ['ppt', 'powerpoint', 'powerpoint presentation', 'ppt doc']:
            print(Fore.LIGHTWHITE_EX + "Opening Power Point Presentation...")
            os.startfile("POWERPNT")
        elif new_thing in ["word doc", 'word', 'word document']:
            print(Fore.LIGHTWHITE_EX + "Opening Word Document...")
            os.startfile("WINWORD")
        elif new_thing in ["excel", 'xlsx', 'excel doc', 'excel document', 'spread sheets']:
            print(Fore.LIGHTWHITE_EX + "Opening Excel Sheets...")
            os.startfile('EXCEL')
        elif new_thing in ['cal', 'calculator', 'calc']:
            print(Fore.LIGHTWHITE_EX + "Opening Calculator...")
            os.startfile('calc')
        elif new_thing in ['notepad', 'notes']:
            print(Fore.LIGHTWHITE_EX + "Opening Notepad...")
            os.startfile('notepad')
        elif new_thing in ['google', 'chrome', 'google chrome', 'g-chrome']:
            print(Fore.LIGHTWHITE_EX + "Opening Google Chrome...")
            os.startfile('chrome')
        elif new_thing in ['edge', 'msedge', 'ms-edge', 'microsoft edge']:
            print(Fore.LIGHTWHITE_EX + "Opening Microsoft Edge...")
            os.startfile("msedge")
        elif new_thing in ['command prompt', 'cmd']:
            print(Fore.LIGHTWHITE_EX + "Opening Command Prompt...")
            os.startfile('cmd')
        elif new_thing in ['paint', 'mspaint', 'ms-paint', 'draw', 'sketch']:
            print(Fore.LIGHTWHITE_EX + "Opening Microsoft Paint...")
            os.startfile('mspaint')
        else:
            try:
                os.startfile(new_thing)
            except OSError:
                print(Fore.LIGHTRED_EX + "Cannot open given item/commmand")

    elif user_items.__len__() == 2:
        if user_items[0] == "get":
            if user_items[1] in ['cwd', 'link']:
                print(Fore.LIGHTGREEN_EX + cd)

            elif user_items[1] in ['time', 'day','date']:
                format_string_time = '%A, %d %B %Y, %H:%M:%S'
                current_time_string = datetime.datetime.now().strftime(format_string_time) 
                print(Fore.LIGHTGREEN_EX + current_time_string)
            elif user_items[1] in ['info', 'help']:
                print(Fore.LIGHTCYAN_EX + help_info)
            
            elif user_items[1] == 'system-info':
                system = platform.uname()
                print(Fore.BLUE + f"System: {system.system}")
                print(Fore.BLUE + f"Node Name: {system.node}")
                print(Fore.BLUE + f"Release: {system.release}")
                print(Fore.BLUE + f"Version: {system.version}")
                print(Fore.BLUE + f"Machine: {system.machine}")
                print(Fore.BLUE + f"Processor: {system.processor}")
            else:    
                print(Fore.LIGHTRED_EX + "Type 'get help' or 'get info' to get information about 'get'")


        elif user_items[0] == 'goto':
            if os.path.isdir(user_items[1]):
                try:
                    os.chdir(f"{cd}\\{user_items[1]}")
                except:
                    os.chdir(f"{user_items[1]}")
                finally:
                    print(Fore.YELLOW + "New working directory: " + os.getcwd())

            elif user_items[1] == "back" or user_items[1] == 'parentDir':
                os.chdir('../')
                print(Fore.YELLOW + "New working directory: " + os.getcwd())
            else:
                print(Fore.CYAN + Style.BRIGHT + f"{user_items[1]} --- does not exist in the current directory")
        else:
            print(Fore.RED + "STATEMENT ENTERED IS NOT VALID; TRY AGAIN \n (check the statement again or enter 'help' to get help about the termial)")
    
    else:
        print(Fore.RED + "STATEMENT ENTERED IS NOT VALID; TRY AGAIN")
        