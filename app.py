import streamlit as st
from googletrans import Translator, LANGUAGES

# Translator instance
translator = Translator()

# Streamlit App
def main():
    st.title('Language Translator')

    # Input text box for user input
    text = st.text_area('Enter text to translate')

    # Selectbox for choosing source language
    source_lang = st.selectbox('Select source language', ['auto'] + list(LANGUAGES.keys()))

    # Selectbox for choosing target language
    target_lang = st.selectbox('Select target language', list(LANGUAGES.keys()))

    if st.button('Translate'):
        if text.strip() != '':
            try:
                # Translate text
                translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
                st.success(f"Translated Text ({target_lang}):")
                st.write(translated_text)
            except Exception as e:
                st.error(f"Translation error: {e}")
        else:
            st.warning("Please enter some text to translate.")

# Footer
st.markdown("---")
st.markdown("By [Rauf](https://personal-web-page-lemon.vercel.app/index.html)")

if __name__ == '__main__':
    main()
