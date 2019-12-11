from os import listdir
import shutil
import getpass
import glob, os


#Get name of current user
username = os.getlogin()

#Path in which we are looking to clean up random files
basepath = 'C:/Users/' + username + '/Downloads'    

#Image file types we're looking for 
imgs = ['*.jpg', '*.jpeg', '*.jpe', '*.jif', '*.jfif','*.jfi', '*.png',
    '*.gif', '*.webp', '*.tiff', '*.psd', '*.raw', '*.bmp', '*.heif',
    '*.indd', '*.svg', '*.ai', '*.eps', '*.tif']
#New folder in which we will move these files types to
imgs_path = basepath + '/Images'

#Compressed file types and new directory for them
zips = ['*.zip', '*.7z', '*.jar', '*.rar']
zips_path = basepath + '/ZIP'

#Exe file types and new directory for them
exes = ['*.exe']
exe_path = basepath + '/EXEs'

#Doc file types and new directory for them
docs = ['*.doc', '*.txt', '*.docx', '*.log']
docs_path = basepath + '/Docs'

#Audio file types and new directory for them
audios = ['*.m4a', '*.wav', '*.mp3']
audio_path = basepath + '/Music'

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

#Run function to move files to their paths
file_to_path(imgs, basepath, imgs_path)
file_to_path(zips, basepath, zips_path)
file_to_path(exes, basepath, exe_path)
file_to_path(docs, basepath, docs_path)
file_to_path(audios, basepath, audio_path)
