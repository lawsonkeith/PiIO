#!/bin/sh
echo do
convert PiIO_DO.jpg -print "Size: %wx%h\n"  /dev/null
echo dio
convert PiIO_DIO.jpg -print "Size: %wx%h\n"  /dev/null
echo adio
convert PiIO_ADIO.jpg -print "Size: %wx%h\n"  /dev/null
echo 232
convert PiIO_232.jpg -print "Size: %wx%h\n"  /dev/null
echo DIO H
convert PiIO_DIOH_ASS.png -print "Size: %wx%h\n"  /dev/null
echo DIO HZ
convert PiIO_DIO_HZ_ASS.png -print "Size: %wx%h\n"  /dev/null
echo
echo convert cmd is....
echo "convert -resize 35% PiIO_DIO_HZ_ASS.png PiIO_DIO_HZ_ASS.png"
