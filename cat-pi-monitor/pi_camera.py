import picamera
import time
import sys
from io import BytesIO
from picamera import PiCamera

class CameraHandler:
    
    def __init__(self):
        self.__init_camera()
    
    def __init_camera(self):
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()

        self._camera = camera

    def get_image_bytes(self):
        image_stream = BytesIO()
        self._camera.capture(image_stream, 'jpeg')
        return image_stream.getvalue()
    
    def get_image_bytes_stream(self):
        image_stream = BytesIO()
        for _ in self._camera.capture_continuous(image_stream, "jpeg"):
            
            image_stream.seek(0)
            yield image_stream.read()

            image_stream.seek(0)
            image_stream.truncate()

camera_handler = None
def get_camera_handler():
    if not camera_handler:
        return CameraHandler()
    return camera_handler