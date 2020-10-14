import os

ALLOWED_EXTENSIONS = ["JPEG", "JPG", "PNG"]
SECRET_KEY = os.environ.get("SECRET_KEY") or "galeriasm"
