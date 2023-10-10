from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust the path if it's different on your machine

# ... rest of your code, including the solve_captcha function

def solve_captcha(image_path):
    # Open the image
    image = Image.open(image_path)
    
    #image = image.resize((width * 0.5, height * 0.5), Image.BICUBIC)
    # Convert the image to grayscale
    #image = image.convert('L')

    image = image.filter(ImageFilter.MedianFilter(size=3))


    threshold = 150
    image = image.point(lambda p: p > threshold and 255)

    
    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    # Apply a filter to reduce noise
    image = image.filter(ImageFilter.MedianFilter(5))

    # Use tesseract to do OCR on the processed image
    text = pytesseract.image_to_string(image, config='--psm 6')

    return text

