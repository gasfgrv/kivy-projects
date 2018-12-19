from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    ti = TextInput()
    ti.text = "Entrada de Texto"
    return ti


app = App()
app.build = build
app.run()

