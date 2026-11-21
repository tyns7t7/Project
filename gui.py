import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import data_handler

data_handler.create_initial_dataset()
library = data_handler.load_library()

def show_songs(song_list):
    for row in table.get_children():
        table.delete(row)
    for song in song_list:
        table.insert("", tk.END, values=song)

def search_songs():
    keyword = search_entry.get().lower()
    search_results = []

    for song in library:
        if keyword in song[0].lower() or keyword in song[1].lower() or keyword in song[2].lower():
            search_results.append(song)

    if len(search_results) > 0:
        show_songs(search_results)
    else:
        messagebox.showinfo("Search Result", "No matches found.")

def add_song():
    title = simpledialog.askstring("Add Song", "Enter Song Title:")
    if not title:
        return
    artist = simpledialog.askstring("Add Song", "Enter Artist Name:")
    genre = simpledialog.askstring("Add Song", "Enter Genre:")
    year = simpledialog.askstring("Add Song", "Enter Release Year:")
    duration = simpledialog.askstring("Add Song", "Enter Duration (sec):")
    rating = simpledialog.askstring("Add Song", "Enter Rating (1.0 - 5.0):")

    new_song = (title, artist, genre, year, duration, rating)
    library.append(new_song)
    data_handler.save_library(library)
    show_songs(library)
    messagebox.showinfo("Success", f"'{title}' added!")

def delete_song():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please click a song in the table first.")
        return

    song_values = table.item(selected[0])["values"]
    target_title = str(song_values[0]).lower()

    for song in library:
        if song[0].lower() == target_title:
            library.remove(song)
            break

    data_handler.save_library(library)
    show_songs(library)
    messagebox.showinfo("Deleted", f"'{song_values[0]}' deleted!")

def show_summary():
    genres_set = set()
    genre_count = {}

    for song in library:
        genre = song[2]
        genres_set.add(genre)
        genre_count[genre] = genre_count.get(genre, 0) + 1

    report = f"Total Songs: {len(library)}\n\nUnique Genres:\n{', '.join(genres_set)}\n\nSongs per Genre:\n"
    for genre, count in genre_count.items():
        report += f"- {genre}: {count} songs\n"

    messagebox.showinfo("Library Summary Report", report)

window = tk.Tk()
window.title("Music Keyword Library Searcher")
window.geometry("800x500")

top_frame = tk.Frame(window)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Keyword:").pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(top_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Button(top_frame, text="Search", command=search_songs).pack(side=tk.LEFT, padx=5)
tk.Button(top_frame, text="Show All", command=lambda: show_songs(library)).pack(side=tk.LEFT, padx=5)

columns = ("Title", "Artist", "Genre", "Year", "Duration", "Rating")
table = ttk.Treeview(window, columns=columns, show="headings", height=15)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120)

table.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

bottom_frame = tk.Frame(window)
bottom_frame.pack(pady=10)

tk.Button(bottom_frame, text="Add Song", width=15, command=add_song).pack(side=tk.LEFT, padx=10)
tk.Button(bottom_frame, text="Delete Selected", width=15, command=delete_song).pack(side=tk.LEFT, padx=10)
tk.Button(bottom_frame, text="Summary Report", width=15, command=show_summary).pack(side=tk.LEFT, padx=10)

show_songs(library)

window.mainloop()