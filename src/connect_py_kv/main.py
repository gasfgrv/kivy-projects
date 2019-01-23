from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import time
import kivy
kivy.require("1.10.1")


class Tela(BoxLayout):
    def on_click(self):
        self.ids.lb1.text = time.strftime("%d/%m/%Y")
        self.ids.lb2.text = time.strftime("%I:%M:%S")


class Estudo(App):
    pass


app = Estudo()
app.run()
