from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import kivy
kivy.require('1.9.1')


class Tela1(BoxLayout):
    def on_press_bt(self):
        app.root_window.remove_widget(app.root)
        app.root_window.add_widget(Tela2())

    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt1 = Button(text="bt1")
        bt1.on_press = self.on_press_bt
        bt2 = Button(text="bt2")
        bt2.on_press = self.on_press_bt
        bt3 = Button(text="bt3")
        bt3.on_press = self.on_press_bt
        self.add_widget(bt1)
        self.add_widget(bt2)
        self.add_widget(bt3)


class Tela2(BoxLayout):
    def on_press_bt(self):
        app.root_window.remove_widget(app.root)
        app.root_window.add_widget(Tela1())

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = "vertical"
        voltar = Button(text="Voltar")
        voltar.on_press = self.on_press_bt
        self.add_widget(voltar)


class KVvsPY(App):
    def build(self):
        return Tela1()


app = KVvsPY()
app.run()
