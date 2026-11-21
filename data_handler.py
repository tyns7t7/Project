import csv
import os

FILE_NAME = "music_library.csv"

def create_initial_dataset():
    if not os.path.exists(FILE_NAME):
        songs = [
            ["Blinding Lights", "The Weeknd", "Pop", 2019, 200, 4.9],
            ["Hotel California", "Eagles", "Rock", 1976, 391, 4.8],
            ["Shape of You", "Ed Sheeran", "Pop", 2017, 233, 4.5],
            ["Bohemian Rhapsody", "Queen", "Rock", 1975, 354, 4.9],
            ["Levitating", "Dua Lipa", "Pop", 2020, 203, 4.6],
            ["Smells Like Teen Spirit", "Nirvana", "Rock", 1991, 301, 4.7],
            ["Starboy", "The Weeknd", "Pop", 2016, 230, 4.7],
            ["Lose Yourself", "Eminem", "Hip-Hop", 2002, 326, 4.9],
            ["Believer", "Imagine Dragons", "Rock", 2017, 204, 4.6],
            ["Uptown Funk", "Bruno Mars", "Pop", 2014, 270, 4.8],
            ["God's Plan", "Drake", "Hip-Hop", 2018, 198, 4.4],
            ["Rolling in the Deep", "Adele", "Pop", 2010, 228, 4.7],
            ["Stairway to Heaven", "Led Zeppelin", "Rock", 1971, 482, 4.9],
            ["HUMBLE.", "Kendrick Lamar", "Hip-Hop", 2017, 177, 4.6],
            ["Closer", "The Chainsmokers", "EDM", 2016, 244, 4.3],
            ["Wake Me Up", "Avicii", "EDM", 2013, 247, 4.7],
            ["Titanium", "David Guetta", "EDM", 2011, 245, 4.5],
            ["Faded", "Alan Walker", "EDM", 2015, 212, 4.6],
            ["Animals", "Martin Garrix", "EDM", 2013, 304, 4.2],
            ["Take Five", "Dave Brubeck", "Jazz", 1959, 324, 4.8],
            ["So What", "Miles Davis", "Jazz", 1959, 562, 4.7],
            ["Fly Me to the Moon", "Frank Sinatra", "Jazz", 1964, 147, 4.8],
            ["What a Wonderful World", "Louis Armstrong", "Jazz", 1967, 139, 4.9],
            ["Autumn Leaves", "Bill Evans", "Jazz", 1959, 360, 4.5],
            ["Kesariya", "Arijit Singh", "Bollywood", 2022, 268, 4.7],
            ["Tum Hi Ho", "Arijit Singh", "Bollywood", 2013, 262, 4.9],
            ["Channa Mereya", "Arijit Singh", "Bollywood", 2016, 289, 4.8],
            ["Kal Ho Naa Ho", "Sonu Nigam", "Bollywood", 2003, 321, 4.8],
            ["Kun Faya Kun", "A.R. Rahman", "Bollywood", 2011, 473, 4.9],
            ["Jai Ho", "A.R. Rahman", "Bollywood", 2008, 319, 4.6],
            ["Save Your Tears", "The Weeknd", "Pop", 2020, 215, 4.7],
            ["Perfect", "Ed Sheeran", "Pop", 2017, 263, 4.6],
            ["Someone Like You", "Adele", "Pop", 2011, 285, 4.8],
            ["Sweet Child O' Mine", "Guns N' Roses", "Rock", 1987, 356, 4.8],
            ["Back in Black", "AC/DC", "Rock", 1980, 255, 4.7],
            ["Numb", "Linkin Park", "Rock", 2003, 187, 4.9],
            ["In the End", "Linkin Park", "Rock", 2000, 216, 4.9],
            ["Mockingbird", "Eminem", "Hip-Hop", 2004, 250, 4.8],
            ["Sicko Mode", "Travis Scott", "Hip-Hop", 2018, 312, 4.5],
            ["Hotline Bling", "Drake", "Hip-Hop", 2015, 267, 4.3],
            ["Levels", "Avicii", "EDM", 2011, 199, 4.7],
            ["Alone", "Marshmello", "EDM", 2016, 273, 4.4],
            ["Scared to Be Lonely", "Martin Garrix", "EDM", 2017, 220, 4.5],
            ["My Way", "Frank Sinatra", "Jazz", 1969, 275, 4.8],
            ["Feeling Good", "Nina Simone", "Jazz", 1965, 174, 4.7],
            ["Apna Bana Le", "Arijit Singh", "Bollywood", 2022, 261, 4.6],
            ["Tera Ban Jaunga", "Akhil Sachdeva", "Bollywood", 2019, 236, 4.5],
            ["Raataan Lambiyan", "Jubin Nautiyal", "Bollywood", 2021, 230, 4.6],
            ["As It Was", "Harry Styles", "Pop", 2022, 167, ""],
            ["Bad Guy", "Billie Eilish", "Pop", 2019, "", 4.4]
        ]
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Artist", "Genre", "Year", "Duration_Sec", "Rating"])
            writer.writerows(songs)

def load_library():
    library = []
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            song_tuple = (row[0], row[1], row[2], row[3], row[4], row[5])
            library.append(song_tuple)
    return library

def save_library(library):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Artist", "Genre", "Year", "Duration_Sec", "Rating"])
        for song in library:
            writer.writerow(song)