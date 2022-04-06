# Bolshevik I, A Pixelplace Bot
# Created by SovietStalin on April 5th, 2022

import sys
import time
from turtle import color

from pynput import keyboard
from pynput.mouse import Button, Controller
from PIL import Image


class ConfigFile:
    def __init__(self, path):
        with open(path, "rt") as f:
            self.raw_contents = f.read()
        self.parse_raw_contents()

    def parse_raw_contents(self):
        contents_dict = {}
        self.raw_contents = self.raw_contents.split('\n')
        for i, e in enumerate(self.raw_contents):
            self.raw_contents[i] = e.split('=')
            contents_dict[self.raw_contents[i][0].strip()] = self.raw_contents[i][1].strip()
        
    def text_to_color(self, text):
        color_names = {
            "WHITE" : 0xffffff,
            "LIGHT_GREY" : 0xc4c4c4,
            "MEDIUM_LIGHT_GREY" : 0x888888,
            "MEDIUM_DARK_GREY" : 0x555555,
            "DARK_GREY" : 0x222222,
            "BLACK" : 0x000000,
            "DARK_GREEN" : 0x006600,
            "LIGHT_GREEN" : 0x22b14c,
            "GREEN" : 0x02be01,
            "PREM_GREEN" : 0x51e119,
            "YELLOW_GREEN" : 0x94e044,
            "LIGHT_YELLOW" : 0xfbff5b,
            "YELLOW" : 0xe5d900,
            "DARK_YELLOW" : 0xe6be0c,
            "ORANGE" : 0xe59500,
            "LIGHT_BROWN" : 0xa06a42,
            "BROWN" : 0x99530d,
            "DARK_BROWN" : 0x633c1f,
            "DARK_RED" : 0x6b0000,
            "MEDIUM_DARK_RED" : 0x9f0000,
            "RED" : 0xe50000,
            "PREM_ORANGE" : 0xff3904,
            "LIGHT_ORANGE" : 0xbb4f00,
            "SALMON" : 0xff755f,
            "MEDIUM_LIGHT_SALMON" : 0xffc49f,
            "LIGHT_SALMON" : 0xffdfcc,
            "PINK" : 0xffa7d1,
            "DARK_PINK" : 0xcf6ee4,
            "MAGENTA" : 0xec08ec,
            "DARK_MAGENTA" : 0x820080,
            "PREM_PURPLE" : 0x5100ff,
            "DARK_BLUE" : 0x020763,
            "MEDIUM_DARK_BLUE" : 0x0000ea,
            "BLUE" : 0x044bff,
            "MEDIUM_LIGHT_BLUE" : 0x0083c7,
            "LIGHT_BLUE" : 0x6483cf,
            "PREM_CYAN" : 0x45ffc8,
            "MEDIUM_DARK_CYAN" : 0x00d3dd,
            "DARK_CYAN" : 0x36baff
        }

        if text in color_names:
            return color_names[text] # convert the color name to its hex value
        else:
            if(type(text) == int): # text is already a hex value
                return text
            else:
                print("Something is wrong with the background color (Check your config file)! Exiting program")
                sys.exit()
            

def main():
    browser_zoom = 1            # zoom in browser
    screen_width = 1920         # width of the display
    pp_zoom = 1                 # zoom in PixelPlace (should always be a positive integer)
    exclude_background = False  # whether the background color should be painted or not
    background_color = 0xffffff # the color to exclude from painting if exclude_background is true
    is_premium = False          # whether the user is a premium user (for extra colors)
    painting_speed = 10         # painting speed in px/s
    image_name = "test.png"     # name and path to the image to be printed

    config = ConfigFile("../config.txt")

    pass

if __name__ == "__main__":
    main()