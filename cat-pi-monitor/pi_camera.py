import picamera
from time import sleep
 
#create object for PiCamera class
camera = picamera.PiCamera()
#set resolution
camera.resolution = (1024, 768)
camera.brightness = 60
camera.start_preview()

for i, filename in zip(range(60), camera.capture_continuous("image{timestamp:%H-%M-%S-%h-%m}")):
    print(filename)
    time.sleep(1)

camera.stop_preview()
