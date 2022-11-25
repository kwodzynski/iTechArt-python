import os
from PIL import Image as im
from PIL import ImageFont as imf
from PIL import ImageDraw as id
from TextParsing import *

# Image variable
path_to_image = f'{os.getcwd()}/Resources/earth.jpg'
path_to_txt = f'{os.getcwd()}/Resources/text_to_parsing.txt'
left = 50
top = 50
right = 1900
bottom = 950


class ImageProcessing(TextParsing):
    def __init__(self, image_path, txt_path, left, top, right, bottom):
        self.image_path = image_path
        self.txt_path = txt_path
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    # Method for processing and showing the final image

    def process_image(self):
        image = im.open(self.image_path)
        croppping_image = image.crop(
            (self.left, self.top, self.right, self.bottom))
        draw = id.Draw(croppping_image)
        draw.text((0, 0), '\n'.join(
            map(str, TextParsing.read_text_file(self.txt_path))), (255, 255, 255))
        croppping_image.show()


img = ImageProcessing(path_to_image, path_to_txt, left, top, right, bottom)
img.process_image()
