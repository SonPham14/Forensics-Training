from PIL import Image

image = Image.open('image.png').convert('RGB')

width, height = image.size

with open('D:\\Training_Forensics\\RGB.txt', 'w') as f:
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            f.write(f'{r} {g} {b}\n')

