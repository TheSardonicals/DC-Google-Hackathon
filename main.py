import os
os.environ["PYSDL2_DLL_PATH"] = os.path.dirname(os.path.abspath(__file__))
from sdl2 import *
from sdl2.sdlmixer import *


class Music:
    def __init__(self):
        Mix_Init(MIX_INIT_MP3)
        Mix_OpenAudio(41000, MIX_DEFAULT_FORMAT, 2, 2048)
        self.genre = {'R&B': [], 'Soul':[],
                      'Hip-Hop': [], 'Pop':[],
                      'Rock':[], 'Alternative': [], 'Trap': []}
        self.__moodtags = {'Happy': ['R&B', 'Hip-Hop', 'Pop', 'Soul'],
                        'Angry': ['Rock', 'Trap'], 'Sad': ['Soul', 'Alternative'],
                        'Relaxed': ['Soul', 'R&B']}
        self.song = dict()
        self.playlist = []

    def add_music(self, name, path, genre = 'Alternative'):
        self.song[name] = Mix_LoadMUS(path.encode('utf-8'))
        self.genre[genre].append(name)

    def add_all_music_from_paths(self, path, subdirectories = []):
        if (len(subdirectories) > 0):
            for subdirectory in subdirectories:
                self._get_all_music((path+subdirectory), subdirectory)
        else:
            self._get_all_music(path, 'Alternative')

    def _get_all_music(self, music_path, genre):
        print(music_path)
        p = SDL_GetPlatform()
        sep = '/'
        if p == b'Windows':
            sep = '\\'
        for path in os.listdir(music_path):
            c = path.split('.mp3')
            self.add_music(c[0],(music_path+'/'+ path), genre)

    def play_music(self, song_name):
        if song_name in self.song:
           if(Mix_PlayMusic(self.song[song_name], 1)):
               return 0
           else:
               print(Mix_GetError())
               return -1
        return -1

    def pause_music(self):
        return Mix_PauseMusic()

    def queue_from_mood(self, mood):
        for key in self.genre:
            if key in self.__moodtags[mood]:
                for song in self.genre[key]:
                    self.add_song_to_queue(song)

    def add_song_to_queue(self, name):
        if self.song[name] is None:
            return 'Not in Queue'
        self.playlist.append(name)

    def play_from_queue(self):
        if len(self.playlist) == 0:
            print('No music in queue')
            return None
        music = self.playlist.pop(0)
        print(music)
        self.play_music(music)


    def get_songs_from_genre(self, genre):
        return self.genre[genre]



class User:
    def __init__(self, user_name, user_email, status = 'happy'):
        self.user_name = user_name
        self.user_email = user_email
        self.__friends = {}
        self.__status = status

    def set_status(self, mood):
        self.__status = mood

    def add_friends(self, friend_name, friend_email):
        self.__friends[friend_name] = friend_email

    def get_username(self):
        return self.user_name

    def get_email(self):
        return self.user_email

    def remove_friend(self, friend_name):
        self.__friends.pop(friend_name)



def main():
    SDL_Init(SDL_INIT_AUDIO)
    Music_Player = Music()
    Music_Player.add_all_music_from_paths('./music/', ['R&B', 'Hip-Hop', 'Trap'])
    print(Music_Player.get_songs_from_genre('R&B'))
    Music_Player.queue_from_mood('Happy')
    Music_Player.play_from_queue()
    while(Mix_PlayingMusic()):
        if(not Mix_PlayingMusic()):
            print('cool')
    print('Done playing Music')
    return 0

main()
