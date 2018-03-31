# photoShare

Author: Mauro Donega`

Scripts to keep photos on my raspberry pi:
- git clone name_repository
- put your photo originals in photoShare/originals/folderName (create originals if it doesn't exists)
- run ./makeUpdate.sh folderName

The scripts will create:
- a directory with resized pictures in photoShare/large
- a directory with pictures thumbnails in photoShare/thumbnails
- a summary web page in photoShare/pages/
- a page with the thumbnails of the originals/<mydir> (or just the newly added)

To move files to the server $IP:
- copyServer.py folderName will copy the directory structure (large, thumbnails, pages) to $IP:/mnt/disk/data/www/public/photos

mp4 will be just copied over to $IP:/mnt/disk/data/www/public/photos/large
