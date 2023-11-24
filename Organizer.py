import os
import shutil

from_dir = "D:/Usuario/Downloads/"
to_dir = "D:/Usuario/Imagens/"

fileList = os.listdir(from_dir)
print(fileList)

for i in fileList:
    name,extension = os.path.splitext(i)
    print(name)
    print(extension)

    if(extension in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]):
        path1 = from_dir+i
        path2 = to_dir+"downloads"
        path3 = to_dir+"downloads/"+i
        if(os.path.exists(path2)):
            print("movendo o arquivo", i)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("movendo o arquivo", i)
            shutil.move(path1, path3)