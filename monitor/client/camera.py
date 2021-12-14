import time
import sys
from io import BytesIO

class CameraHandler:

    def get_image_bytes(self):
        raise NotImplementedError
    
    def get_image_byte_stream(self):
        raise NotImplementedError

class PiCameraHandler(CameraHandler):

    def __init__(self):
        from picamera import PiCamera
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()

        self.camera = camera
    
    def get_image_bytes(self):
        image_stream = BytesIO()
        self.camera.capture(image_stream, 'jpeg')
        return image_stream.getvalue()

    def get_image_byte_stream(self):
        image_stream = BytesIO()
        for _ in self.camera.capture_continuous(image_stream, "jpeg"):
            
            image_stream.seek(0)
            yield image_stream.read()

            image_stream.seek(0)
            image_stream.truncate()


# camera_handler = None
# def get_camera_handler():
#     if not camera_handler:
#         return CameraHandler()
#     return camera_handler