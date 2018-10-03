#!/usr/bin/env python
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

dadJokeList = [
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
    ["Do you know how a backwards poet writes?", "Inverse."],
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
    ["A woman walks past the bathroom to see her husband standing on the scale, sucking in his stomach.  \"Ha, that's not going to help,\" she says;", "The man responds, \"Sure it does, it\'s the only I can see the numbers.\""],
    ["After having children, I put in a swear jar.  Each time someone said a bad word, they had to put a dollar in;", "At the end of each month I bought myself a nice fucking steak."],
    ["I had a joke about a broken pencil, but I can't seem to remember how it goes....", "It doesn\'t matter anyway, it was pointless."],
    ["What country has the fastest-growing capital?", "Ireland, cause everyday it's Dublin."],
    ["The other day I had a clown open the door for me;", "Such a nice Jester."],
    ["Why can\'t you run in a campground?", "You can only \"ran\", since it\'s past tents."],
    ["Why do scuba divers fall backwards out of the boat?", "Because if they fell forwards they'd still be in the boat."],
    ["When does a joke become a dad joke?", "When it becomes apparent..;", "When does it become apparent?", "After the delivery"],
    ["I never tell jokes to a klepto,","they tend to take things literally."],
    ["I was working on a construction joke,", "But it's not finished, yet."],
    ["I support 'Doctors Without Borders', because I'm well rounded.", "Besides, borders are for edgy people, that need limitations."]
]

badJokeList = [ ["What do you get when you mix Goat DNA and Human DNA?", "Kicked out of the petting zoo."],
                ["The day the brothel closed down they hung a sign on the door,", "It read, \"Beat it, we're closed.\""],
                ["Why does Santa Claus carry around such a big sack?", "Cause he only comes once a year."],
                ["What does a vacuum cleaner, and a mans wife have in common?", "They both quit sucking after about a year and a half."],
                ["What do you call someone who refuses to fart in public?", "A private tutor."],
                ["Heard a human once say that sex was like a game of Euchre,", "With a good enough hand, you can go it alone."],
                ["What do push-up bras and bags of chip have in common?", "The let down you feel after you open it just to find it's half empty."],
                ["What did Cinderella say when she got to the ball?", "gaaaahhhggggg"],
                ["Ever wonder why after almost 60 years of making dolls, they've never made a pregnant Barbie?", "Ken has come in a different box than Barbie since 1961."],
                ["Some human was complaining in chat about their cheap circumcision;", "They said it was a total rip off."]
]

audioFiles = {"naviListen": "C:\\Users\\Jesse\\Documents\\coding\\python\\twitchbot\\sound_effects\\Navi_Listen.mp3",
              "smokeWeed": "C:\\Users\\Jesse\\Documents\\coding\\python\\twitchbot\\sound_effects\\SmokeWeedEveryday.mp3"
}

def jokes(jokeType = 'dad'):
    if jokeType.lower() == "dad":
        jokeIndex = randint(0, len(dadJokeList)-1)        
        response = dadJokeList[jokeIndex]
    elif jokeType.lower() == "bad":
        jokeIndex = randint(0, len(badJokeList)-1)                
        response = badJokeList[jokeIndex]
    else:
        response = ["Invalid Joke Type."]
    return(response)
           
def playSound(meme):
    import subprocess
    subprocess.call([cnf("CLIENT", "VLC_PATH"), audioFiles[meme], '--play-and-exit'])
    print("{} audio file was played.".format(meme))
