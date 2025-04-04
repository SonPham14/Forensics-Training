from PIL import Image

width = 631
height = 437

image = Image.new('RGB', (width, height))

with open('D:\\Training_Forensics\\RGB.txt', 'r') as f:
    for y in range(height):
        for x in range(width):
            r, g, b = map(int, f.readline().split())
            image.putpixel((x, y), (r, g, b))


image.save('D:\\Training_Forensics\\image.png')
