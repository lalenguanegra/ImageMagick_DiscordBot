@echo off
magick convert -background black -fill white -font Comic-Sans-MS -size x400  label:"ayylmao" caption.jpg
magick mogrify -resize 400x *.jpg
magick convert -append 1.jpg caption.jpg photo.jpg
del 1.jpg
del caption.jpg
