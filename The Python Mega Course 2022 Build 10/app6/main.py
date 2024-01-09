from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior


Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction = "left"
        self.manager.current = "sign_up_screen"
    def ForgotPass(self):
        self.manager.transition.direction = "left"
        self.manager.current = "forgot_password_screen"
    def login(self, user, pword):
        self.manager.transition.direction = "left"
        with open("users.json") as file:
            users = json.load(file)
        if user in users and users[user]['password'] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong Username Or Password"

class RootWidget(ScreenManager):
    pass

class ForgotPasswordScreen(Screen):
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    def change_password(self, user, pword):
        with open("users.json", "r") as file:
            users = json.load(file)
        file.close()
        users[user]['password'] = pword
        if user in users:
            with open("users.json", "w") as file:
                json.dump(users, file)
            file.close()
            self.ids.username.text = ""
            self.ids.password.text = ""
            self.ids.state.text = "Password Changed!"
        else:
            self.ids.state.text = "This Username Does Not Exists"
        

class SignUpScreen(Screen):
    def add_user(self, user, pword):
        with open("users.json") as file:
            users = json.load(file)

            users[user] = {'username':user, 'password':pword,
            'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

            with open("users.json", "w") as file:
                json.dump(users, file)
            self.manager.current = "sign_up_screen_success"
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class SignUpScreenSuccess(Screen):
    def get_back(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        
        available_feelings = [Path(filename).stem for filename in
                                 available_feelings]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quotes.text = "Try another feeling :("

class ImageButton(ButtonBehavior, HoverBehavior, Image ):
    pass

    
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()