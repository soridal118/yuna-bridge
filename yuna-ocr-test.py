from google.cloud import vision
import io

def detect_text(image_path):
    """Google Cloud Vision OCR을 사용하여 이미지 속 텍스트를 추출"""
    client = vision.ImageAnnotatorClient()

    # 이미지 파일을 읽어오기
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)

    # OCR 실행
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # 결과 출력
    if texts:
        print("✅ OCR 결과:")
        print(texts[0].description)  # 전체 감지된 텍스트 출력
    else:
        print("❌ 텍스트를 감지하지 못했어요.")

    # 에러 처리
    if response.error.message:
        print(f"⚠️ 오류 발생: {response.error.message}")

# 테스트할 이미지 경로 설정 (바탕화면에 샘플 이미지 저장 후 사용)
image_path = "/Users/guyuli/Desktop/yuna-ocr/yunaocr.png"



# OCR 실행
detect_text(image_path)

