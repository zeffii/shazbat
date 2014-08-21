'''
Experiments with Kivy drawing.
'''
from math import sin, cos, pi

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Line, Triangle, Mesh
from random import random as r
from functools import partial


def make_theme():
    ''' alternative, import obj literal from file.. '''
    theme = lambda: None
    theme.row_height = 20

    theme.text = lambda: None
    theme.text.height = 14
    theme.text.color = (0.3, 0.7, 0.7)

    theme.body = lambda: None
    theme.body.radius = 10
    theme.body.radius_div = 20

    theme.header = lambda: None
    theme.header.height = 20
    theme.header.color = (0.5, 0.7, 0.5)

    theme.border = lambda: None
    theme.border.color = (0.9, .9, .9)
    return theme


def make_node_specs():
    node_specs = lambda: None
    node_specs.width = 150
    node_specs.rows = 9
    node_specs.body_color = (0.3, 0.4, 0.6)
    return node_specs

theme = make_theme()
node_specs = make_node_specs()


def get_arc_thetas(num, arc_start):
    theta = 0.5 * pi / num
    return [(theta*j) + arc_start for j in range(num+1)]


def arc(pos, r, thetas):
    x, y = pos
    pts = []
    pts.extend([x, y, 0, 0])
    for arc_angle in thetas:
        pt = [x+cos(arc_angle)*r, y+sin(arc_angle)*r, 0, 0]
        pts.extend(pt)
    indices = [i for i in range(len(thetas)+1)]
    return pts, indices


def arclight(pos, r, thetas):
    x, y = pos
    pts = []
    for arc_angle in thetas:
        pt = [x+cos(arc_angle)*r, y+sin(arc_angle)*r]
        pts.extend(pt)
    return pts


def draw_rounded_rect(pos, col, dims, div):
    thetas1 = get_arc_thetas(div, 0)
    thetas2 = get_arc_thetas(div, 0.5*pi)
    thetas3 = get_arc_thetas(div, pi)
    thetas4 = get_arc_thetas(div, 1.5*pi)
    pts = []
    x, y = pos
    pts.extend(arclight(pos=(x+dims.w-dims.r, y), r=dims.r, thetas=thetas1))
    pts.extend(arclight(pos=(x+dims.r, y), r=dims.r, thetas=thetas2))
    pts.extend(arclight(pos=(x+dims.r, y-dims.h), r=dims.r, thetas=thetas3))
    pts.extend(arclight(pos=(x+dims.w-dims.r, y-dims.h), r=dims.r, thetas=thetas4))

    Color(*col)
    Line(points=pts, width=1, close=True)


def draw_half_rr(pos, direction, dims, col, div):
    x, y = pos
    Color(*col)
    r, hh, width = dims.r, dims.h, dims.w

    draw_y_buffer = hh > r
    if r > hh:
        r = hh

    if direction == 'up':
        start1 = 0.5*pi
        start2 = 0
    elif direction == 'down':
        start1 = pi
        start2 = 1.5*pi

    # horizontal indicator
    # Line(points=[x, y, x-20, y])

    # arc
    thetas = get_arc_thetas(div, start1)
    verts, indices = arc((x+r, y), r, thetas)
    Mesh(vertices=verts, indices=indices, mode='triangle_fan')

    # rect
    if direction == 'up':
        Rectangle(pos=(x+r, y), size=(width-(2*r), r))
        if draw_y_buffer:
            Rectangle(pos=(x, y-hh+r), size=(width, hh-r))

    if direction == 'down':
        Rectangle(pos=(x+r, y-r), size=(width-(2*r), r))
        if draw_y_buffer:
            Rectangle(pos=(x, y), size=(width, hh-r))

    # arc
    thetas = get_arc_thetas(div, start2)
    verts, indices = arc((x+width-r, y), r, thetas)
    Mesh(vertices=verts, indices=indices, mode='triangle_fan')


def draw_buttons(pos):
    layout = FloatLayout(size=(300, 300))
    # layout = BoxLayout(orientation='vertical')
    # layout.width = 200
    # layout.height = 100
    btn1 = Button(text='Hello')
    btn2 = Button(text='World')
    layout.add_widget(btn1)
    layout.add_widget(btn2)
    pass


class StressCanvasApp(App):

    def add_node_background(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:

            x, y = xy = (int(r() * wid.width + wid.x), int(r() * wid.height + wid.y))
            width = node_specs.width
            height = node_specs.rows * theme.row_height
            radius = theme.body.radius
            header = theme.header.color
            body = node_specs.body_color
            div = theme.body.radius_div
            border_col = theme.border.color

            dims = lambda: None
            dims.r = radius
            dims.h = theme.header.height
            dims.w = width
            draw_half_rr(
                pos=(x, y+height-radius),
                direction='up', dims=dims, col=header, div=div)

            dims2 = lambda: None
            dims2.r = radius
            dims2.h = height - (theme.header.height)
            dims2.w = width
            draw_half_rr(
                pos=(x, y+radius),
                direction='down', dims=dims2, col=body, div=div)

            # Line(rectangle=[x, y, width, height])
            dims3 = lambda: None
            dims3.r = radius
            dims3.h = height - (theme.header.height)
            dims3.w = width
            draw_rounded_rect(
                pos=(x, y+height-radius), col=border_col, dims=dims3, div=div)

            # draw_buttons(pos=xy)

    def reset_rects(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        wid = Widget()

        label = Label(text='0')

        btn_add100 = Button(
            text='+ new node',
            on_press=partial(self.add_node_background, label, wid, 1))

        btn_reset = Button(
            text='Reset',
            on_press=partial(self.add_node_background, label, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add100)
        layout.add_widget(btn_reset)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root

if __name__ == '__main__':
    StressCanvasApp().run()
