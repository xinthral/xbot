import requests, sys

from bs4 import BeautifulSoup
from os import getcwd
from random import randint
from utils import cnf

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

"""
This whole jokes things needs to get unfucked, put the dictionary in a seperate file
"""
jokesDict = {
    'dad': [
        ["Why can\'t a bicycle stand on its own?", "It\'s two-tired."],
        ["What\'s the best thing about living in Switzerland,", "I don\'t know, but I hear their flag is a big plus."],
        ["What\'s more amazing than a talking dog?", "A spelling bee."],
        ["Why don\'t you see many poker players on the Savanna?", "There\'s too many cheetahs."],
        ["What did the grape say when it was stepped on?", "Nothing, it just let out a little wine."],
        ["I was up all night wondering where the sun went,", "but then it dawned on me."],
        ["I was thinking about Orion's Belt earlier,", "seems like a giant waist of space, if you ask me."],
        ["You know where General\'s keep their armies?", "In their sleevies."],
        ["Humans never like my dolphin puns,", "So I make them bad on porpoise."],
        ["I was disappointed the first time I tried to grow a beard,", "but then it grew on me."],
        ["Do you know how a backwards poet writes?", "In-verse."],
        ["I think of plateau's as compliments,", "afterall, they are the highest form of flattery."],
        ["To the guy who invented zero..", "Thanks for nothing!"],
        ["After watching a documentary on beavers, I realized something...","It was the best dam show I ever saw!"],
        ["A recent Hollywood hacker releaved Forrest Gump\'s password:", "1forrest1"],
        ["I was once programmed to make calendars, but then I got fired...", "All cause I took a couple days off."],
        ["Ever wonder how they make Holy Water?", "They boil the hell out of it."],
        ["I had a dream one time that I was a muffler...", "I woke up exhausted."],
        ["Do you know who you really can\'t trust?", "Atoms, cause they make up everything."],
        ["What do you get when you cross an elephant with a rhino?", "Elephino"],
        ["Who was the fattest knight at King Arthur's table?", "Sir Cumference, he let the pi define him."],
        ["What kind of fish has knees?", "A \'two-knee\' fish."],
        ["What is the loniest kind of cheese?", "Prov-alone"],
        ["I tried buying velcro shoes one time", "Don\'t do it, they're a total rip-off."],
        ["Where do the vampires from Twilight shop?", "Forever21"],
        ["Why doesn't Mr. Krabbs ever share his earnings with his employees?", "Cause he's shellfish."],
        ["I once ordered a thesaurus online, and when it arrived the pages were blank.", "I had no words to describe how angry I was."],
        ["Did you hear about Elon Musks' sex scandal?", "Apparently they're calling it Elon-gate."],
        ["To the person who stole my copy of Microsoft Office,", "I will find you, you have my Word!"],
        ["Few people know I simulate a priest in my off-time,", "I like to say it\'s my altar ego."],
        ["I used to stare at the ocean wondering what it would say, if it could talk;", "But alas, it only ever waved."],
        ["Did you hear about that octopus that ended the 1996 elmo craze?", "Apparently Elmo got outsold ten-tickles to one."],
        ["To the person who invented the shovel,", "You were ground-breaking!"],
        ["I find all these jokes about german sausage highly offensive;", "They\'re just the wurst."],
        ["A woman walks past the bathroom to see her husband standing on the scale, sucking in his stomach.  \"Ha, that's not going to help,\" she says;", "The man responds, \"Sure it does, it\'s the only way I can see the numbers.\""],
        ["I had a joke about a broken pencil, but I can't seem to remember how it goes....", "It doesn\'t matter anyway, it was pointless."],
        ["What country has the fastest-growing capital?", "Ireland, cause everyday it's Dublin."],
        ["The other day I had a clown open the door for me;", "Such a nice Jester."],
        ["Why can\'t you run in a campground?", "You can only \"ran\", since it\'s past tents."],
        ["Why do scuba divers fall backwards out of the boat?", "Because if they fell forwards they'd still be in the boat."],
        ["When does a joke become a dad joke?", "When it becomes apparent;", "When does it become apparent?", "After the delivery"],
        ["I never tell jokes to a klepto,","they tend to take things literally."],
        ["I was working on a construction joke,", "But it's not finished, yet."],
        ["I support 'Doctors Without Borders', because I'm well rounded.", "Besides, borders are for edgy people, that need limitations."],
        ["What do you say when a cat wins a dog show?", "That it was a cat-has-trophy!"],
        ["My wife said it was impossible for me to build a car from spaghetti", "You should have seen her face when I drove pasta."],
        ["What does 4 drinks in one hand, 5 drinks in the other equal?", "Alcoholism."],
        ["What day of the week do chickens hate the most?", "Fry-day."],
        ["A young man approaches a widow at her husbands funeral and says, 'plethora';", "The woman says, 'Thanks, that means alot.'"],
        ["Did you hear about Santa's stand-up comedy act?", "The reviews say he sleighed."],
        ["What kind of storm is always in a rush?", "A Hurricane...", "You're smirking and regretting it, so you're welcome."],
        ["A criminal is wanted for stealing wheels off police cars", "Police are working tirelessly to catch him."],
	    ["Did you hear about the cashier that scanned the eyes of a rude customer with her barcode reader.", "They said the look on her face was priceless."],
	    ["Did you hear about the toddler getting charged for being uncooperative?", "They said he refused to take a nap, and was charged for resisting a rest."],
	    ["What is the least spoken language in the world?", "...Sign Language..."],
	    ["My spouse started yelling at me for not listening to a word she was saying.", "I don't know what she's mad about, that's a weird way to start a conversation."],
	    ["I tried calling the Tinnitus hot-line one time.", "It just kept ringing"],
	    ["Fun fact: Did you know that dogs can't operate MRI equipment?", "However, cats_can"],
        ["What do sprinters eat before a race?", "Nothing, they fast!"],
        ["I watched a child go up and hug his mother, walking away they both wore large smiles;", "Walking around the corner, I hear the child tell his father, \"You're right dad, she is gaining weight.\""],
        ["Sometimes it is very important if a sentence was said by a man or a woman,", "A good example: \"I used a whole pack of tissues while watching that movie you lent me!\""],
    ],
    'taboo': [
        ["What do you get when you mix Goat DNA and Human DNA?", "Kicked out of the petting zoo."],
        ["The day the brothel closed down they hung a sign on the door,", "It read, \"Beat it, we're closed.\""],
        ["Why does Santa Claus carry around such a big sack?", "Cause he only comes once a year."],
        ["What does a vacuum cleaner, and a mans wife have in common?", "They both quit sucking after about a year and a half."],
        ["What do you call someone who refuses to fart in public?", "A private tutor."],
        ["Heard a human once say that sex was like a game of Euchre,", "With a good enough hand, you can go it alone."],
        ["What do push-up bras and bags of chip have in common?", "The let down you feel after you open it just to find it's half empty."],
        ["What did Cinderella say when she got to the ball?", "gaaaahhhggggg"],
        ["Ever wonder why after almost 60 years of making dolls, they've never made a pregnant Barbie?", "Ken has come in a different box than Barbie since 1961."],
        ["Some human was complaining in chat about their cheap circumcision;", "They said it was a total rip off."],
        ["Gonorrhea would have been a great name for diarrhea medication."],
        ["Did you hear why 7 8 9?", "To see what 6 had been braggin about.", "I'll let that one sink in for a minute."],
        ["Dating a single parent can be very awkward at first...", "It feels a bit like picking up from some else's saved game."],
        ["Leer, Flash, Harden, Withdraw, Sleep...", "When you read that list, do you think this a list of Pokemon moves, or a description of your sex life?"],
        ["I received an email the other day asking me if I believed in creationism or evolutionism...", "I never use creative mode, it's for people who can't handle the struggle."],
        ["After having children, I put in a swear jar.  Each time someone said a bad word, they had to put a dollar in;", "At the end of each month I bought myself a nice fucking steak."],
        ["A Police officer is filling out his paperwork after an arrest, he leans over to his supervisor and says is 'buttcheeks' the correct spelling?", "Without missing a beat, the prison yells from the drunk tank, 'NO! According to you, you need to spread them apart.'"],
        ["Did you hear about this whack job who coated his testicles in glitter?", "Yeah, from what the reporter was saying I guess it was pretty nuts."],
        ["I guess I scared the mailman when I answered the door in the nude.", "Never did figure out what freaked him out the most", "Maybe it was being buff in the door way, maybe it was the question of how I got in his house.  Who really knows..."],
    ],
    'gaming': [
        ["I kept dying in Overwatch earlier while playing Tracer, and the replay was corrupted", "I would like to know why, but it seems I will be unable to recall."],
        ["There was a Pokemon streamer who had his girlfriend show up during his stream and called him childish for playing the game", "He started thrashing about and roared \"You don’t have enough badges to control me!\"", "...Well played kiddo, well play."],
        ["You know when you walk into a room and forget why you went in there?", "Now you know what it feels like to be a Sim and have your action cancelled mid way."],
        ["Had a viewer one time ask me if I believed in creationism or evolutionism...","Confused I said, \"Evolutionism...cause if I'm going to get that Charizard, then I would rather earn it instead of cheat it in.\""],
        ["I heard they were making a new Minecraft Movie called TNT!!!!!","I bet it's going to be a real block-buster."],
        ["I heard this story of a guy who's girlfriend was going to leave him due to his deep-seeded obsession with Assassin's Creed...", "This was a real eye-opener for him and to say thanks he got her a card that read...", "You're absolutely right, I cannot Altair the past, and as for my games I know you Haytham, and therefor have packed my things Bayek up.  There's no need to be Frye-twins, and remember 'Nothing is true; everything is permitted'"],
        ["If you ever wanted to know what Minecraft was like,", "its Top-Notch."],
        ["I hate hearing non-gamers telling gamers to 'get a life'","I've made every birthday in Stardew Valley, built a kingdom in Minecraft, excavated an ancient tomb in Tomb Raider, and saved the world with a horse called Epona.", "All of which I did before sunrise, your move...."],
        ["What does a gorilla wear to the beach?", "Donkey Thongs"],
        ["I heard they were adding Turkies to Minecraft...", "If you listen, you can hear them in the distance. 'cobble, cobble, cobble'."],
        ["Do you know why Donkey Kong has such white teeth?", "Cause he brushes every day....to prevent tooth DK."],
        ["A pro basketball team mentioned they were looking to pick up Link as their new forward.", "I guess they finally heard how good he was with a hookshot."],
        ["Spent hours tunneling in Minecraft, and still no diamonds.", "I feel totally shafted."],
        ["What's the best spec for a druid who doesn't like to shapeshift?", "Restoration, cause once you go tree you never have to leaf it."]
    ],
    'offensive': [
        ["So, Pokemon Black came out this weekend.", "Gotta Catch Jamal."],
        ["While playing some Call of Duty with a friend, I asked him who he thought the best CoD player was,","and without missing a beat, he responded 'Hitler'...", "Confused by his response, I made the mistake of inquiring why.", "With a smirk he said, 'Dude, check his K-D.'", "...And that was the last time he we spoke."],
    ]
}

