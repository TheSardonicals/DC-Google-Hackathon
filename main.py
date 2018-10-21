import os
os.environ["PYSDL2_DLL_PATH"] = os.path.dirname(os.path.abspath(__file__))
from sdl2 import *
from sdl2.sdlmixer import *

class Music:
    def __init__(self):
        Mix_Init(MIX_INIT_MP3)
        Mix_OpenAudio(41000, MIX_DEFAULT_FORMAT, 2, 2048)
        self.genre = {'R&B': ['Cocoa Butter Kisses'], 'Soul':[],
                      'Hip-Hop': [], 'Pop':[],
                      'Rock':[], 'Alternative': [], 'Trap': []}
        self.song = dict()
        self.playlist = []

    def add_music(self, name, path, genre = 'Alternative'):
        self.song[name] = Mix_LoadMUS(path.encode('utf-8'))
        self.genre[genre].append(name)

    def play_music(self, song_name):
        if song_name in self.song:
            return Mix_PlayMusic(self.song[song_name], 1)
        return -1

    def pause_music(self):
        return Mix_PauseMusic()

    def add_song_to_queue(self, name):
        if not self.song[name]:
            return 'Not in Queue'
        self.playlist.append((name, self.song[name]))

    def play_from_queue(self):
        if len(self.playlist) == 0:
            print('No music in queue')
            return None
        music = self.playlist.pop(0)
        Mix_PlayMusic(music[1],1)
        return music[0]


class User:
    def __init__(self, user_name, user_email, friends, status, preferences):
        self.__user_name = user_name
        self.__user_email = user_email
        self.__friends = {}
        self.__status = status
        self.preferences = {'R&B': True, 'Soul': True,
                      'Hip-Hop': True, 'Pop': True,
                      'Rock': True, 'Alternative': True,
                      'Trap': True}


    def set_status(self, mood):
        self.__status = mood

    def add_friends(self, friend_name, friend_email):
        self.__friends[friend_name] = friend_email

    def remove_friend(self, friend_name):
        self.__friends.pop(friend_name)

    def change_preferences(self, genre, preference):
        self.preferences[genre] = preference


class PublicDiary:
    def __init__(self, user_name):
        self.posts = list()
        self.user_name = user_name

    def __addPost__(self, post):
        self.posts.append(post)

    def getPosts(self):
        for post in self.posts:
            print(post.thoughts, "\n")


class PrivateDiary:
    def __init__(self, user_name):
        self.posts = list()
        self.__user_name = user_name

    def __addPost__(self, post):
        self.posts.append(post)

    def getPosts(self):
        for post in self.posts:
            print(post.thoughts, "\n")


class Post:
    def __init__(self, user_name, thoughts, time, public):
        self.thoughts = thoughts
        self.time = time
        self.__user_name = user_name
        self.public = public


def main():
    SDL_Init(SDL_INIT_AUDIO)
    Music_Player = Music()

    Music_Player.add_music('Cocoa Butter Kisses', 'music/Cocoa Butter Kisses.mp3', 'R&B')
    Music_Player.play_music('Cocoa Butter Kisses')
    while(Mix_PlayingMusic()):
        if(not Mix_PlayingMusic()):
            print('cool')
    print('Done playing Music')
    return 0

main()
