from kivy.app import App
from kivy.uix.button import Button


def click():
    print('Hello')

def buid():
    btn = Button(text="Click Here")
    btn.on_press = click
    return btn

app = App()
app.build = buid
app.run()