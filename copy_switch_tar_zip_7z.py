import zipfile
from  py7zr import *
import tarfile
from threading import *
import os
dir=os.getcwd()
print("enter which file need to extract tar.gz  or zip file")
print("1.tar file  2. zip file 3. 7z file")
data=int(input())
def tarfile_display():
    for path,directory,files in os.walk(dir):
        for f in files:
            if f.endswith('.tar.gz'):
                print(f)
if(data==1):
    t=Thread(target=tarfile_display)
    t.start()
"""
def zip_display():
    for path,directory,files in os.walk(dir):
        for f in files:
            if f.endswith('.zip'):
                print(f)
t1=Thread(target=zip_display)
t1.start()"""
def zipfile_fun():
    for path,directory,files in os.walk(dir):
        for f in files:
            if(f.endswith('.zip')):
                with zipfile.ZipFile(os.path.join(path,f),'r')as zip:
                    zip.printdir()
                    zip.extractall()
def tarfile_fun():
    for path,directory,files in os.walk(dir):
        for f in files:
            if(f.endswith('.tar.gz')):
                tar=tarfile.open(os.path.join(path,f),'r:gz')
                tar.extractall()
                tar.close()
def sevenzip_fun():
    for path,directory,files in os.walk(dir):
        for f in files:
            if(f.endswith('.7z')):
                    with SevenZipFile(os.path.join(path,f),'r')as zip:
                        allfiles=zip.getnames()
                        print(allfiles)
                        zip.extractall()



def default():
    print("enter the correct choice")
switcher={
        1:tarfile_fun,
        2:zipfile_fun,
        3:sevenzip_fun
        }
def switch(choice):
    switcher.get(choice, default)()
switch(data)
    
        
