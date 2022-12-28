import numpy as np
from PIL import Image

def draw_canvas(img_width, img_height, color, shapes):
    img_data = np.zeros((img_width, img_height, 3), dtype=np.uint8)
    if color.lower() == 'w':
        img_data[:] = [255, 255, 255]
    for shape in shapes:
        img_data[shape.x:(shape.x + shape.width), shape.y:(shape.y + shape.height)] = shape.color
    img = Image.fromarray(img_data, 'RGB')
    img.save("canvas.png")