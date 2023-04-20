import argparse
import pytesseract
import cv2
from PIL import Image

# 设置Tesseract可执行文件路径（用实际路径替换<path_to_tesseract>）
# pytesseract.pytesseract.tesseract_cmd = '<path_to_tesseract>'

def preprocess_image(image_path, debug=False):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    denoised_image = cv2.medianBlur(binary_image, 3)

    if debug:
        cv2.imwrite("gray_image.png", gray_image)
        cv2.imwrite("binary_image.png", binary_image)
        cv2.imwrite("denoised_image.png", denoised_image)

    return Image.fromarray(denoised_image)

def ocr_image(image, language):
    text = pytesseract.image_to_string(image, lang=language)
    return text

def main():
    parser = argparse.ArgumentParser(description="OCR an image")
    parser.add_argument("image_path", help="Path to the image")
    parser.add_argument("--language", default="eng", help="Language for OCR (default: eng)")
    parser.add_argument("--debug", action="store_true", help="Save preprocessed images for debugging (default: False)")
    args = parser.parse_args()

    preprocessed_image = preprocess_image(args.image_path, args.debug)
    extracted_text = ocr_image(preprocessed_image, args.language)

    print("Extracted text:")
    print(extracted_text)

if __name__ == "__main__":
    main()
