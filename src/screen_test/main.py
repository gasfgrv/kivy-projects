from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.window import Window


def click():
    print(txt.text)
    txt.text = ""


def build():
    layout = FloatLayout()
    global txt
    txt = TextInput(text="Teste")
    txt.size_hint = None, None
    txt.height = 300
    txt.width = 400
    txt.y = 250
    txt.x = 60

    btn = Button(text="Clique Aqui")
    btn.size_hint = None, None
    btn.width = 200
    btn.height = 50
    btn.y = 150
    btn.x = 170
    btn.on_press = click
    layout.add_widget(txt)
    layout.add_widget(btn)

    return layout


Window.size = 525, 600

app = App()
app.title = "teste"
app.build = build
app.run()
