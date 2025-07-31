import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    now = datetime.datetime.now()

    time_str = "The time is " + now.strftime("%I:%M %p")
    
    tts = gtts.gTTS(text=time_str, lang=lang)
    
    tts.save(filename)
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    jokes = [
        "I broke my arm in two places.   My doctor told me to stop going to those places."
        "I was going to tell you a fighting joke...  but I forgot the punch line."
        "Did you hear about the famous Italian chef that recently died?   He pasta way."
        "I could never be a plumber  it’s too hard watching your life’s work go down the drain."
        "What is the only concert in the world that costs 45 cents?   50 Cent, featuring Nickelback."
        "Want to hear a construction joke?   Sorry, I’m still working on it."
        "Where did Captain Hook get his hook?   From the second-hand store."
        "Why did Shakespeare’s wife leave him?   She got sick of all the drama."
        "Want to hear a joke about going to the bathroom?   Urine for a treat."
        "I'm reading a book about anti-gravity.   It's impossible to put down!"
        "What’s Forrest Gump’s password?   1forrest1"
    ]
    joke = random.choice(jokes)
    
    tts = gtts.gTTS(text=joke, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    now = datetime.datetime.now()

    date_str = "Today is " + now.strftime("%A, %B %d, %Y")
    
    tts = gtts.gTTS(text=date_str, lang=lang)
    tts.save(audiofile)
    

    url = "https://calendar.google.com/"
    
    return url

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    r = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=lang)
        print("You said: " + text)
        
        if "time" in text:
            what_time_is_it(lang, filename)
        elif "joke" in text:
            tell_me_a_joke(lang, filename)
        elif "day" in text:
            what_day_is_it(lang, filename)
        else:
            unrecognized_text = "Sorry, I didn't understand that."
            tts = gtts.gTTS(text=unrecognized_text, lang=lang)
            tts.save(filename)
            
    except speech_recognition.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        
    except speech_recognition.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
