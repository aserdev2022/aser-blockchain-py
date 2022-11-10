from kivy.app import App
from kivy.graphics import Color, Ellipse, Line, Rectangle
from random import randint
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        color = randint(0, 255)
        color1 = randint(0, 255)
        color2 = randint(0, 255)
        self.canvas.add(Color(rgb=(color / 255.0, color1 / 255.0, color2 / 255.0)))
        print(touch)
        d = 40
        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))
        #        self.canvas.add(Rectangle(pos=(touch.x + d, touch.y - d / 2), size=(d, d)))
        touch.ud['line'] = Line(pos=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):
    def build(self):
        rootWindow = Widget()
        self.painter = PaintWindow()
        claer_Button = Button(text='Clear')

        claer_Button.bind(on_release=self.clear_def)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(claer_Button)
        return rootWindow

    def clear_def(self, obj):
        self.painter.canvas.clear()


PaintApp().run()
