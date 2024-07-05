# Install google_trans library: pip install google_trans_new
from google_trans_new import google_translator

def translate_text(input_text, target_language):
    translator = google_translator()
    translated_text = translator.translate(input_text, lang_tgt=target_language)
    return translated_text

if __name__ == "__main__":
    input_text = "Hello, world!"
    target_language = "es"  # Spanish
    translated_result = translate_text(input_text, target_language)
    print(f"Translated text: {translated_result}")
