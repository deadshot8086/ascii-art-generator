import sys
from PIL import Image, ImageDraw, ImageFont
import cv2
import math
import numpy as np

# chars sorted based on luminosity
chars = " \":;Il!i+?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao#MW&8%B@$"
charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256
# for scaling frames down
scaleFactor = .5
# char width, height in px
oneCharWidth = 5
oneCharHeight = 8
fileName = sys.argv[1]
cap = cv2.VideoCapture(fileName)  # input videocapture
FPS = cap.get(cv2.CAP_PROP_FPS)  # FPS of input video
# print(FPS)
out = None
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # total frames for progress


# gets character based on luminosity of pixels
def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]


# text_file = open("Output.txt", "w")
fnt = ImageFont.truetype('lucon.ttf', 7)
print("working ...")
while cap.isOpened():
    ret, img = cap.read()  # reading frame by frame
    print(f' {round((100 * cap.get(cv2.CAP_PROP_POS_FRAMES)) / total_frames, 2):<6}%', end='\r')  # progress printing
    if ret:
        # height, width, _ = img.shape
        # img = cv2.resize(img, (int(320*scaleFactor), int(scaleFactor * height * (320 / width) * (oneCharWidth / oneCharHeight))), interpolation=cv2.INTER_NEAREST_EXACT, fx=0, fy=0)
        img = Image.fromarray(img)
        width, height = img.size
        # scaling image frame
        img = img.resize(
            (int(320 * scaleFactor), int(scaleFactor * height * (320 / width) * (oneCharWidth / oneCharHeight))),
            Image.NEAREST)
        width, height = img.size
        pix = img.load()
        # output video writer
        if out is None:
            out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), FPS,
                                  (oneCharWidth * width, oneCharHeight * height))
        # output image frame
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
                h = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # calculating luminosity
                # text_file.write(getChar(h))
                # replace pixel with text of similar color
                d.text((j * oneCharWidth, i * oneCharHeight), getChar(h), font=fnt, fill=(r, g, b))
        open_cv_image = np.array(outputImage)
        out.write(open_cv_image)  # write frame
    else:
        break

    # text_file.write('\n')
cap.release()
out.release()
cv2.destroyAllWindows()
print("done, check file output.avi")
