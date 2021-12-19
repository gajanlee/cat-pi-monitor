import base64
import numpy as np
import cv2
import time

def get_image_bytes(image_path):
    with open(image_path, "rb") as f:
        return f.read()

def get_image_base64_from_bytes(image_bytes):
    return base64.b64encode(image_bytes)

def get_image_base64_from_path(image_path):
    image_bytes = get_image_bytes(image_path)
    return get_image_base64_from_bytes(image_bytes)

def decode_base64_to_bytes(base64_code):
    return base64.b64decode(base64_code)

def write_bytes_to_path(image_bytes, image_path):
    with open(image_path, "wb") as file:
        file.write(image_bytes)

def write_base64_to_path(base64_code, image_path):
    image_bytes = decode_base64_to_bytes(base64_code)
    write_bytes_to_path(image_bytes, image_path)


def image_byte_to_cv2_image(width, height, byte):
    # image_array = np.fromstring(decode_base64_to_bytes(byte), np.uint8)
    image_array = np.frombuffer(byte, np.uint8)
    image_array = image_array.reshape(width, height, -1)
    # _, image = cv2.imencode(".jpg", image_array)
    cv2.putText(image_array, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , 
        (0, 20), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.5,
        (255, 255, 255),
        1,
        2
    )
    return image_array


def add_timestamp_to_image(image):
    cv2.putText(image, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , 
        (0, 0), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1,
        (255, 255, 255),
        1,
        2
    )

def compose_photos_to_gif():
    pass

def check_photos_equivalence():
    pass

def detect_object(category="cat"):
    pass