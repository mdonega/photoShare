#!/bin/bash
args=("$@")
DIR=${args[0]}
echo Updating directory $DIR

echo Cleaning
rm */*~ 
rm */*/*~ 
#rm thumbnails/$DIR/thumb*.jpg -f
#rmdir thumbnails/$DIR/
echo Run makePage
#python makePage.py originals/$DIR/
python updatePage.py originals/$DIR/

