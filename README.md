# xbot
Python Twitch Bot

In order for this to work, you need a settings.config file containing the following:
```
[AUTH]

IDENT = #Profile Identity 

NICK = #PROJECT NAME (optional) 

LONG_NAME = #DISPLAY NAME 

CHANNEL_ID = 36703910

CLIENT_ID = #CLIENT KEY 

IRC_SECRET = #TWICH SECRET KEY 

XAPI_SECRET = #API SECRET KEY (optional) 

[SERVER]

HOST = irc.chat.twitch.tv

PORT = 6667

CHANNEL = #Default Channel Name 

[ADMIN]

OWNERS = #Developer username here (would recommend leaving as singular)

ADMINS = #Comma Seperated List of Authorized Admin usernames here 

AUTH_COMMANDS = #Comma Seperated List of commands allowed to run 

AUTH_JOKES = #Comma Seperated List of allowed joke types 

[DEV]

DEBUG = False

[CLIENT]

VLC_PATH = #Path to VLC  
```
