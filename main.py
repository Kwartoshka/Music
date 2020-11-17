class Track:
    def __init__(self, name = 'No name', duration = 'No duration'):
        self.name = name
        self.duration = duration

    def __str__(self):
        return(f"{self.name} - {self.duration} min\n")

    def __lt__(self, other):
        if not isinstance(self, Track) or not isinstance(self, Track):
            print("One ore more positions aren't tracks")
            return
        return self.duration < other.duration

    def __le__(self, other):
        if not isinstance(self, Track) or not isinstance(self, Track):
            print("One ore more positions aren't tracks")
            return
        return self.duration <= other.duration


class Album:
    def __init__(self, name = 'No name', group = 'No group'):
        self.name = name
        self.group = group
        self.tracklist = []

    def get_tracks(self):
        for track in self.tracklist:
            print(track)

    def add_track(self, track):
        self.tracklist.append(track)

    def get_duration(self):
        summary_duration = 0
        for track in self.tracklist:
            summary_duration += track.duration
        print(f'Album duration is {summary_duration}')

    def __str__(self):
        a = '\n'.join([str(track) for track in self.tracklist])
        b= f'Album - {self.name}\nGroup - {self.group}\n{a}\n'
        return b


song_1 = Track('First song', 1)
song_2 = Track('Second song', 2)
song_3 = Track('Third song', 3)
song_2_1 = Track('Erste song', 4)
song_2_2 = Track('Zweite song', 2)
song_2_3 = Track('Dritte song', 6)

album_1 = Album('Album №1', 'The Numbers')
album_2 = Album('Album №2', 'The Numbers')

album_1.add_track(song_1)
album_1.add_track(song_2)
album_1.add_track(song_3)
album_2.add_track(song_2_1)
album_2.add_track(song_2_2)
album_2.add_track(song_2_3)

# album_1.get_tracks()
# album_2.get_tracks()
#
# album_1.get_duration()
# album_2.get_duration()

print(song_1)
print(song_2)
print(song_3)
print(song_2_1)
print(song_2_2)
print(song_2_3)

print(album_2)
print(album_1)

print(song_1 > song_2)
print(song_1 < song_2)
print(song_2 >= song_2_2)
print(song_2_3 <= song_2_1)