from bs4 import BeautifulSoup
import requests
import pafy
from prettytable import PrettyTable
from pytube import YouTube
from pprint import pprint
import os, sys
import re

# Written by Daniel Koifman(A.K.A HeliosHype) and Alex Putilin
# You are allowed to freely use, edit, modify and distribute this script, just make sure to give proper credit :)
# Also, if you want to ontribute to the code, send me a fork request. Once you're done, send in a pull request.
# Please make sure do properly document your contribution!



# TODO: how to handle playlists?


song_titles = []
i = 1
z = 1


def downloadSong(url):
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    yt = YouTube()
    yt.url = url
    os.system('cls') # os.system('clear') for linux.
    print "Download URL fetched successfully!\n"
    print "1. Get the list of available streams"
    print "2. Get the highest resolution available"
    print "3. Start download the video\n"

    while True:
        print "Select an action: "
        action = raw_input("> ")

        if action == str(1):
            print "Availabile streams for the URL: \n"
            pprint(yt.videos)
            print "\n"

        elif action == str(2):
            print "Highest resolution is:"
            pprint(yt.filter('mp4')[-1])
            print "\n"

        elif action == str(3):
            print "Starting download: \n"
            best.download(quiet=False)
            print "Download finished!, the file has been downloaded to the same folder where the script is located."
            sys.exit(0)

        else:
            print "Not a valid option!\n"

def download_playlist(playlist_url):
    try:
        pl = pafy.get_playlist(playlist_url)
        for i in pl['items']:
            a = i['pafy'].getbest(preftype="mp4")
            a.download()
    except Exception, e:
        print e

#print("\n\t1. Songs\n\t2. Playlists")

#choice = raw_input("Enter your selection: ")
#if choice == "1":
#    get_song()
#elif choice == "2":
#    pass
    #get_playlist()
#else:
#    print "Not a valid option!\n"


songName = raw_input("Enter the name of the song: ")
artistName = raw_input("Enter the name of the artist: ")

# Making the song name and the artist name appear in a queryable format
replacedSongName = songName.replace(" ", "+")
replacedArtistName = artistName.replace(" ", "+")
song_titles = []
playlist_titles = []
collect_lengths = []
playlist_lengths = []
i = 1
z = 1

# for i in playlist_lengths:
#...  m = re.findall(r"(\d.*videos)", i)
#...   x.append(m)



#url = "https://www.youtube.com/results?search_query=%s+%s" % (replacedSongName, replacedArtistName)

# Playlists
playlist_url = "https://www.youtube.com/results?filters=playlist&lclk="\
"playlist&search_query={}+{}".format(replacedSongName, replacedArtistName)
source = requests.get(playlist_url)
plain = source.text
soup = BeautifulSoup(plain)
for item in soup.findAll('a', {'class': 'yt-uix-tile-link yt-ui-ellipsis\
    yt-ui-ellipsis-2 yt-uix-sessionlink     spf-link '}):
    playlist_titles.append(item.string)
    i += 1

for item in soup.findAll('a', {'class': ' yt-uix-sessionlink spf-link '}):
    collect_lengths.append(item.string[-12:])
for i in collect_lengths:
    match = re.findall(r"(\d.*videos)", i)
    playlist_lengths.append(match) 
p = [str(i[0]) for i in playlist_lengths]


x = PrettyTable(["Playlist name"])
x.align["Playlist name"] = "p"
x.padding_width = 10
for title in zip(playlist_titles, p):
    x.add_row([str(z) + "." + title[0] + " | " + title[1]])
    z += 1
print x
video_number = raw_input("Enter the number of the video to download: ")

for title in soup.findAll('a', {'title': playlist_titles[int(video_number)-1]}):
    link_to_download = "http://www.youtube.com" + title.get("href")


#downloadSong(link_to_download)

#source_code = requests.get(url)
#plain_text = source_code.text
#soup = BeautifulSoup(plain_text)
#for SongTitle in soup.findAll('a', {'class': 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink     spf-link '}):
#    song_titles.append(SongTitle.string)
#    i += 1


#x = PrettyTable(["Video name"])
#x.align["Video name"] = "l"
#x.padding_width = 10
#for title in song_titles:
#    x.add_row([str(z) + "." + title])
#    z += 1
#print x




#video_number = raw_input("Enter the number of the video to download: ")


#for title in soup.findAll('a', {'title': song_titles[int(video_number)-1]}):
#    link_to_download = "http://www.youtube.com" + title.get("href")


#downloadSong(link_to_download)
#download_playlist(link_to_download)
