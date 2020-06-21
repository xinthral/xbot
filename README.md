# xbot
Python Twitch Bot

In order for this to work, you need a settings.config file containing the following:
```
[AUTH]
NICK = #PROJECT NAME (optional) 
LONG_NAME = #DISPLAY NAME 
CHANNEL_ID = 36703910
CLIENT_ID = #CLIENT KEY 
ACCESS_TOKEN = #TWICH SECRET KEY 
REFRESH_TOKEN = #API SECRET KEY (optional) 

[SERVER]
HOST = irc.chat.twitch.tv
PORT = 6667
CHANNEL = #Default Channel Name 

[ADMIN]
OWNERS = xinthral #Developer username here (would recommend leaving as singular)
ADMINS = #Comma Seperated List of Authorized Admin usernames here 
AUTH_COMMANDS = #Comma Seperated List of commands allowed to run 
AUTH_JOKES = #Comma Seperated List of allowed joke types 

[DEV]
DEBUG = False

[CLIENT]
VLC_PATH = C:\\Program Files\\VideoLAN\\VLC\\vlc.exe #Path to VLC  
```
