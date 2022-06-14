
# ASCII Art Generator

- convert image to ascii image
- convert video to ascii video(MJPG codec)

# REQUIREMENTS
- using pipenv
```bash
pipenv install
```

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
