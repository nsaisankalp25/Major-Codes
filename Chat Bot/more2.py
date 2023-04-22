import datetime
from mysql.connector.errors import DatabaseError
import requests
from bs4 import BeautifulSoup
import webbrowser, googlesearch
import tkinter
from tkinter import *
import mysql.connector
# Temperature Converting Class
class temperature:
    def __init__(self):
        print("Bot: Convert any temperature.")
        print("""Bot: Enter the Number of the conversion
        1: Kelvin - Celsius 
        2: Kelvin - Fahrenheit
        3: Fahrenheit - Celsius
        4: Celsius - Fahrenheit 
        5: Fahrenheit - kelvin
        6: Celsius - Kelvin 
        """)
        self.which = input("User: ")
        try:
            self.which = int(self.which)
            if self.which > 6:
                print("Bot: Only Conversions 1-6 allowed \n Will be taking Conversion 1")
                self.which = 1
            else:
                pass
        except ValueError:
            print("Bot: Only Numbers are allowed")
        self.conversion_func()
    
    def conversion_func(self):
        print('Bot: Enter number to bo converted')
        num = input("User: ")
        try:
            self.num = float(num)
        except ValueError:
            print("Bot: Only numbers allowed")
            self.num = 0
        
        if self.which == 1:
            print('Bot: Converting Kelvin - Celsius')
            print(f"Bot: {self.num-273.15}")

        elif self.which == 2:
            print('Bot: Converting Kelvin - Fahrenheit')
            print(f"Bot: {(self.num - 273.15) * 9/5 + 32 }")
        
        elif self.which == 3:
            print('Bot: Converting Fahrenheit - Celsius')
            print(f"Bot: {(self.num - 32) * 5/9}")
        
        elif self.which == 4:
            print('Bot: Converting Celsius - Fahrenheit')
            print(f"Bot: {(self.num * 9/5) + 32  }")
        
        elif self.which == 5:
            print('Bot: Converting Fahrenheit - kelvin')
            print(f"Bot: {(self.num - 32) * 5/9 + 273.15}")
        
        elif self.which == 6:
            print('Bot: Converting Celsius - Kelvin')
            print(f"Bot: {self.num + 273.15}")

# Distance Converting Class
class distance:
    def __init__(self):
        num1 = input('Enter the value: ')
        unit1 = input('Which unit do you want it converted from:  ')
        unit2 = input('Which unit do you want it converted to: ')
        if unit1 == "cm" and unit2 == "m":
            ans = float(num1)/100
            print(ans)
        elif unit1 == "mm" and unit2 == "cm":
            ans = float(num1)/10
            print(ans)
        elif unit1 == "m" and unit2 == "cm":
            ans = float(num1)*100
            print(ans)
        elif unit1 == "cm" and unit2 == "mm":
            ans = float(num1)*10
            print(ans)
        elif unit1 == "mm" and unit2 == "m":
            ans = float(num1)/1000
            print(ans)
        elif unit1 == "m" and unit2 == "mm":
            ans = float(num1)*1000
            print(ans)
        elif unit1 == "km" and unit2 == "m":
            ans = float(num1)*1000
            print(ans)
        elif unit1 == "m" and unit2 == "km":
            ans = float(num1)/1000
            print(ans)
        elif unit1 == "mm" and unit2 == "km":
            ans = float(num1)/1000000
            print(ans)
        elif unit1 == "ft" and unit2 == "cm":
            ans = float(num1)*30.48
            print(ans)
        elif unit1 == "ft" and unit2 == "mm":
            ans = float(num1)*304.8
            print(ans)
        elif unit1 == "ft" and unit2 == "inch":
            ans = float(num1)*12
            print(ans)
        elif unit1 == "inch" and unit2 == "cm":
            ans = float(num1)*2.54
        elif unit1 == "inch" and unit2 == "mm":
            ans = float(num1)*25.4

class help_bot_add:       
    def __init__(self):
        pass

    def time_def(self):
        format_string_time = '%H:%M:%S | %A, %d %B %Y'
        a_datetime_datetime = datetime.datetime.now()
        self.current_time = a_datetime_datetime.strftime(format_string_time)      
        print(f"The Current time is: {self.current_time}")

    def math_function(self):
        def math_expression():
            print("Bot: Enter the math expression")
            self.user_math = input("User: ")
            try: 
                print(eval(self.user_math))
            except:
                print("Bot: Oops, Could'nt solve that.")

        def interest_finder():
            print("Bot: Enter 1 for Simple interest \n 2 for compound interest")
            again1or2 = input("User: ")
            def SI():
                print("Bot: Enter the Following")
                P = float(input("Principal Amount(P): "))
                R = float(input("Ratio of Interest(R): "))
                T = float(input("Number of Years(T): "))
                print(f"Bot: Simple Interest {P*T*R}")
                print(f"Bot: Interest Amount {(P*T*R)-P}")
            def CI():
                print("Bot: Enter the Following")
                P = float(input("Principal Amount(P): "))
                R = float(input("Ratio of Interest(R): "))
                N = float(input("Number of Years(n): "))
                print(f"Bot: Compound interest {((P*(1+(R))**N))}")
                print(f"Bot: Interest amount {((P*(1+R)^N) - P)}")

                

            try:
                num2 = int(again1or2)
                if num2 == 1:
                    SI()
                elif num2 == 2:
                    CI()
                else:
                    print("Only Numbers 1 or 2 to be entered")
            except:
                print("Only Numbers to be entered")


        print("Bot: Enter 1 for Math Expression solver \n 2 for Interest Finder")
        self.num1or2 = input("User: ")
        try:
            self.numusr = int(self.num1or2)
            if self.numusr == 1:
                math_expression()
            elif self.numusr == 2:
                interest_finder()
            else:
                print('Bot: Only 2 functions available')

        except: print("Bot: Only enter numbers 1 or 2")
            

        

    def google(self):
        def open_web(link):
            webbrowser.open(link)

        self.search_to = input("User: Google Search: ")
        self.link_list = []
        self.num = 1
        for j in googlesearch.search(self.search_to, tld="com", num=20, stop=20, pause=2):
            print(f'{self.num}) {j}')
            self.num += 1
            self.link_list.append(j)

        print('Bot: Enter Link Number (enter NONE to cancel): ')
        self.open_link = input("User: ")
        if self.open_link.lower() == "none":
            pass
        else:
            try:
                open_link = int(self.open_link)-1
            except:
                print("Bot: Only Numbers expected")
            open_web(self.link_list[open_link])  

class sticky_notes():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'sai25withpython@mysql',
            database = 'chatbot_database'
        )
        self.cursorsql = self.mydb.cursor()
        self.formula = "something lol"
        self.cursorsql.execute("select * from chatbot_database.notes_cb")   
        for i in self.cursorsql:
            print(i)


def function_show():
    string = """
    Bot:
    The things that are available in the chatbot is
    1) Time
    2) Weather
    3) Google
    4) Math
    5) Periodic Table
    6) Password Generator/checker
    7) File Opener
    8) Unit Conversions
    More will be added soon... 
    """
    print(string)