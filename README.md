
# ASCII Art Generator

- convert image to ascii image
- convert video to ascii video(MJPG codec)

# Internal Working
Video is processed frame-by-frame, each frame is processed as an image using PIL, first it is resized to fit in time and quality, then each pixel is replaced with ascii character of same color, choice of ASCII character is based on Luminosity of pixel which is calculated by given formula. Finally video is written to output.avi in MJPG compression
```
Luminosity = 0.2126 * R + 0.7152 * G + 0.0722 * B
```

# REQUIREMENTS
- using pipenv
```bash
pipenv install
```

# Demo Video
https://user-images.githubusercontent.com/76732801/174393765-4ef4a2c7-16d8-4df9-8bca-2b5102daa8b7.mp4


# Usage/Examples
### Image to ASCII (TYPE-0)
```bash
python3 image_to_ascii.py car.png 0
```
Original             |  ASCII
:-------------------------:|:-------------------------:
![](https://github.com/adityabadhiye/ascii-art-generator/blob/master/images/car.png)  |  ![](https://github.com/adityabadhiye/ascii-art-generator/blob/master/images/car-output.png)

### Image to ASCII (TYPE-1)
```bash
python3 image_to_ascii.py img.jpg 1
```
Original             |  ASCII
:-------------------------:|:-------------------------:
![](https://github.com/adityabadhiye/ascii-art-generator/blob/master/images/img.jpg)  |  ![](https://github.com/adityabadhiye/ascii-art-generator/blob/master/images/img-output.png)

### Video to ASCII
```bash
python3 video_to_ascii.py video.mp4
```
Original             |  ASCII
:-------------------------:|:-------------------------:
![](https://github.com/adityabadhiye/ascii-art-generator/blob/master/images/video.gif)  |  ![](https://github.com/adityabadhiye/ascii-art-generator/blob/master/images/output_video.gif)

# Learnings
- Learned storage of image as matrix of pixels
- Learned to use PIL, OpenCV for image processing
- Learned to process video frame-by-frame as an image with PIL, OpenCV

# Reference
- https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
- https://dev.to/anuragrana/generating-ascii-art-from-colored-image-using-python-4ace
