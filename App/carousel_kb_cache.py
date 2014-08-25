import sys
import os
import kivy
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.core.window import Window


class MainApp(object):

    def __init__(self, argv):
        self.args = argv
        self.parametrics()

    def parametrics(self):
        alternate_directory = (len(self.args) == 2)

        print(repr(alternate_directory))

        path_to_read = self.args[1] if alternate_directory else os.curdir
        path_list = os.listdir(path_to_read)
        ok = {'jpg', 'png'}  # , 'gif'}
        base_path = os.path.abspath(path_to_read)

        r = [i for i in path_list if i.lower()[-3:] in ok]
        if alternate_directory:
            r = [os.path.join(base_path, i) for i in r]

        self.filenames = r


class Example1(App):

    def build(self):

        self.additional_init()
        self.carousel = Carousel(direction='right', loop=True)

        for src in k.filenames:
            image = Factory.AsyncImage(source=src, allow_stretch=True)
            self.carousel.add_widget(image)
        return self.carousel

    def additional_init(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _print_debug(self, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self._print_debug(keycode, text, modifiers)

        # If we hit escape, release the keyboard
        k = keycode[1]
        if k == 'escape':
            keyboard.release()

        if k == 'right':
            self.carousel.load_next()
            pass
        if k == 'left':
            self.carousel.load_previous()
            pass

        return True


if __name__ == '__main__':
    '''
    >> kivy carousel.py
       - (for current dir, ie .py is located in same dir as images)
    >> kivy carousel.py c:/directory/images/
       - (for images not located in current directory directory)

    - issues:
    resize causes all images to be reloaded.
    '''
    k = MainApp(sys.argv)
    Example1().run()
