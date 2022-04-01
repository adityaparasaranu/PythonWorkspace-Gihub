from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class Demo(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x="left",
            anchor_y="top"
        )
        btn1 = Button(
            text="Anchor Layout Demo",
            size_hint=(.2, .2),
            background_color=(0.0, 25, .86, 1.0),
            color=(0, 0, 0, 1),
        )
        btn1.bind(on_press=self.clicking)
        layout.add_widget(btn1)
        return layout

    def clicking(self, event):
        for i in range(10):
            print(i)


app = Demo()
app.run()
