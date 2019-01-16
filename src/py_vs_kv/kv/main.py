from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import kivy
kivy.require('1.9.1')


class Tela1(BoxLayout):
    def on_press_bt(self):
        app.root_window.remove_widget(app.root)
        app.root_window.add_widget(Tela2())


class Tela2(BoxLayout):
    def on_press_bt(self):
        app.root_window.remove_widget(app.root)
        app.root_window.add_widget(Tela1())


class KVvsPY(App):
    def build(self):
        return Tela1()


app = KVvsPY()
app.run()
