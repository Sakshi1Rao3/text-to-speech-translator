
from gtts import gTTS
from deep_translator import MyMemoryTranslator

# MyMemory language names
LANGUAGES = {
    "en": "english",
    "fr": "french",
    "es": "spanish"
}


def translate_text(input_text, input_lang, output_lang):
    try:
        if input_lang == output_lang:
            return input_text

        translated = MyMemoryTranslator(
            source=LANGUAGES[input_lang],
            target=LANGUAGES[output_lang]
        ).translate(input_text)

        return translated

    except Exception as e:
        print(f"Translation error: {e}")
        raise


def text_to_audio(text, output_lang):
    try:
        audio_file = "output.mp3"

        tts = gTTS(
            text=text,
            lang=output_lang,
            slow=False
        )

        tts.save(audio_file)
        return audio_file

    except Exception as e:
        print(f"Audio generation error: {e}")
        raise
