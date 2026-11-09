import streamlit as st
from main import translate_text, text_to_audio
import os

st.title("Text-to-Speech Translator")

languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
}

text_input = st.text_area("Enter the text you want to convert:", height=150)

col1, col2 = st.columns(2)

with col1:
    input_lang_name = st.selectbox(
        "Select the language of your input text:",
        options=list(languages.keys()),
        index=0
    )

with col2:
    output_lang_name = st.selectbox(
        "Select the language for the audio output:",
        options=list(languages.keys()),
        index=0
    )

if st.button("Translate and Convert to Audio"):
    if not text_input:
        st.warning("Please enter some text to convert.")
    else:
        input_lang_code = languages[input_lang_name]
        output_lang_code = languages[output_lang_name]

        with st.spinner(f"Translating text from {input_lang_name} to {output_lang_name}..."):
            translated_text = translate_text(text_input, input_lang_code, output_lang_code)

        if translated_text:
            st.subheader("Translated Text:")
            st.write(translated_text)

            with st.spinner(f"Generating audio in {output_lang_name}..."):
                audio_file_path = text_to_audio(translated_text, output_lang_code)

            if audio_file_path and os.path.exists(audio_file_path):
                st.subheader("Generated Audio:")
                try:
                    with open(audio_file_path, "rb") as audio_file:
                        audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/mp3')
                    st.success(f"Audio generated successfully!")
                except Exception as e:
                    st.error(f"Error displaying audio: {e}")
                    if os.path.exists(audio_file_path):
                         st.info(f"Audio saved as {audio_file_path}, but could not be played in the browser.")

            else:
                st.error("Failed to generate audio file.")
        else:
            st.error("Translation failed. Please check your input and language selection.")
