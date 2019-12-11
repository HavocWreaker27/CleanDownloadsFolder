import os
from os import listdir
from os.path import isfile, join
from os import walk
import shutil
import glob, os

#Path in which we are looking to clean up random files
basepath = 'C:/Users/Ryan/Downloads/'    

#Image file types and new directory for them
imgs_path = 'C:/Users/Ryan/Downloads/Images'
imgs = ['*.jpg', '*.jpeg', '*.jpe', '*.jif', '*.jfif','*.jfi', '*.png',
    '*.gif', '*.webp', '*.tiff', '*.psd', '*.raw', '*.bmp', '*.heif',
    '*.indd', '*.svg', '*.ai', '*.eps', '*.tif']

#Compressed file types and new directory for them
zips_path = 'C:/Users/Ryan/Downloads/ZIP'
zips = ['*.zip', '*.7z', '*.jar']

#Exe file types and new directory for them
exe_path = 'C:/Users/Ryan/Downloads/EXEs'
exes = ['*.exe']

#Doc file types and new directory for them
docs_path = 'C:/Users/Ryan/Downloads/Docs'
docs = ['*.doc', '*.txt', '*.docx', '*.log']

#Audio file types and new directory for them
audio_path = 'C:/Users/Ryan/Downloads/Music'
audios = ['*.m4a', '*.wav', '*.mp3']

#Function to handle path creation and moving of files
def file_to_path(files, src, destination):
    os.chdir(src)
    for i in files:
        for file in glob.glob(i):
            print(file)
            if len(file) > 0:
                if not os.path.exists(destination):
                    os.makedirs(destination)
                shutil.move(join(src, file), destination)

file_to_path(imgs, basepath, imgs_path)
file_to_path(zips, basepath, zips_path)
file_to_path(exes, basepath, exe_path)
file_to_path(docs, basepath, docs_path)
file_to_path(audios, basepath, audio_path)








#for i in imgs:
 #   for file in glob.glob(i):
  #      print(file)
   #     shutil.move(join(basepath, file), imgs_path)"""
    
    #for file in glob.glob("*.jpg" or "*.zip"):
     #   print(file)
        

    #return False