import os
import shutil

def main():
    #create 26 directories for each letter of the alphabel
    for char in "abcdefghijklmnopqrstuvwxyz":
        if os.path.exists(char) == False:
            os.mkdir(char)

    #get all file names from the directory where files are stored
    filenames = os.listdir('files')

    for filename in filenames:
        os.chdir(filename[0])  #change to the destination directory
        srcFile = "../files/" + filename
        shutil.move(srcFile, ".")  #move file from source directory
        os.chdir("..")  #return to original directory

main()