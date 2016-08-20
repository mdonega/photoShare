#!/bin/bash
for i in `ls originals`; do
    sudo mkdir /var/www/public/photos/originals/$i
    sudo mv originals/$i/* /var/www/public/photos/originals/$i/
    sudo mkdir /var/www/public/photos/thumbnails/$i
    sudo mv thumbnails/$i/* /var/www/public/photos/thumbnails/$i/
done
sudo mv *.html       /var/www/public/photos/pages/

rmdir originals/*
rmdir originals
rmdir thumbnails/*
rmdir thumbnails