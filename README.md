# kexp_sotd_collector
A quick python script to take a large folder of KEXP Song of the Day podcasts, split them into smaller folders, and fix titles.

There are currently two functions: 
 * `copy_files()` takes a large collection of files and splits them into groups of 100. It currently does not sort these files, so the order is somewhat arbitrary.
 * `adjust_title()` checks to see if the artist name is also included at the start of a song title name, and if so, removes the first instance of it. This is currently somewhat inexact: it fails to catch some cases, for unclear reasons.
 
 If you're just using `copy_files()`, you can safely comment out the mutagen imports, but otherwise this script does require 
 the [Mutagen](https://pypi.org/project/mutagen/) library, available through `pip`.
 
 To use, update the script to specify the path to the folder of music you want collected (`SRC_DIR`), and specify a folder you want as a destination (`TARGET_DIR`), uncomment the function calls, then from a prompt run:
 `python kexp_sotd.py`
 
 That's it!
