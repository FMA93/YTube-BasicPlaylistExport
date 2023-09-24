import pandas as pd
from pytube import Playlist

# In this variable you need to replace the string message with the desired Youtube playlist URL
# URL of the YouTube playlist
playlist_url = "INSERT_YOUR_DESIRED_YOUTUBE_URL"

# Initialize a playlist object
playlist = Playlist(playlist_url)

# Create an empty list to store video details
video_details = []

# Loop through the videos in the playlist
for video in playlist.videos:
    # Extract video details using pytube
    title = video.title
    author = video.author
    video_url = video.watch_url
    views = video.views
    
    # Append the details to the list
    video_details.append([title, author, video_url, views])

# Create a DataFrame from the list of video details
columns = ["Title", "Author", "Video URL", "Views"]
df = pd.DataFrame(video_details, columns=columns)

# Sort the DataFrame by views in descending order
df = df.sort_values(by="Views", ascending=False)

# Export the DataFrame to an Excel file
# Here you can change the name of the output file if desired
excel_file = "sorted_playlist_basic.xlsx"
df.to_excel(excel_file, index=False, engine="openpyxl")

# This print message was made for the purpose of a YT tutorial video
# You can easily change the output if desired
print("An Excel file of the playlist details sorted on amount of views is now available you lazy B*TCH!")
