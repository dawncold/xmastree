from random import shuffle, random
from xmastree.tree import RGBXmasTree
from colorzero import Color
from time import sleep

tree = RGBXmasTree(brightness=.1)

top_light_colors = [Color('yellow'), Color('blue')]

try:
    while 1:
        for index, light in enumerate(tree):
            if index == 3:
                shuffle(top_light_colors)
                light.color = top_light_colors[0]
            else:
                light.color = (random(), random(), random())
        for light in tree:
            light.off()
            light.on()
            light.off()
            light.on()
            light.off()
            light.on()
except KeyboardInterrupt:
    tree.off()
