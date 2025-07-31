import speech_recognition

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    r = speech_recognition.Recognizer()

    with speech_recognition.AudioFile(filename) as source:

        audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data, language=language)
        return text

    except speech_recognition.UnknownValueError:

        return "Google Web Speech API could not understand the audio"
        
    except speech_recognition.RequestError as e:

        return f"Could not request results from Google Web Speech API; {e}"
