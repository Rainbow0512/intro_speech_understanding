import gtts

def synthesize(text, lang, filename):
    '''
    Use gtts.gTTs(text=text, lang=lang) to synthesize speech, then write it to filename.
    
    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    '''
    tts_object = gtts.gTTS(text=text, lang=lang)

    tts_object.save(filename)

