from kivy.app import App
from kivy.core.window import ObjectProperty
from kivy.uix.label import Label

# importing the kv file
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

Builder.load_file("./main.kv")


class FlappyApp(App):
    def build(self):
        game = FlappyGame()
        return game


class FlappyGame(Widget):
    player = ObjectProperty()
    obsitcales = ObjectProperty()


if "__main__" == __name__:
    FlappyApp().run()
