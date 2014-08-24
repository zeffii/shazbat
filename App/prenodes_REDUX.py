'''
Experiments with Kivy drawing.
'''
from math import sin, cos, pi

from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Line, Triangle, Mesh
from random import random as r
from functools import partial

def tc(*args):
    ''' usage: 
            tc(('ff3333', 'Hello '), ('aaeeff', 'World')) 
        returns:
            formatted using appropriate markup
    '''
    sumtext = ''
    for col, text in args:
        props = {
            'col': col if col else 'ffffff',
            'text': text if text else '_'}
        sumtext += '[color={col}]{text}[/color]'.format(**props)
    return sumtext


class NodeViewApp(App):

    def add_node(self, label, f, count, *largs):
        label.text = str(int(label.text) + count)

        s = Scatter()
        with s.canvas:
            Color(0.3, 0.3, 0.3)
            Rectangle(size=(400, 100))

        l = Label(
            text=tc(('ff3333', 'Hello '), ('aaeeff', 'World')),
            markup=True)

        s.add_widget(l)
        f.add_widget(s)            

    def reset_rects(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        wid = Widget()
        f = FloatLayout()
        wid.add_widget(f)

        label = Label(text='0')

        btn_add100 = Button(
            text='+ new node',
            on_press=partial(self.add_node, label, f, 1))

        btn_reset = Button(
            text='Reset',
            on_press=partial(self.add_node, label, f))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add100)
        layout.add_widget(btn_reset)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root

if __name__ == '__main__':
    NodeViewApp().run()
