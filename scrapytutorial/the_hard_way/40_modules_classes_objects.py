# coding: utf-8

mystuff = {'apples': 'I AM APPLES'}
print mystuff


# this goes in mystuff.py
def apple():
    print 'I AM APPLES!'


apple()


class MyStuff(object):
    def __init__(self):
        self.tangerine = "I'm creating a __init__ function"

    def apple(self):
        print 'I am classy apples'


thing = MyStuff()
thing.apple()
print thing.tangerine


class Song(object):
    def __init__(self, lyrics):
        self.lyric = lyrics

    def sing_me_a_song(self):
        for line in self.lyric:
            print line


happy_bday = Song(
    ["when you were here before", "couldn't look you in the eyes", "you look like an angel", "your skin makes me cry"])


bulls_on_parade = Song(["我要从南走到北", "我还要从白走到黑"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
