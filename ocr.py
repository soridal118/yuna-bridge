import pytesseract
from PIL import Image

# Tesseract 실행 경로 설정 (Windows 환경)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    """
    이미지에서 텍스트를 추출하는 함수
    """
    try:
        img = Image.open(image_path)  # 이미지 열기
        text = pytesseract.image_to_string(img, lang="kor+eng")  # 한글+영어 OCR 수행
        return text.strip()
    except Exception as e:
        return f"오류 발생: {e}"

if __name__ == "__main__":
    image_path = input("OCR을 수행할 이미지 파일 경로 입력: ")
    extracted_text = extract_text(image_path)
    print("\n추출된 텍스트:\n", extracted_text)
