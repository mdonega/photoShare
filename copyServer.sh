#!/bin/bash
args=("$@")
if  [ -z "$1" ]; then
    echo "Missing folder name"
    echo "Usage: ./copyServer.sh <folder name>"
    exit -1
fi
DIR=${args[0]}
echo Copying to server $DIR

ssh mauro@$IPHOME "mkdir -p /tmp/originals/$DIR"
scp originals/$DIR/*.jpg mauro@$IPHOME:/tmp/originals/$DIR/
ssh mauro@$IPHOME "mkdir -p /tmp/thumbnails/$DIR"
scp thumbnails/$DIR/thumb*.jpg mauro@$IPHOME:/tmp/thumbnails/$DIR/
scp pages/$DIR.html mauro@$IPHOME:/tmp/
