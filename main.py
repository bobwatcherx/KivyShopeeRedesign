from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file("homescreen.kv")


class HomeScreen(MDScreen):
	pass


class MyApp(MDApp):
	def build(self):
		return HomeScreen()


if __name__ == "__main__":
	MyApp().run()

