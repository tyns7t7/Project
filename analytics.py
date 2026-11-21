import numpy as np
import pandas as pd

def run_data_analysis(file_name):
    print("\n================ PANDAS DATA ANALYSIS ================")
    df = pd.read_csv(file_name)

    df["Duration_Sec"] = df["Duration_Sec"].fillna(df["Duration_Sec"].mean())
    df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

    print("\n1. Top 5 Songs (Title, Artist, Rating):")
    print(df[["Title", "Artist", "Rating"]].head(5))

    top_rated = df[df["Rating"] >= 4.8]
    print(f"\n2. High Rated Songs (Rating >= 4.8): {len(top_rated)} songs found.")

    longest_songs = df.sort_values(by="Duration_Sec", ascending=False)
    print("\n3. Top 5 Longest Songs:")
    print(longest_songs[["Title", "Duration_Sec"]].head(5))

    print("\n4. Average Rating by Genre (GroupBy):")
    print(df.groupby("Genre")["Rating"].mean().round(2))

    print("\n5. Overall Statistical Summary (Pandas describe):")
    print(df[["Year", "Duration_Sec", "Rating"]].describe().round(2))

    print("\n================ NUMPY DATA ANALYSIS ================")
    durations_1d = np.array(df["Duration_Sec"])
    stats_2d = np.array(df[["Year", "Rating"]])

    print("First song duration (Indexing):", durations_1d[0])
    print("First 5 song durations (Slicing):", durations_1d[0:5])
    print("First 2 rows of 2D array (Year, Rating):\n", stats_2d[0:2])

    print("\nTotal Library Duration (sec):", round(np.sum(durations_1d), 2))
    print("Average Song Duration (sec):", round(np.mean(durations_1d), 2))
    print("Longest Song Duration (sec):", round(np.max(durations_1d), 2))
    print("Shortest Song Duration (sec):", round(np.min(durations_1d), 2))
    print("Standard Deviation of Duration:", round(np.std(durations_1d), 2))