from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class GridLayoutDemo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        l1 = Label(
            text="Pls Click the Button"
        )
        self.add_widget(l1)
        self.bt1 = Button(
            text="I am Button",
            background_color=(0, 24, 67, 1),
            color=(0, 0, 0, 1),
        )
        self.add_widget(self.bt1)


class Demo(App):
    def build(self):
        return GridLayoutDemo()


app = Demo().run()
