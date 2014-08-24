'''
Experiments with Kivy drawing.
'''
from math import sin, cos, pi

from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Line, Triangle, Mesh
from random import random as r
from functools import partial


class NodeViewApp(App):

    def add_node(self, label, f, count, *largs):
        label.text = str(int(label.text) + count)

        s = Scatter(do_rotation=False)
        # s.auto_bring_to_front = True
        # bbox=((0,0),(100,200)))

        with s.canvas:
            Color(0.3, 0.3, 0.3)
            Rectangle(size=(100, 400))

        # l = Label(
        #     text='[color=ffaaff]what?[/color]',
        #     markup=True)
        glayout = GridLayout(cols=2)
        glayout.add_widget(Button(text='Hello 1'))
        glayout.add_widget(Button(text='World 1'))
        glayout.add_widget(Button(text='Hello 2'))
        glayout.add_widget(Button(text='World 2'))
        s.add_widget(glayout)
        f.add_widget(s)

    def reset_rects(self, label, sf, *largs):
        label.text = '0'
        sf.clear_widgets()

    def build(self):
        # sf = ScatterLayout()
        sf = FloatLayout()
        label = Label(text='0')

        btn_add100 = Button(
            text='+ new node',
            on_press=partial(self.add_node, label, sf, 1))

        btn_reset = Button(
            text='Reset',
            on_press=partial(self.reset_rects, label, sf))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add100)
        layout.add_widget(btn_reset)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)
        root.add_widget(sf)

        return root

if __name__ == '__main__':
    NodeViewApp().run()
