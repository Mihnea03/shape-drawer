from image import draw_canvas

img_width = int(input("Enter width of canvas: "))
img_height = int(input("Enter height of canvas: "))

color = input("Do you want the color to be black(b) or white(w)? ")
while color.lower() not in ['b','w']:
    color = input("Invalid color! Try 'b' or 'w': ")

shapes = []

class Shape:
    def __init__(self, x, y, width, height, r, g, b):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = [r,g,b]

while True:
    shape = input("Want to draw a square('s') or a rectangle('r')? Type 'quit' to finish: ")
    if shape.lower() == "quit":
        draw_canvas(img_width, img_height, color, shapes)
        break
    x = int(input("Enter x: "))
    y = int(input("Enter y: ")) 
    if shape.lower() == 's':
        width = int(input("Enter square width: "))
        height = width
    else:
        width = int(input("Enter rectangle width: "))
        height = int(input("Enter rectangle height: "))
    r = input("Enter red level (0-255): ")
    g = input("Enter green level (0-255): ")
    b = input("Enter blue level (0-255): ")
    shapes.append(Shape(x, y, width, height, r, g, b))
    
    
        
