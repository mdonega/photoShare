import sys
import os

# run the script from the directory that has as
# subdirectories ./originals and ./thumbnails

if len(sys.argv) == 1:     
    print "\033[0;31mNo originals directory \033[0;m"
    sys.exit()
if len(sys.argv) >  2:
    print "\033[0;31mToo many arguments \033[0;m"
    sys.exit()

originalspath = str(sys.argv[1])
print "Photo PATH = ", originalspath
originalspathPage = os.getcwd() + "/" + originalspath 

words = originalspath.split('/')

if (len(words)<2) or (words[0]!="originals") :
    print "\033[0;31mmissing originals directory \033[0;m"
    print "\033[0;31mpath = originals/NAME \033[0;m"
    sys.exit()
if not(os.path.isdir(originalspath)) :
    print "\033[0;31mmissing originals: ", originalspath, "does not exist \033[0;m"
    sys.exit()    

photodir = words[1]

photos = os.listdir(originalspath)
#rm .DS_Store
photostmp = []
for photo in photos:
    if (photo != ".DS_Store"):
        photostmp.append(photo)
photos = photostmp
photos.sort()
newPhotos = []
# print "original photos", photos

largepath = "large/"+photodir+"/"
print "Large PATH = ", largepath
print "Preparing the large format directory: ", largepath
if not(os.path.isdir("large")):
    os.mkdir("./large")
if not(os.path.isdir(largepath)):
    os.mkdir(str(largepath))

if not(os.path.isdir("thumbnails")):
    os.mkdir("./thumbnails")
if not(os.path.isdir("pages")):
    os.mkdir("./pages")

existingPhotos= []
existingPhotos_nolarge= []
existingPhotos_thumb= []

thumbpath     = "thumbnails/"+photodir
print "Preparing the thumbs directory: ", thumbpath
if not(os.path.isdir(thumbpath)):
    os.mkdir(str(thumbpath))
    for photo in photos:
        print "new Photo ", photo 
        newPhotos.append(photo)
else:
    print "\033[0;31mThe directory", thumbpath, "already exists \033[0;m"
    print "Update with the latest photos in originals"


    lsLarge = "\"ls /mnt/disk/data/www/public/photos/large/" + photodir + "/ > /mnt/disk/data/www/public/photos/large/" + photodir + "/large.lst\""
    print lsLarge
    command = "ssh mauro@$IPLOCHOME " + lsLarge
    os.system(command)
    os.system("scp mauro@$IPLOCHOME:/mnt/disk/data/www/public/photos/large/" +photodir+ "/large.lst ./")

    existingPhotos_tmp = ''
    with open('./large.lst', 'r') as myfile:
        existingPhotos_tmp=myfile.readlines()
    # print "existingPhotos_tmp = ",existingPhotos_tmp

    for photo in existingPhotos_tmp:
        if photo != "large.lst\n":
            photo = photo.replace("\n","")
            # print photo        
            existingPhotos.append(photo)
    # print "existingPhotos = ", existingPhotos
    
    for photo in existingPhotos:
        if photo != "large.lst\n":
            photo = photo.replace("large_","")
            # print photo        
            existingPhotos_nolarge.append(photo)
    # print "existingPhotos_nolarge = ", existingPhotos_nolarge

    for photo in existingPhotos:
        if photo != "large.lst\n":
            photo = photo.replace("large_","thumb_")
            # print photo        
            existingPhotos_thumb.append(photo)
    # print "existingPhotos_thumb = ", existingPhotos_thumb

    # print "PHOTOS     = ", photos

    for photo in photos:
        thumbphoto = "thumb_"+photo
        print thumbphoto
        if ( (thumbphoto in existingPhotos_thumb) or ("mp4" in photo) ) :
            if ("mp4" in photo) :
                print "Video -> ", photo
            else:
                print "existing Photo ->", photo, "-> skip"                            
        else:
            newPhotos.append(photo)
            print "new Photo -> ", photo

# print "NEWPHOTOS  = ", newPhotos

for photo in newPhotos:
    print photo

    if "mp4" not in photo:
        convertCommand = "convert -define jpeg:size=500x180 \"./" + originalspath + "/"+ photo + "\" -auto-orient -thumbnail 500x180   -unsharp 0x.5 \"" + thumbpath + "/thumb_" + photo +"\""
        os.system(convertCommand)
        convertCommand = "convert -define jpeg:size=1328x747 \"./" + originalspath + "/"+ photo + "\" -auto-orient -thumbnail 1328x747 -unsharp 0x.5 \"" + largepath + "/large_" + photo +"\"" 
        os.system(convertCommand)
        #print convertCommand
    
# PHOTO PAGES

