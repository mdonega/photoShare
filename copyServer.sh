#!/bin/bash
DIR=Mallorca
echo $DIR
ssh mauro@$IPHOME "mkdir /var/www/photos/originals/$DIR"
scp originals/$DIR/*.jpg mauro@$IPHOME:/var/www/photos/originals/$DIR
ssh mauro@$IPHOME "mkdir /var/www/photos/thumbnails/$DIR"
scp thumbnails/$DIR/thumb*.jpg mauro@$IPHOME:/var/www/photos/thumbnails/$DIR/
scp pages/$DIR.html mauro@$IPHOME:/var/www/photos/pages/
