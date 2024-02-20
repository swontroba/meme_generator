"""
class accepts an image output path, selects a random image and quote,
saves the image to the output path and returns the path to the image.
"""

import random

from PIL import Image, ImageDraw, ImageFont

from matplotlib import font_manager


class MemeEngine:
    """
    This class takes in an image output path, selects a random image and quote, saves the image to the output path
    and returns the path to the image.
    """
    def __init__(self, output_path):
        """Create instance of class."""
        self.output_path = output_path

    @staticmethod
    def get_rand_y(value):
        """Return a random y-axis."""
        y_min = 10
        y_max = value - 100
        return random.randint(y_min, y_max)

    def make_meme(self, path, text, author, width=500) -> str:
        """Create meme with provided text and author."""
        try:
            img = Image.open(path)
        except Exception as ex:
            print(f"Exception: {ex}")
        else:
            if width is not None:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if text and author:
                message = f"{text}\n- {author}"
                draw = ImageDraw.Draw(img)
                # simple
                # font = ImageFont.load_default()
                # nicer but needs matplotlib an additional lib
                font = font_manager.FontProperties(family='sans-serif', weight='bold')
                file = font_manager.findfont(font)
                print(file)
                font = ImageFont.truetype(file, 20)
                axis = (10, self.get_rand_y(img.size[1]))
                left, top, right, bottom = draw.textbbox(axis, message, font=font)
                draw.rectangle((left-5, top-5, right+5, bottom+5), outline='red')
                draw.text(axis, message, font=font, fill="white")

            out_path = f"{self.output_path}/{random.randint(0, 1000000)}.jpeg"

            img.save(out_path)
            print(f"Meme saved to {self.output_path}")
            return out_path
