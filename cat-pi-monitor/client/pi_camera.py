import picamera
import time

class CameraConfig:
    
    def __init__(self, resolution, brightness):
        self.resolution = (1024, 768)
        self.brightness = 60

camera_config = CameraConfig(resolution)

def continuous_shooting(interval):
    camera = picamera.PiCamera()
    camera.resolution = (1024, 768)
    camera.brightness = 60

    camera.start_preview()
    
    for filename in zip(range(60), camera.capture_continuous("image{timestamp:%H-%M-%S-%h-%m}")):
        time.sleep(interval)

    camera.stop_preview()