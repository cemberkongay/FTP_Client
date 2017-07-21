__author__ = 'cemberk'

from ftplib import FTP
import sys,os

#------ Only connections and downloads -----

ftp = FTP('*******')     #Host IP
ftp.login('******', '*******') #Host username and password
ftp.retrlines('LIST') #List files which in the main directory

while 1:
    loc = input('--> ')
    if loc == 'DWN':
        downloadFile(loc)

    def downloadFile(path):

        filename = input('Download Filename --> ')
        local_filename = os.path.join("The place where the files will be downloaded.", filename)
        lf = open(local_filename, "wb")
        ftp.retrbinary("RETR "+ filename, lf.write, 8*4096)

    ftp.cwd(loc)
    ftp.retrlines('LIST')

ftp.quit()

