import os
import shutil

path = input("Enter Path:")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extenaion+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
