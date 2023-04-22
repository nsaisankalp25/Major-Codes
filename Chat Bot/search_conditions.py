import more2
import more
from ChatBot import weather
import webbrowser

class search_method:
    def __init__(self, user_help_edit):
        self.user_help_edit = user_help_edit
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
            