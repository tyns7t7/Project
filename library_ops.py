def display_all_songs(library):
    print("\n--- ALL SONGS IN LIBRARY ---")
    for index, song in enumerate(library, start=1):
        print(f"{index}. {song[0]} | Artist: {song[1]} | Genre: {song[2]} | Year: {song[3]} | Duration: {song[4]}s | Rating: {song[5]}")
    print(f"Total Songs: {len(library)}\n")

def search_songs(library):
    keyword = input("Enter keyword to search (Title, Artist, or Genre): ").lower()
    search_results = []

    for song in library:
        if keyword in song[0].lower() or keyword in song[1].lower() or keyword in song[2].lower():
            search_results.append(song)

    if len(search_results) > 0:
        print(f"\nFound {len(search_results)} match(es):")
        for song in search_results:
            print(f"- {song[0]} by {song[1]} ({song[2]}, {song[3]})")
    else:
        print("\nNo matches found.")

def add_song(library):
    title = input("Enter Song Title: ")
    artist = input("Enter Artist Name: ")
    genre = input("Enter Genre: ")
    year = input("Enter Release Year: ")
    duration = input("Enter Duration (in seconds): ")
    rating = input("Enter Rating (1.0 to 5.0): ")

    new_song = (title, artist, genre, year, duration, rating)
    library.append(new_song)
    print(f"\n'{title}' added successfully!")
    return library

def update_song(library):
    target = input("Enter the exact Title of the song to update: ").lower()
    found = False

    for i in range(len(library)):
        if library[i][0].lower() == target:
            print("Enter new details:")
            title = input("New Title: ")
            artist = input("New Artist: ")
            genre = input("New Genre: ")
            year = input("New Year: ")
            duration = input("New Duration (sec): ")
            rating = input("New Rating: ")

            library[i] = (title, artist, genre, year, duration, rating)
            found = True
            print("\nSong updated successfully!")
            break

    if not found:
        print("\nSong not found.")
    return library

def delete_song(library):
    target = input("Enter the exact Title of the song to delete: ").lower()
    found = False

    for song in library:
        if song[0].lower() == target:
            library.remove(song)
            found = True
            print(f"\n'{song[0]}' deleted successfully!")
            break

    if not found:
        print("\nSong not found.")
    return library

def show_data_structure_summary(library):
    genres_set = set()
    genre_count = {}

    for song in library:
        genre = song[2]
        genres_set.add(genre)
        genre_count[genre] = genre_count.get(genre, 0) + 1

    print("\n--- LIBRARY SUMMARY REPORT ---")
    print("Unique Genres (Set):", genres_set)
    print("Songs per Genre (Dictionary):")
    for genre, count in genre_count.items():
        print(f"  {genre}: {count} songs")