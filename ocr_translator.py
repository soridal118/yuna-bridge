import pytesseract
from PIL import Image
from translator import translate_text  # 번역기 함수 불러오기

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
    image_path = input("OCR을 수행할 이미지 파일 경로 입력 (예: C:\\YUNA\\sample_text.png): ")
    
    extracted_text = extract_text(image_path)
    print("\n🔍 OCR 추출된 텍스트:\n", extracted_text)

    if extracted_text:
        translated_text = translate_text(extracted_text, src_lang="ko", dest_lang="km")
        print("\n🌍 번역 결과 (한 → 크메르어):\n", translated_text)
    else:
        print("❌ OCR에서 텍스트를 추출하지 못했습니다.")
