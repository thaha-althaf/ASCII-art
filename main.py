from PIL import Image

image = Image.open("ascii-pineapple.jpg")

image_rgb = image.convert("RGB")

width, height = image_rgb.size

pixels = [[image_rgb.getpixel((col, row)) for col in range(width)] for row in range(height)]

gradient = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


ascii_matrix = []

for row in pixels:
    ascii_row = []
    for pixel in row:
        red, green, blue = pixel


        brightness = (red + green + blue) /3


        index = int(brightness * (len(gradient) - 1) / 255)
        ascii_char = gradient[index]
        ascii_row.append(ascii_char*2)

    ascii_matrix.append(ascii_row)


for row in ascii_matrix:
    print(''.join(row))

