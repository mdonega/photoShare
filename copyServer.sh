#!/bin/bash
args=("$@")
if  [ -z "$1" ]; then
    echo "Missing folder name"
    echo "Usage: ./copyServer.sh <folder name>"
    exit -1
fi
DIR=${args[0]}
echo Copying to server $DIR

ssh mauro@$IPLOCHOME "mkdir -p /mnt/disk/data/www/public/photos/large/$DIR"
scp large/$DIR/*.jpg mauro@$IPLOCHOME:/mnt/disk/data/www/public/photos/large/$DIR/
scp originals/$DIR/*.mp4 mauro@$IPLOCHOME:/mnt/disk/data/www/public/photos/large/$DIR/
ssh mauro@$IPLOCHOME "mkdir -p /mnt/disk/data/www/public/photos/thumbnails/$DIR"
scp thumbnails/$DIR/thumb*.jpg mauro@$IPLOCHOME:/mnt/disk/data/www/public/photos/thumbnails/$DIR/
scp pages/$DIR.html mauro@$IPLOCHOME:/mnt/disk/data/www/public/photos/pages/
