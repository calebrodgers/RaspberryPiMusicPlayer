#!/usr/bin/env python3


# Script from calebrodgers.com, 2021

import os
from omxplayer.player import OMXPlayer

from gpiozero import Button

# Root directory for the program to look for audio files
music_dir = "music"

# List of acceptable files - program will ignore files that do not match one of the types during indexing
acceptable_filetypes = ['MP3', 'M4A', 'FLAC', 'WAV', 'WMA', 'AAC']

# Creating button objects - change the numbers if you connected the buttons to different GPIO pins
back_btn = Button(4, bounce_time=0.2)
pp_btn = Button(3, bounce_time=0.2)
fwrd_btn = Button(2, bounce_time=0.2)

# Function to go through and index all audio files in the 'music_dir'
tracks = []
def index_music():
    dir_tracks = []
    for possible_track in os.listdir(music_dir):
        track_text, track_extension = os.path.splitext(possible_track)
        track_extension = track_extension[1:].upper()
        if track_extension in acceptable_filetypes:
            dir_tracks.append(f'{music_dir}/{possible_track}')

    for i in range(0, len(dir_tracks)):
        tracks.append(os.path.abspath(dir_tracks[i]))

print("Indexing Music")
index_music()
print("Indexing Complete")

players = []
current_player = 0
currently_playing = 0

def exit_event(player, exit_status):
    global players
    global current_player
    global currently_playing
    print("Track Finished - Playing Next Track")
    if currently_playing == len(tracks)-1:
        play_track(0, False)
    else:
        play_track(currently_playing+1, False)

def empty_exit(player, exit_status):
    exit_status = exit_status

def play_track(track, quit):
    global players
    global current_player
    global currently_playing
    if quit:
        players[current_player].quit()
    players.append(OMXPlayer(tracks[track]))
    current_player = len(players) - 1
    players[current_player].exitEvent = exit_event
    currently_playing = track
    print(f"Now Playing: {os.path.basename(tracks[currently_playing])}")

def play_pause():
    global players
    global current_player
    global currently_playing
    players[current_player].play_pause()
    print("Playing/Pausing Track")

def next_track():
    global players
    global current_player
    global currently_playing
    print("Next Track")
    players[current_player].exitEvent = empty_exit
    if currently_playing == len(tracks)-1:
        play_track(0, True)
    else:
        play_track(currently_playing+1, True)

def prev_track():
    global players
    global current_player
    global currently_playing
    print("Previous Track")
    players[current_player].exitEvent = empty_exit
    if currently_playing == 0:
        play_track(len(tracks)-1, True)
    else:
        play_track(currently_playing-1, True)

back_btn.when_pressed=prev_track
pp_btn.when_pressed=play_pause
fwrd_btn.when_pressed=next_track

play_track(0, False)

while True:
    status = players[current_player].playback_status