webpagename  = "./pages/"+photodir+".html"
webpagetitle = "<title>" + photodir + "</title>"
webpagetitleHTML = "<font color=\"lightgrey\" size =+3>"+ photodir +"</font><p>\n"
webpage      = open(webpagename, 'w+')
webpage.write("<html>\n")
webpage.write("<head>\n")
webpage.write(webpagetitle)
webpage.write("</head>\n")
webpage.write("\n")
webpage.write("<!--==================================================================-->\n")
webpage.write("<!--                         STYLE SHEETS                             -->\n")
webpage.write("<!--==================================================================-->\n")
webpage.write("\n")
webpage.write("<style type=\"text/css\">\n")
webpage.write("<!--\n")
webpage.write("body\n")
webpage.write("{ ; -webkit-background-size: cover\n")
webpage.write("  ; -moz-background-size: cover\n")
webpage.write("  ; background-size: cover\n")
webpage.write("  ; font-family      :  Noteworthy, Arial, helvetica, Verdana, sans-serif\n")
webpage.write("  ; margin-left      : 0in\n")
webpage.write("  }\n")
webpage.write("hr\n")
webpage.write("{ width            : 100%\n")
webpage.write("  }\n")
webpage.write("td\n")
webpage.write("{ font-family      : Noteworthy, Arial, helvetica, Verdana, sans-serif\n")
webpage.write("  }\n")
webpage.write("-->\n")
webpage.write("</style>\n")
webpage.write("<STYLE>\n")
webpage.write("<!--\n")
webpage.write("A{text-decoration:none}\n")
webpage.write("-->\n")
webpage.write("</STYLE>\n")
#colors at http://www.computerhope.com/htmcolor.htm
webpage.write("<body text=\"#FFFFFF\" bgcolor=\"#2C3539\" link=\"#FFFF00\" vlink=\"#FFFF00\" alink=\"#FFFF00\" >\n")
webpage.write("\n")
webpage.write("         <p>&nbsp;\n")
webpage.write("         <p>&nbsp;\n")
webpage.write("         <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n")
webpage.write(webpagetitleHTML)
#webpage.write("<tablestyle=\"width:100%\">")
#photosPerLine = 2
#countPhotos =1
#webpage.write("<tr>\n")

videoLines = []

photos = existingPhotos_nolarge+newPhotos

tmpphotos = []
for photo in photos:
    photo = photo.replace("\n","")
    # print photo        
    tmpphotos.append(photo)
photos = tmpphotos
# print "final list ", photos

photos.sort()

for photo in photos:
    # line = "<td> <a href=\"../" + originalspath + photo + "\"><img src=\"../" + thumbpath + "/thumb_" + photo + "\"></a></td>"
    if "mp4" not in photo:
        line = "<a href=\"../" + largepath + "large_" + photo + "\"><img src=\"../" + thumbpath + "/thumb_" + photo + "\"></a>"
        webpage.write(line)
    else:
        line = "<a href=\"../" + largepath + photo + "\">" + photo + "</a><br>"
        videoLines.append(line)

#    countPhotos+=1
#    if countPhotos%photosPerLine == 0:
#        webpage.write("</tr>\n")
#        webpage.write("<tr>\n")
#        countPhotos =1
#webpage.write("</tr>\n")
#webpage.write("</table>\n")

webpage.write("<p>\n")
webpage.write("Videos\n")
webpage.write("<p>\n")

for video in videoLines:
    webpage.write(video)
webpage.write("</body>\n")
webpage.write("</html>\n")

# INDEX PAGE

indexpagename  = "./photos.html"
indexpagetitle = "<title> Photos </title>"
indexpagetitleHTML = "<font color=\"lightgrey\" size =+3> Photos</font><p>\n"
indexpage      = open(indexpagename, 'w+')
indexpage.write("<html>\n")
indexpage.write("<head>\n")
indexpage.write("<p>&nbsp;\n")
indexpage.write("<p>&nbsp;\n")
indexpage.write("&nbsp;&nbsp;&nbsp;&nbsp;My Photos")
indexpage.write("<p>")
indexpage.write("</head>\n")
indexpage.write("\n")
indexpage.write("<!--==================================================================-->\n")
indexpage.write("<!--                         STYLE SHEETS                             -->\n")
indexpage.write("<!--==================================================================-->\n")
indexpage.write("\n")
indexpage.write("<style type=\"text/css\">\n")
indexpage.write("<!--\n")
indexpage.write("body\n")
indexpage.write("{ ; -webkit-background-size: cover\n")
indexpage.write("  ; -moz-background-size: cover\n")
indexpage.write("  ; background-size: cover\n")
indexpage.write("  ; font-family      :  Noteworthy, Arial, helvetica, Verdana, sans-serif\n")
indexpage.write("  ; margin-left      : 0in\n")
indexpage.write("  }\n")
indexpage.write("hr\n")
indexpage.write("{ width            : 100%\n")
indexpage.write("  }\n")
indexpage.write("td\n")
indexpage.write("{ font-family      : Noteworthy, Arial, helvetica, Verdana, sans-serif\n")
indexpage.write("  }\n")
indexpage.write("-->\n")
indexpage.write("</style>\n")
indexpage.write("<STYLE>\n")
indexpage.write("<!--\n")
indexpage.write("A{text-decoration:none}\n")
indexpage.write("-->\n")
indexpage.write("</STYLE>\n")
#colors at http://www.computerhope.com/htmcolor.htm
indexpage.write("<body text=\"#FFFFFF\" bgcolor=\"#2C3539\" link=\"#B6B6B4\" vlink=\"#B6B6B4\" alink=\"#B6B6B4\" >\n")
indexpage.write("<br>")
htmls = os.listdir("./pages/")
for html in htmls:
    line = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href=\"./pages/" + html  +  "\">" + html + "</a><br>"
    indexpage.write(line)
indexpage.write("</body>\n")
indexpage.write("</html>\n")
