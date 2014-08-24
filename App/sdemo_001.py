from kivy.app import App
from kivy.graphics import Color, Rectangle, Line, Triangle, Mesh

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


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


class NodeView(App):
    def build(self):
        b = BoxLayout(orientation='vertical')

        f = FloatLayout()
        s = Scatter()

        f.add_widget(s)

        with s.canvas:
            Color(0.3, 0.3, 0.3)
            Rectangle(size=(250, 500))

        l = Label(
            text=tc(('ff3333', 'Hello '), ('aaeeff', 'World')),
            markup=True)
        s.add_widget(l)

        b.add_widget(f)
        return b

if __name__ == "__main__":
    NodeView().run()
