from random import shuffle
from xmastree.tree import RGBXmasTree
from colorzero import Color
from time import sleep

tree = RGBXmasTree(brightness=.1)

top_light_colors = [Color('yellow'), Color('blue')]
other_colors = [Color('red'), Color('green'), Color('white'), Color('blue'), Color('yellow')]

try:
    while 1:
        for index, light in enumerate(tree):
            if index == 3:
                shuffle(top_light_colors)
                light.color = top_light_colors[0]
            else:
                shuffle(other_colors)
                light.color = other_colors[0]
        sleep(.5)
except KeyboardInterrupt:
    tree.off()
