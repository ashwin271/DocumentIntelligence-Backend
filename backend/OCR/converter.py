import pytesseract
from .pre_process import process


# converting image to text
def convert(image):
    ocr_result = pytesseract.image_to_string(image)
    return ocr_result

