import base64

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

def compose_photos_to_gif():
    pass

def check_photos_equivalence():
    pass

def detect_object(category="cat"):
    pass