import requests
import webbrowser

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = \
        {
            "rel_rhy": word,
            "max": "3"
        }
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    # return resp.json()  # Return a python object (a list of dictionaries in this case)


parag = '''The answers to questions two and three, about the contents of the 
value of the params dictionary, can be found in the section of the 
documentation that describes the particular endpoint. For example, take a 
look at the documentation for the “words” endpoint. The entire request will 
return some words, and all of the params contents will specify constraints 
that restrict the search. '''

webbrowser.open('www.google.com')