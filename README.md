# photoShare

Author: Mauro Donega`

Scripts to keep photos on my raspberry pi:
- git clone <git repo>
- put your photo originals in originals/<mydir> (create originals if it doesn't exists)
- run ./makeUpdate.sh <folderName>

The scripts will create:
- a summary web page
- a page with the thumbnails of the originals/<mydir> (or just the newly added)

To move files to the server $IPHOME:
- copyServer.py <folderName> will move the directory structure to $IPHOME:/tmp/
- from there you can use moveToWWW.sh to move it to /var/www/public/photos/<dirs>
