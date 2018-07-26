#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import os
import shutil
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import EasyMP3

N = 100 # the number of files in each subfolder
SRC_DIR = "/Volumes/Durandal/Music/iTunes/Podcasts/KEXP Song of the Day/"
TARGET_DIR = "/Users/nadreck/src/KEXP/"

def copy_files():
	"""Copy Files into subdirectory"""
	songs = []
	dirn = 100
	
	for (dirpath, dirnames, filenames) in os.walk(SRC_DIR):
		songs.extend(filenames)
	
	for num, name in enumerate(songs):
		if num % N == 0:
			dirn = num + N
			print("Making folder {0:04d}".format(dirn))
			folder_name = "{0:04d}".format(dirn)
			os.mkdir(TARGET_DIR + folder_name)
		source_name = SRC_DIR + name
		target_name = TARGET_DIR + folder_name + os.sep + name
		print("Copying {} to {}".format(source_name, target_name))
		shutil.copy2(source_name, target_name)

def adjust_title():
	for subdir, dirs, files in os.walk(TARGET_DIR):
		for file in files:
			#print os.path.join(subdir, file)
			filepath = subdir + os.sep + file
			
			if filepath.endswith(".mp3"):
				song = mutagen.mp3.EasyMP3(filepath)
				for title in song['title']:
					print(title)
					songtitle = title
				for artist in song['artist']:
					print(artist)
					songartist = artist
				if songtitle.startswith(artist):
					newtitle = title.replace(artist + " - ", '', 1)
					print(newtitle)
					song['title'] = newtitle
					song.save()					
				print("---")
		
#copy_files()
#adjust_title()
