__author__ = 'cemberk'

from ftplib import FTP
import sys, os


def downloadFile(dwn):
    try:
        filename = input('Download Filename --> ')  # Download edilecek dosyanın ismi alınır.
        local_filename = os.path.join("/home/user/Desktop/newFile",
                                      filename)  # Dosyanın nereye download edileceği istenir.
        lf = open(local_filename, "wb")  # Dosya oluşturulup, yazma izni oluşturulur.
        ftp.retrbinary("RETR " + filename, lf.write, 8 * 4096)  # Bu fonksiyon ile download işlemi gerçekleştirilir.
        print("Complete!")
    except:
        pass


def uploadFile(upd):
    filePath = input("File Path --> ")  # Dosyanın bilgisayardaki yol bilgisi girilir.
    fileName = input("Upload Filename --> ")  # Upload edilecek dosyanın ismi girilir.
    ftpPath = input("FTP Folder Path --> ")  # FTP de nereye yükleneceğini bilgisi girilir.
    ftp.cwd("/" + ftpPath)  # ftp de yüklenecek dizine gidilir.
    os.chdir(filePath)  # Dosyaya ulaşım sağlar.
    file = open(fileName, 'rb')  # Dosyayı okur.
    ftp.storlines("STOR " + fileName, file)  # Dosyayı FTP'ye bu fonksiyon ile upload eder.
    file.close()
    print("Complete!")
    ftp.retrlines('LIST')  # Mevcut dizini listeler.


def deleteFile(dlt):
    try:
        filename = input('Delete Filename --> ')
        ftp.delete(filename)  # Silinecek dosya bu fonkisyon ile ftp server üzerinde silinir.
        print("Complete!")
        ftp.retrlines('LIST')  # Mevcut dizini listeler.

    except:
        pass


def createFolder(crt):
    foldername = input('Folder Name --> ')  # Oluşturulucak klasör adı.

    if foldername in ftp.nlst():  # ftp.nlst dizindeki sadece dosya isimlerini listeler.
        print(
            'The name ' + foldername + ' is already used in this location. Please use a different name.')  # Girilen dosya adı mevcutsa aynı isimde dosya oluşturmaz.
        ftp.cwd(foldername)  # mevcut o isimdeki klasöre gider.
        ftp.retrlines('LIST')  #klasördeki dosyaları listeler.

    else:
        print(
            'Create a new directory called ' + foldername + ' on the server.')  # Girilen dosya mevcut değilse istenen isimde klasörü oluşturur.
        ftp.mkd(foldername)  # Klöser bu satırda oluşturulur.
        ftp.cwd(foldername)  # Oluşturulan klösere gider.
        ftp.retrlines('LIST')  # Oluşturulan klasördeki dosyaları listeler.


def renameFolder(rnm):
    rename = input('Rename Folder --> ')  # İsmi değiştirelecek dosyanın adı.
    toname = input('Toname --> ')  # Dosyanın yeni adı.
    ftp.rename(rename, toname)  # Bu fonksiyonla isim değiştirilir.
    ftp.retrlines('LIST')  # Mevcut dizini listeler.


def permissionChange(perm):
        nameFile = input("Filename -->") #İzni değiştirilecek dosyanın adı alınır.
        perm = input("Entry File Permissions --> ") #Dosya izin kodu girili 555 veya 666 veya 777.
        ftp.sendcmd('SITE CHMOD' + perm + nameFile) #Kullanıcının girdiği koda göre izin değiştirilir.

def moveFile(mv):
    mvfile = input('Moving File--> ')  # İsmi değiştirelecek dosyanın adı.
    newfilepath = input('New Path --> ')  # Dosyanın yeni adı.
    ftp.rename(mvfile, newfilepath+"/"+mvfile)  # Bu fonksiyonla isim değiştirilir.
    ftp.retrlines('LIST')  # Mevcut dizini listeler.

print('---------------------------------------')
print('--FTP CLIENT--')
print('Download ---> "DWN" ')
print('Upload ---> "UPD" ')
print('Delete ---> "DLT" ')
print('Create New Folder ---> "CRT" ')
print('Rename Folder ---> "RNM" ')
print('Permission Settings ---> "PERM" ')
print('Move File ---> "MV" ')
print('Back directory ---> ".." ')
print('---------------------------------------')
ftp = FTP('++++++++++++')  # Host IP
ftp.login('++++++', '++++++')  # Host kullanıcı adı ve parola
ftp.retrlines('LIST')  # Ana dizindeki dosyaları listeleme

while 1:
    loc = input('--> ')

    if loc == 'DWN':
        downloadFile(loc)
    elif loc == 'UPD':
        uploadFile(loc)
    elif loc == 'DLT':
        deleteFile(loc)
    elif loc == 'CRT':
        createFolder(loc)
    elif loc == 'RNM':
        renameFolder(loc)
    elif loc == 'PERM':
        permissionChange(loc)
    elif loc == "MV":
        moveFile(loc)
    else:
        ftp.cwd(loc)
        print(ftp.pwd())
        ftp.retrlines('LIST')


ftp.quit()
ftp.close()
