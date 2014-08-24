import sys
import os
import kivy
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory


class MainApp(object):

    def __init__(self, argv):
        self.args = argv
        self.parametrics()

    def parametrics(self):
        alternate_directory = (len(self.args) == 2)

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
        carousel = Carousel(direction='right')
        for src in k.filenames:
            image = Factory.AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel


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
