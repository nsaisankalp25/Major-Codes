import datetime
import requests
from bs4 import BeautifulSoup
import webbrowser, googlesearch
import more
import more2

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather():         
    city_inp = input("Enter the Name of City ->  ")
    if city_inp == "" or city_inp == " ":
        city_inp = 'Dubai'
    city = city_inp+" weather"
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(weather+"°C")
    print(f"{int(weather)*(9/5)+32} °F")

class chatbot():
    def __init__(self):
            pass
    def greet(self):
        self.gc = "Great Fine good awesome super not no well nice perfect super healthy bad sick"
        print("Bot: Hi! How are you doing?")
        self.user = input("User: ")
        self.break_yrn = False
        def search_keywords():
            for i in self.gc.split():
                self.question = self.user.lower().replace("?", '').replace(".", '').replace(',', '').replace("!", '').split()
                if i.lower() in self.question and i != 'not' or i.lower() in self.question and i != 'no' or i.lower() in self.question and i != 'bad' or i.lower() in self.question and i != 'sick':
                    print('Bot: Great! \n How can I help you?')
                    self.break_yrn = False
                    break
                else:
                    if self.user.split()[0] == 'not' or self.user.split()[0] == 'no':
                        self.break_yrn = True
                        break
            if self.break_yrn == True:
                print("Bot: Oh, Take Care...")
                print("Bot: Is there any way that I can help you?")
                self.help_bot()
            else:
                self.help_bot()
        if "not bad" in self.user.lower() or 'not sick' in self.user.lower() or 'not ill' in self.user.lower():
            print('Bot: Great! \n How can I help you? ')
            print("Bot:     type INFO to know about the chatbot")
            self.help_bot()
        else:
            search_keywords()   
    def help_bot(self):
        self.user_help = input("User: ")
        self.user_help_edit = self.user_help.lower().replace("?", '').replace(".", '').split()
        if "time" in self.user_help_edit or "date" in self.user_help_edit or "day" in self.user_help_edit:
            more2.help_bot_add.time_def(self)

        elif "weather" in self.user_help_edit or 'condition' in self.user_help_edit or "temperature" in self.user_help_edit:     
            weather()

        elif "google" in self.user_help_edit or "open google" in self.user_help_edit or "search google" in self.user_help_edit:
            more2.help_bot_add.google(self)

        elif 'math' in self.user_help_edit or 'maths' in self.user_help_edit or 'mathematics' in self.user_help_edit:
            more2.help_bot_add.math_function(self)

        elif "periodic table" in self.user_help.lower().replace("?", '').replace(".", ''):
            more.periodic_table()

        elif "password" in self.user_help_edit:
            print("Bot: Password Generator(1) or Checker(2) ?")
            self.u1or2 = input("User: ")
            if self.u1or2.lower().strip() == "generator" or self.u1or2.lower().strip() == '1':
                more.password('').generate_pass()
            
            elif self.u1or2.lower().strip() == "checker" or self.u1or2.lower().strip() == '2':
                print("Bot: Enter the password to be tested: ")
                self.user_pass = input("User: ")
                more.password(self.user_pass).check_pass(False, False)
            else:
                print("Bot: Only Password Generator and Checker Available")

        elif "open" in self.user_help_edit:
            more.open_file()

        elif "convert" in self.user_help_edit or "converter" in self.user_help_edit:
            print("Bot: Select The Type of Converter")
            print("""
            1: Temperature
            2: Distance
            """)
            self.which = input("User: ")
            try:
                self.which = int(self.which)
                if self.which > 2:
                    print("Bot: Number selected is exceded, will be taking conversion 1")
                    self.which = 1
                else:
                    pass
            except ValueError:
                print("Bot: Only numbers allowed")
            if self.which == 1:
                more2.temperature()
            elif self.which == 2:
                more2.distance()

        elif "notes" in self.user_help_edit:
            #more2.sticky_notes()
            ''
        
        elif "info" in self.user_help_edit:
            more2.function_show()

        else:
            print("Bot: Oh, I dont know the answer. \n Would you like me to google that? ")
            self.user_yrn = input("Bot: Yes or No ")
            if self.user_yrn.lower() == 'yes':
                webbrowser.open(self.user_help)
            else:
                print("Bot: I'm Sorry that I wasn't able to help")
            

bot = chatbot()
bot.greet()
