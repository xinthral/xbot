"""
ToDo:
 - Achievement System
 - Point Accrual for viewers (from streamlabs)
 - List: First 100 hellos in chat
 - SQLite integration for jokes, etc...
"""
from apiHandler import *
from featuresExtended import *
from sys import exit
from time import sleep

class CommandHandler(object):
    def __init__(self, obj, command):
        self.conn = obj.connection
        self.command = command
        self.obj = obj
        self.offlineMsg = "@{} -> The [{}] command is unavailable because it would appear that {} is offline.".format(self.obj.requestor, self.command[0], self.obj.channel_displayName)
        self.apiStreams = api_streams({'user_login': self.obj.channel_id})
        self.selector(self.command[0].lower())

    def selector(self, cmd):
        """ Selects between Command Options """
        # ===== Bot Commands ===== #
        if cmd == "greet" and self.command > 1:
            message = "Welcome {}, the regime welcomes you. Lurk, Chat, be merry!".format(self.command[1])
            self.obj.connection.privmsg(self.obj.channel, message)

        elif cmd == "game":
            try:
                r2 = api_games({'id': self.apiStreams['data'][0]['game_id']})

                # HotFix: Natural Language
                if r2['data'][0]['name'] == 'Creative':
                    action = 'being'
                else:
                    action = 'playing'

                self.obj.connection.privmsg(self.obj.channel, "@{} -> {} is currently {} {}.".format(
                    self.obj.requestor,
                    self.obj.channel_displayName,
                    action,
                    activity
                ))
            except:
                self.obj.connection.privmsg(self.obj.channel, self.offlineMsg)

        # Display current time live
        elif cmd == "uptime":
            try:
                self.obj.connection.privmsg(self.obj.channel, self.apiStreams['data'][0]['started_at'])
            except:
                self.obj.connection.privmsg(self.obj.channel, self.offlineMsg)

        # Display follower list...of some kind?
        elif cmd == "follows":
            try:
                self.obj.connection.privmsg(self.obj.channel, api_follows({'to_id': self.apiStreams['data'][0]['user_id']}))
            except:
                self.obj.connection.privmsg(self.obj.channel, self.offlineMsg)

        # Command to remove bot from channel
        elif cmd == "exitus" or cmd == "retire":
            message = "Adios Senior..."
            self.obj.connection.privmsg(self.obj.channel, message)
            self.obj.disconnect(message)
            exit(1)

        # ===== Regular Commands ===== #
        elif cmd == "build":
            buildtype, buildLink = "Minions", "https://www.pathofexile.com/forum/view-thread/2167692"
            message = "Current {} build: {}".format(buildType, buildLink)
            self.obj.connection.privmsg(self.obj.channel, message)

        elif cmd == "schedule":
            message = "A schedule hasn't been established yet, " \
                + "Xinthral's life is currently chaos."
            self.obj.connection.privmsg(self.obj.channel, message)

        elif cmd == "title":
            if self.obj.requestor.lower() in self.obj.moderators:
                try:
                    self.obj.connection.privmsg(self.obj.channel, '@{} -> Stream Title: {}'.format(
                        self.obj.requestor,
                        self.apiStreams['data'][0]['title']
                    ))
                except:
                    self.obj.connection.privmsg(self.obj.channel, self.offlineMsg)


        # ===== Extended Features ===== #
        #elif cmd == "raffle":
        #elif cmd == "stalk":
        #elif cmd == "trivia":
        #elif cmd == "yeet":
        elif cmd == "pyramid":
            #FIXME: Has no error checking or failsafes
            meme = "PogChamp"
            if len(self.command) >= 2:
                meme = self.command[1]
            msg = memePyramid(meme)
            for message in msg:
                self.obj.connection.privmsg(self.obj.channel, message)
                sleep(2)

        elif cmd == "fact":
            fact = randomFacts()
            self.obj.connection.privmsg(self.obj.channel, fact)

        elif cmd == "haiku":
            msg = haikuMe()
            for message in msg:
                self.obj.connection.privmsg(self.obj.channel, message)
                sleep(2)

        elif cmd == "jokes" or cmd == "joke":
            if len(self.command) >= 2:
                if self.command[1].lower() in self.obj.allowedJokes:
                    if len(self.command) > 2:
                        responseList = jokes(self.command[1], self.command[2])
                    else:
                        responseList = jokes(self.command[1])
                else:
                    responseList = ["I don\'t have \"{}\" jokes available, but maybe one of these? {}".format(
                        self.command[1],
                        ', '.join(self.obj.allowedJokes)
                    )]
            else:
                responseList = jokes()
                # Optional Response
                #responseList = ["What type of joke would you like? {}".format(', '.join(self.obj.allowedJokes))]

            for element in responseList:
                self.obj.connection.privmsg(self.obj.channel, element)
                sleep(4)

        elif (cmd == "help" or cmd == "commands") and self.obj.requestor.lower() in self.obj.moderators:
            msg = "The following Commands are available: "
            for each in self.obj.commandList:
                if each == self.obj.commandList[-1]:
                    msg += "{}".format(each)
                elif each != "help":
                    msg += "{}, ".format(each)
            self.obj.connection.privmsg(self.obj.channel, msg)

        elif cmd == "quote":
            if len(self.command) >= 2:
                responseList = quotes(self.command[1], self.command[2])
            else:
                responseList = quotes()

            for element in responseList:
                self.obj.connection.privmsg(self.obj.channel, element)
                sleep(4)
                
        # ===== Subscriber Commands ===== #
        #elif cmd == "name":
        #elif cmd == "fubar":
        #elif cmd == "quote":
        elif cmd == "play": #playnavi
            if len(self.command) > 1:
                if self.command[1].lower() == "weed":
                    playSound('smokeWeed')
                    message = "Smoke Weed everyday."
                elif self.command[1].lower() == "navi":
                    playSound('naviListen')
                    message = "Hey, Listen!"
                sleep(7)
                self.obj.connection.privmsg(self.obj.channel, message)

        # ===== Moderator Commands ===== #
        #elif cmd == "clip":
        elif cmd == "poll":
            message = "Polls!? Polls!? We didn't need no steenking polls!!"
            self.obj.connection.privmsg(self.obj.channel, message)

        # ===== Developmental Section ===== #
        elif cmd == "mods" and self.obj.requestor.lower() in self.obj.admins:
            if len(self.command) < 2:
                response = ', '.join(self.obj.moderators)
                self.obj.connection.privmsg(self.obj.channel, "The Current Mods Online: " + response)

            elif self.command[1].lower() == "add" and self.command[2] != None:
                self.obj.moderators.append(self.command[2].lower())
                self.obj.connection.privmsg(self.obj.channel, "@{} -> {} has been added to the mod list.".format(self.obj.requestor, self.command[2]))

        #elif cmd == "test" and self.obj.requestor in self.obj.admins:
            #response = "Test"
            #self.obj.connection.privmsg(self.obj.channel, response)

        # The command was not recognized
        else:

            self.obj.connection.privmsg(self.obj.channel, "I'm sorry {}, I'm afraid I can't do that. [{}]".
                     format(self.obj.requestor, cmd))
