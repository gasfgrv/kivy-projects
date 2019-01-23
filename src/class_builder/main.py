from kivy.app import App
import kivy
kivy.require("1.10.1")


code = """
BoxLayout:
    Button:
        text: "left"
    Button:
        text: "right"
"""

from kivy.lang import Builder

class Estudo(App):
    def build(self):
        return Builder.load_string(code)


app = Estudo()
app.run()
