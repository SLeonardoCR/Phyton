from googletrans import Translator

def translate(txt):
    translator = Translator()
    translation = translator.translate(text=txt, dest='es')
    return translation.text