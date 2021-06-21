import unittest
from ircHandler import IRC

class TestIRCMethods(unittest.TestCase):
    def setUp(self):
        self._chatObj = IRC(['xinthral'])
        self._chatObj.connect()
        self._chatObj.authenticate()

    def test_add_channel(self):
        self._chatObj.add_channel('nerd_kommander')
        self.assertIn('nerd_kommander', self._chatObj.current_channels())

    def test_connection(self):
        self.assertIsNotNone(self._chatObj.irc)

    def test_join_channel(self):
        self._chatObj.join_channel('nerd_kommander')
        self.assertTrue(len(self._chatObj.current_channels()) == 1)

    def test_parse_message_userstate(self):
        msg = """@badge-info=;badges=moderator/1;color=;\
        display-name=Nerd_Kommander;emote-sets=0,472873131,488737509,\
        537206155;mod=1;subscriber=0;user-type=mod \
        :tmi.twitch.tv USERSTATE #xinthral"""
        obj = self._chatObj.parse_message(msg)
        self.assertEqual('USERSTATE', obj['category'])

    def test_parse_message_roomstate(self):
        msg = """@emote-only=0;followers-only=-1;r9k=0;rituals=1;room-id=36703910;slow=0;subs-only=0 :tmi.twit
        ch.tv ROOMSTATE #xinthral"""
        # FIXME
        self.assertEqual(0, 0)

    def test_part_channel(self):
        self._chatObj.part_channel('xinthral')
        self.assertEqual(len(self._chatObj.current_channels()), 0)

    def test_part_channels(self):
        self._chatObj.join_channel('xinthral')
        self._chatObj.join_channel('nerd_kommander')
        listSize = len(self._chatObj.current_channels())
        self.assertEqual(listSize, 2)
        self._chatObj.part_channels(['xinthral', 'nerd_kommander'])
        self.assertEqual(len(self._chatObj.current_channels()), 0)

    def tearDown(self):
        self._chatObj.tear_down()

# class TestMessageMethods(unittest.TestCase):
#     def test_parse_message(self):
#         pass

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)


if __name__ == '__main__':
    unittest.main()



"""
Message: _':tmi.twitch.tv HOSTTARGET #xinthral :arcangl -'_

Message: _'@msg-id=host_on :tmi.twitch.tv NOTICE #xinthral :Now hosting ArcAngL.'_

Message: _'@badge-info=;badges=moderator/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,488
737509,537206155;mod=1;subscriber=0;user-type=mod :tmi.twitch.tv USERSTATE #xinthral'_

Message: _'@emote-only=0;followers-only=-1;r9k=0;rituals=1;room-id=36703910;slow=0;subs-only=0 :tmi.twit
ch.tv ROOMSTATE #xinthral'_

Message: _'@badge-info=;badges=moderator/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,488
737509,537206155;mod=1;subscriber=0;user-type=mod :tmi.twitch.tv USERSTATE #xinthral'_

Message: _':tmi.twitch.tv CAP * ACK :twitch.tv/membership'_

Message: _':tmi.twitch.tv CAP * ACK :twitch.tv/tags'_

Message: _':tmi.twitch.tv CAP * ACK :twitch.tv/commands'_

Message: _':nerd_kommander!nerd_kommander@nerd_kommander.tmi.twitch.tv JOIN #nerd_kommander'_

Message: _':nerd_kommander.tmi.twitch.tv 353 nerd_kommander = #nerd_kommander :nerd_kommander'_

Message: _':nerd_kommander.tmi.twitch.tv 366 nerd_kommander #nerd_kommander :End of /NAMES list'_

Message: _'@badge-info=;badges=broadcaster/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,4
88737509,537206155;mod=0;subscriber=0;user-type= :tmi.twitch.tv USERSTATE #nerd_kommander'_

Message: _'@emote-only=0;followers-only=10;r9k=0;rituals=0;room-id=177511329;slow=0;subs-only=0 :tmi.twi
tch.tv ROOMSTATE #nerd_kommander'_

Message: _'@badge-info=;badges=broadcaster/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,4
88737509,537206155;mod=0;subscriber=0;user-type= :tmi.twitch.tv USERSTATE #nerd_kommander'_

Message: _'@badge-info=;badges=moderator/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,488
737509,537206155;mod=1;subscriber=0;user-type=mod :tmi.twitch.tv USERSTATE #xinthral'_

Message: _'@badge-info=;badges=moderator/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,488
737509,537206155;mod=1;subscriber=0;user-type=mod :tmi.twitch.tv USERSTATE #xinthral'_

Message: _'@badge-info=;badges=broadcaster/1,overwatch-league-insider_2019A/1;client-nonce=de1958d752ef8023a515240c77be1aa
8;color=#00FF7F;display-name=Xinthral;emotes=;flags=;id=9af0379f-a15f-4126-be26-33cb932a376c;mod=0;room-id=36703910;subscr
iber=0;tmi-sent-ts=1617450082412;turbo=0;user-id=36703910;user-type= :xinthral!xinthral@xinthral.tmi.twitch.tv PRIVMSG #xi
nthral :helllo'_

Message: _'@badge-info=;badges=moderator/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,488737509,537206155;m
od=1;subscriber=0;user-type=mod :tmi.twitch.tv USERSTATE #xinthral'_

Message: _'@badge-info=;badges=broadcaster/1,overwatch-league-insider_2019A/1;client-nonce=9378814b1c26606c44e1daa505bf4c6
3;color=#00FF7F;display-name=Xinthral;emotes=;flags=;id=1fc37498-4435-4219-8c19-f917bcaba29e;mod=0;room-id=36703910;subscr
iber=0;tmi-sent-ts=1617450088236;turbo=0;user-id=36703910;user-type= :xinthral!xinthral@xinthral.tmi.twitch.tv PRIVMSG #xi
nthral :!joke this is a joke'_

Message: _'@badge-info=;badges=moderator/1;color=;display-name=Nerd_Kommander;emote-sets=0,472873131,488737509,537206155;m
od=1;subscriber=0;user-type=mod :tmi.twitch.tv USERSTATE #xinthral'_
"""
