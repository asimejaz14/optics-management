import hashlib
import time


def generate_tracking_number():
    return hashlib.md5(str(time.time()) + "!salt!").hexdigest()[:16]
