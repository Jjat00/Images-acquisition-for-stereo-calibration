# **Images Acquisition for Extrinsic Calibration**

This is a simple desktop application for automatic acquisition to later perform a stereo calibration between two cameras using Python. In this case, rgb and depth images are acquired, however this application can be used for any pair of cameras as long as the appropriate calibration pattern is available.
The pair of images for which the pattern is detected are automatically saved in the path chosen by the user.


## Dependencies

* Ubuntu +18.04
* [libfreenect](https://github.com/OpenKinect/libfreenect)
* Python +3.7

This project needs **[libfreenect](https://github.com/OpenKinect/libfreenect)** on your computer to enter the microsoft kinect camera. If you are using a different camera you need to modify the file **src/acquisition/DataAcquisition.py** and ready, you can use this application.

## Project Setup
```
    pip install -r requirements.txt
```
## Run Project
```
    python src/app.py
```

