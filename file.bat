@echo off
magick convert -background black -fill white -font Candice \ -size x400  label:"Sys3 is an elite hacker!" caption.jpg
magick mogrify -resize 400x *.jpg
magick convert -append 1.jpg caption.jpg photo.jpg
del 1.jpg
del caption.jpg