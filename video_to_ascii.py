import sys
from PIL import Image, ImageDraw, ImageFont
import cv2
import math
import numpy as np

chars = " \":;Il!i+?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao#MW&8%B@$"
charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256

scaleFactor = .5

oneCharWidth = 5
oneCharHeight = 8
fileName = sys.argv[1]
cap = cv2.VideoCapture(fileName)
FPS = cap.get(cv2.CAP_PROP_FPS)
# print(FPS)
out = None
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]


# text_file = open("Output.txt", "w")
fnt = ImageFont.truetype('lucon.ttf', 7)
print("working ...")
while cap.isOpened():
    ret, img = cap.read()
    print(f' {round((100*cap.get(cv2.CAP_PROP_POS_FRAMES))/total_frames, 2):<6}%', end='\r')
    if ret:
        # height, width, _ = img.shape
        # img = cv2.resize(img, (int(320*scaleFactor), int(scaleFactor * height * (320 / width) * (oneCharWidth / oneCharHeight))), interpolation=cv2.INTER_NEAREST_EXACT, fx=0, fy=0)
        img = Image.fromarray(img)
        width, height = img.size
        img = img.resize(
            (int(320 * scaleFactor), int(scaleFactor * height * (320 / width) * (oneCharWidth / oneCharHeight))), Image.NEAREST)
        width, height = img.size
        pix = img.load()
        if out is None:
            out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), FPS,
                                  (oneCharWidth * width, oneCharHeight * height))
        outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
        d = ImageDraw.Draw(outputImage)
        cf = 10

        for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]
                r = min(r + cf, 255)
                g = min(g + cf + 5, 255)
                b = min(b + cf + 5, 255)
                h = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
                # text_file.write(getChar(h))

                d.text((j * oneCharWidth, i * oneCharHeight), getChar(h), font=fnt, fill=(r, g, b))
        open_cv_image = np.array(outputImage)
        out.write(open_cv_image)
    else:
        break

    # text_file.write('\n')
cap.release()
out.release()
cv2.destroyAllWindows()
print("done, check file output.avi")
