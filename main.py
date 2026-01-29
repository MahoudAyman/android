from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty


class HomeScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class CalcScreen(Screen):
    result = StringProperty("0")

    def add(self, value):
        if self.result == "0":
            self.result = value
        else:
            self.result += value

    def clear(self):
        self.result = "0"

    def calculate(self):
        try:
            self.result = str(eval(self.result))
        except:
            self.result = "خطأ"


class MyScreenManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        self.title = "My Smart App"
        return MyScreenManager()


if __name__ == "__main__":
    MyApp().run()
