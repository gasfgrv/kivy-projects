from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
import time
import kivy
kivy.require("1.10.1")


def self_kw(x):
    print('self keyword se refere ao widget')


Button.self_kw = self_kw


class Tela(BoxLayout):
    def root_kw(self):
        print('root keyword se refere à classe que é implementada')


class Estudo(App):
    def app_kw(self):
        print('app keyword se refere à classe da aplicação')


app = Estudo()
app.run()
