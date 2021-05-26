
from kivy.core.window import Window
from kivy.config import Config
from kivy.app import App
from kivy.app import App
from kivy.uix.label import Label


Config.window_icon = "icon.png"
class KivyApp(App):
    def build(self):
        self.icon = 'icon.png'
        self.title = "Mj App"
        label = Label(text='Testing ...',
                      size_hint=(.1, .1),
                      pos_hint={'center_x': .1, 'center_y': .1})

        return label

if __name__ == '__main__':
    app = KivyApp()
    app.run()