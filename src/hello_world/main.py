from kivy.app import App
from kivy.uix.label import Label


def build():
    return Label(text="No more TKInter")


hello_world = App()
hello_world.build = build
hello_world.run()
