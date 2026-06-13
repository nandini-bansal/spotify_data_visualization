import json
import pandas as pd
import matplotlib.pyplot as plt

# Load Spotify Library JSON
with open(
    r'C:\Users\nandi\Downloads\my_spotify_data\Spotify Account Data\YourLibrary.json',
    'r',
    encoding='utf-8'
) as file:
    data = json.load(file)

# Convert tracks into DataFrame
tracks_df = pd.DataFrame(data['tracks'])

# Check first few rows (not an important step, this is just to see how data looks)
#print(tracks_df.head())

# Count songs by artist
artist_counts = tracks_df['artist'].value_counts()

# Top 10 artists
top_artists = artist_counts.head(10)
print(top_artists)

# Plotting Graph 1
plt.figure(figsize=(10, 6))
fig=top_artists.sort_values().plot(kind='barh',color='orchid',edgecolor='black')
#title of the graph
plt.title('Top 10 Artists in My Spotify Library')
#naming the x-axis
plt.xlabel('Number of Saved Songs')
#naming the y-axis
plt.ylabel('Artist')
#setting a range forr the x-axis
plt.xlim(0,35)
#setting a background color
fig.patch.set_facecolor("oldlace")
plt.show()



#Plotting Graph 2
album_counts = tracks_df['album'].value_counts()
top_albums = album_counts.head(3)
plt.figure(figsize=(8,5))
print(top_albums)
figs=top_albums.plot(kind='line',linewidth=4,marker="*",markersize=20,color='seagreen')
plt.title('Top 3 Albums in My Spotify Library')
plt.xlabel('Album')
plt.ylabel('Number of Songs')
figs.patch.set_facecolor("powderblue")
plt.ylim(2,7)
plt.show()

#Plotting Graph 3
artist_counts = tracks_df['artist'].value_counts()
top5 = artist_counts.head(5)
others = artist_counts.iloc[5:].sum()
pie_data = pd.concat(
    [top5, pd.Series({'Others': others})]
)
plt.figure(figsize=(8,8))
custom_colors=["red","lime","fuchsia","yellow","indigo","cyan"]
plt.pie(
    pie_data,
    labels=pie_data.index,
    colors=custom_colors,
    autopct='%1.1f%%'
)
plt.title('Artist Distribution in My Spotify Library')
plt.show()

#Final Analysis
total_songs = len(tracks_df)
unique_artists = tracks_df['artist'].nunique()
print("Total Songs:", total_songs)
print("Unique Artists:", unique_artists)
diversity = (unique_artists / total_songs) * 100
print("Artist Diversity Score:", round(diversity, 2), "%")