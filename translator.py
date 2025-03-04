from googletrans import Translator

def translate_text(text, src_lang="ko", dest_lang="km"):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

if __name__ == "__main__":
    text = input("번역할 문장을 입력하세요: ")
    result = translate_text(text)
    print(f"번역 결과: {result}")
