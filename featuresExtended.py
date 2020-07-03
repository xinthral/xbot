import requests, sys

from bs4 import BeautifulSoup
from os import getcwd
from random import randint, seed
from utils import cnf
from time import time

from db.jokes_db import jokesDict
from db.phrases_db import phraseDict

""" Prologue """
seed(int(time()))

""" Globals """
dadJokeList = jokesDict['dad'].copy()
tabooJokeList = jokesDict['taboo'].copy()
gamingJokeList = jokesDict['gaming'].copy()
positivQuoteList = phraseDict['positivity'].copy()
inspirQuoteList = phraseDict['inspirational'].copy()
streamQuoteList = phraseDict['stream'].copy()
funnyQuoteList = phraseDict['funny'].copy()
showerQuoteList = phraseDict['shower'].copy()
nerdQuoteList = phraseDict['nerd'].copy()

def haikuMe():
    wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]
    wordList2 = ["visions", "distance", "conscience", "process", "chaos"]
    wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
    wordList4 = ["true", "dark", "cold", "warm", "great"]
    wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
    wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
    wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]

    wordIndex1=randint(0, len(wordList1)-1)
    wordIndex2=randint(0, len(wordList2)-1)
    wordIndex3=randint(0, len(wordList3)-1)
    wordIndex4=randint(0, len(wordList4)-1)
    wordIndex5=randint(0, len(wordList5)-1)
    wordIndex6=randint(0, len(wordList6)-1)
    wordIndex7=randint(0, len(wordList7)-1)

    haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n"
    haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
    haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."
    response = haiku.split('\n')
    return(response)

audioFiles = {"naviListen": getcwd() + "\\sound_effects\\Navi_Listen.mp3",
              "smokeWeed": getcwd() + "\\sound_effects\\SmokeWeedEveryday.mp3"
}

def jokes(jokeType = 'dad', index = -1):
    try:
        index = int(index)
        global jokesDict

        if jokeType.lower() == "dad":
            global dadJokeList
            if len(dadJokeList) < 1:
                dadJokeList = jokesDict['dad'][:]
            if index > -1:
                jokeIndex = index
            else:
                jokeIndex = randint(0, len(dadJokeList)-1)
            response = dadJokeList.pop(jokeIndex)

        elif jokeType.lower() == "taboo":
            global tabooJokeList
            if len(tabooJokeList) < 1:
                tabooJokeList = jokesDict['taboo'][:]
            if index > -1:
                jokeIndex = index
            else:
                jokeIndex = randint(0, len(tabooJokeList)-1)
            response = tabooJokeList.pop(jokeIndex)

        elif jokeType.lower() == "gaming":
            global gamingJokeList
            if len(gamingJokeList) < 1:
                gamingJokeList = jokesDict['gaming'][:]
            if index > -1:
                jokeIndex = index
            else:
                jokeIndex = randint(0, len(gamingJokeList)-1)
            response = gamingJokeList.pop(jokeIndex)
        else:
            error = "Invalid Joke Type."
            response = dadJokeList.pop(randint(0, len(dadJokeList)-1))
            response.insert(0, error)
    except:
        print(sys.exc_info())
        error = "Invalid Syntax. So here's a dad joke."
        response = jokesDict['dad'][randint(0, len(jokesDict['dad'])-1)]
        response.insert(0, error)
    return(response)

def memePyramid(meme = 'PogChamp'):
    #FIXME: Function needs work, doesn't work as intended.
    response = []
    size = len(meme)
    for i in range(1, 4):
        response.append((" " + meme + " ") * i)
    print(response)
    return(response)

def playSound(meme):
    import subprocess
    subprocess.call([cnf("CLIENT", "VLC_PATH"), audioFiles[meme], '--play-and-exit'])
    print("{} audio file was played.".format(meme))

def quotes(phraseType = "positivity", index = -1):
    try:
        if phraseType.lower() == "positivity":
            global positivQuoteList
            if len(positivQuoteList) < 1:
                positivQuoteList = phraseDict['positivity'][:]
            if index > -1:
                quoteIndex = index
            else:
                quoteIndex = randint(0, len(positivQuoteList)-1)
            response = positivQuoteList.pop(quoteIndex)

        elif phraseType.lower() == "inspirational":
            global inspirQuoteList
            if len(inspirQuoteList) < 1:
                inspirQuoteList = phraseDict['inspirational'][:]
            if index > -1:
                quoteIndex = index
            else:
                quoteIndex = randint(0, len(inspirQuoteList)-1)
            response = inspirQuoteList.pop(quoteIndex)

        elif phraseType.lower() == "shower":
            global showerQuoteList
            if len(showerQuoteList) < 1:
                showerQuoteList = phraseDict['shower'][:]
            if index > -1:
                quoteIndex = index
            else:
                quoteIndex = randint(0, len(showerQuoteList)-1)
            response = showerQuoteList.pop(quoteIndex)

        elif phraseType.lower() == "stream":
            global streamQuoteList
            if len(streamQuoteList) < 1:
                streamQuoteList = phraseDict['stream'][:]
            if index > -1:
                quoteIndex = index
            else:
                quoteIndex = randint(0, len(streamQuoteList)-1)
            response = streamQuoteList.pop(quoteIndex)

        elif phraseType.lower() == "nerd":
            global nerdQuoteList
            if len(nerdQuoteList) < 1:
                nerdQuoteList = phraseDict['nerd'][:]
            if index > -1:
                quoteIndex = index
            else:
                quoteIndex = randint(0, len(nerdQuoteList)-1)
            response = nerdQuoteList.pop(quoteIndex)

        else:
            error = "Invalid Quote Type."
            response = quotes()
            response.insert(0, error)
    except:
        response = quotes()
    return(response)

def randomFacts():
    url = "http://randomfactgenerator.net/"
    r = requests.get(url)
    bs = BeautifulSoup(r.content, 'html.parser')
    fact = bs.find(id="z").text.replace('\nTweet', '')
    if '\n' in fact:
        fact = fact.replace('\n', ' ')
    return(str(fact))
