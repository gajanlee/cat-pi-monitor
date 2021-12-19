import time
from io import BytesIO
import importlib

import cv2
import numpy as np

class CameraHandler:

    def get_image_bytes(self):
        raise NotImplementedError
    
    def get_image_byte_stream(self):
        raise NotImplementedError


class SimpleCameraHandler(CameraHandler):

    def __init__(self):
        pass

    def get_image_bytes(self):
        return self.generate_time_image().tobytes()

    def get_image_byte_stream(self):
        while True:
            print("generating cv2 image, ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            yield (512, 512, self.get_image_bytes())
            time.sleep(1)

    def generate_time_image(self):
        img = np.zeros((512,512,3), np.uint8)

        # Write some Text

        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (0, 250)
        fontScale              = 1
        fontColor              = (255,255,255)
        thickness              = 1
        lineType               = 2

        import datetime

        cv2.putText(img, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            thickness,
            lineType)
        
        return img


class PiCameraHandler(CameraHandler):

    def __init__(self):
        self.width, self.height = 256, 256
        from picamera import PiCamera
        camera = PiCamera()
        camera.resolution = (self.width, self.height)
        camera.start_preview()

        self.camera = camera
    
    def get_image_bytes(self):
        image_stream = BytesIO()
        self.camera.capture(image_stream, 'rgb')
        return image_stream.getvalue()

    def get_image_byte_stream(self):
        image_stream = BytesIO()
        for _ in self.camera.capture_continuous(image_stream, "rgb"):
            print("capturing pi photo, ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            image_stream.seek(0)
            yield self.width, self.height, image_stream.read()

            image_stream.seek(0)
            image_stream.truncate()