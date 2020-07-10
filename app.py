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
