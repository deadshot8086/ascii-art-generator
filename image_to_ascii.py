import sys
from PIL import Image, ImageDraw, ImageFont
import math

# chars = "#Wo- "[::-1]
if int(sys.argv[2]) == 0:  # Type-0
    chars = " \":;Il!i+?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao#MW&8%B@$"
else:  # Type-1
    chars = " ░▒▓█"
charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256

scaleFactor = 1

oneCharWidth = 5
oneCharHeight = 8
fileName = sys.argv[1]


# gets character based on luminosity of pixels
def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]


# text_file = open("Output.txt", "w")
# input image
im = Image.open(fileName)
# importing font
fnt = ImageFont.truetype('lucon.ttf', 7)

width, height = im.size
# resize image
im = im.resize((320, int(scaleFactor * height * (320 / width) * (oneCharWidth / oneCharHeight))),
               Image.Resampling.NEAREST)

width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)
cf = 10
# iterating over each pixel
for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        r = min(r + cf, 255)
        g = min(g + cf + 5, 255)
        b = min(b + cf + 5, 255)
        h = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        # replace pixel with text of similar color
        d.text((j * oneCharWidth, i * oneCharHeight), getChar(h), font=fnt, fill=(r, g, b))

    # text_file.write('\n')
# save image
outputImage.save('output.png')