dadJokeList = jokesDict['dad'].copy()
tabooJokeList = jokesDict['taboo'].copy()
gamingJokeList = jokesDict['gaming'].copy()

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
                jokeIndex = randint(0, len(jokesDict['dad'])-1)
            response = dadJokeList.pop(jokeIndex)

        elif jokeType.lower() == "taboo":
            global tabooJokeList
            if len(tabooJokeList) < 1:
                tabooJokeList = jokesDict['taboo'][:]
            if index > -1:
                jokeIndex = index
            else:
                jokeIndex = randint(0, len(jokesDict['taboo'])-1)
            response = tabooJokeList.pop(jokeIndex)

        elif jokeType.lower() == "gaming":
            global gamingJokeList
            if len(gamingJokeList) < 1:
                gamingJokeList = jokesDict['gaming'][:]
            if index > -1:
                jokeIndex = index
            else:
                jokeIndex = randint(0, len(jokesDict['gaming'])-1)
            response = gamingJokeList.pop(jokeIndex)
        else:
            error = "Invalid Joke Type."
            response = jokesDict['dad'][randint(0, len(jokesDict['dad'])-1)]
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

def randomFacts():
    url = "http://randomfactgenerator.net/"
    r = requests.get(url)
    bs = BeautifulSoup(r.content, 'html.parser')
    fact = bs.find(id="z").text.replace('\nTweet', '')
    if '\n' in fact:
        fact = fact.replace('\n', ' ')
    return(str(fact))
