from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class FloatLayoutDemo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bt1 = Button(
            text="Button",

        )
        self.add_widget(bt1)


class Demo(App):
    def build(self):
        return FloatLayoutDemo()


app = Demo().run()
