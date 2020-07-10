import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import send
import os
import sys

# The used version of kivy
kivy.require("1.11.1")


class LabelSroll(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)

        self.chat_log = Label(size_hint_y=None, markup=True)
        self.scroll_target = Label()

        self.layout.add_widget(self.chat_log)
        self.layout.add_widget(self.scroll_target)

    def update_chat_log(self, message):
        self.chat_log.text += '\n' + message
        self.layout.height = self.chat_log.texture_size[1] + 15
        self.chat_log.height = self.chat_log.texture_size[1]
        self.chat_log.text_size = (self.chat_log.width * 0.98, None)

        self.scroll_to(self.scroll_target)


class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # set the column number of the Grid layout
        self.cols = 1
        self.rows = 5

        title = GridLayout(cols=1)
        title.add_widget(Label(text="Distributed Messaging System ", ))
        self.add_widget(title,)



        space = GridLayout(cols=2)
        self.add_widget(space)

        username = GridLayout(cols=2)
        username.add_widget(Label(text="Username:"))
        # Get Username
        self.username_input = TextInput(multiline=False)
        username.add_widget(self.username_input)
        u_name = self.username_input.text
        self.add_widget(username)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)


    def join_button(self, instance):
        username = self.username_input.text

        information = "Attempting to join as the user name:" + username
        chat_instance.info.update_info(information)
        chat_instance.screen_manager.current = "Info_page"
        Clock.schedule_once(self.connect, 1)

    def connect(self, _):
        usernsame = self.username_input.text

        chat_instance.create_chat_page()
        chat_instance.screen_manager.current = "Chat"

class Info(GridLayout):
    def __init__(self, **kwards):
        super().__init__(**kwards)

        # set the column number of the Grid layout
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message_text_size = (self.message.width * 0.9, None)


