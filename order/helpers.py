import hashlib
import time
from base64 import encode


def generate_tracking_number():
    return (hashlib.md5((str(time.time()) + "!salt!").encode()).hexdigest()[:8]).upper()

