class Song:
    count = 0
    genres = []
    artists =[]
    genre_count ={}
    artist_count ={}
    def __init__(self, name, artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.genres.append(genre)
        Song.artists.append(artist)

        if genre in Song.genre_count:
            Song.genre_count[genre] +=1
        else:
            Song.genre_count[genre] = 1

        if artist in Song.artist_count:
            Song.artist_count[artist] +=1
        else:
            Song.artist_count[artist] =1
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
