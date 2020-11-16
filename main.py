class Track:
    def __init__(self, name = 'No name', duration = 'No duration'):
        self.name = name
        self.duration = duration

    def show(self):
        print(f"{self.name} - {self.duration}")

class Album:
    def __init__(self, name = 'No name', group = 'No group'):
        self.name = name
        self.group = group
        self.tracklist = []

    def get_tracks(self):
        for track in self.tracklist:
            track.show()

    def add_track(self, track):
        self.tracklist.append(track)

    def get_duration(self):
        summary_duration = 0
        for track in self.tracklist:
            summary_duration += track.duration
        print(f'Album duration is {summary_duration}')

song_1 = Track('First song', 1)
song_2 = Track('Second song', 2)
song_3 = Track('Third song', 3)
song_2_1 = Track('Erste song', 4)
song_2_2 = Track('Zweite song', 5)
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

album_1.get_duration()
album_2.get_duration()