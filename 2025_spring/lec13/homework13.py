import bs4, gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    soup = bs4.BeautifulSoup(text, 'html.parser')
    stories = []
    
    story_divs = soup.find_all('div', class_='story-text')

    for story_div in story_divs:
        title_tag = story_div.find('h3', class_='title')
        
        if title_tag:
            title = title_tag.get_text().strip()
        else:
            continue

        teaser_tag = story_div.find('p', class_='teaser')
        if teaser_tag:
            teaser = teaser_tag.get_text().strip()
        else:
            teaser = "" 

        stories.append((title, teaser))
        
    return stories
    
def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    title, teaser = stories[n]
    
    full_text = title + ". " + teaser
    
    tts_object = gtts.gTTS(text=full_text, lang='en')
    
    tts_object.save(filename)
