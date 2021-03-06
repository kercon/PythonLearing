import codecs
import os


def directory():
    print(os.getcwd())


def makedirectory():
    os.makedirs('.\\test', exist_ok=True)


def getfiles():
    savefile = open('.\\test\\file.txt', 'w')
    path = 'E:\\Anime'
    for n in os.listdir(path):
        print(n)
        savefile.write(n+'\n')
        if os.path.isdir(path+'\\'+n):
            for m in os.listdir(path+'\\'+n):
                print(n+'\\'+m)
                savefile.write('\t'+n+'\\'+m+'\n')
    savefile.close()


def getfilestree():
    savefile = codecs.open('.\\test\\file2.txt', 'w', 'utf-8')
    path = 'E:\\Anime'
    for folderName, subfolders, filenames in os.walk(path):
        savefile.write(str(folderName) + '\n')
        print(folderName)
        # for subfolder in subfolders:
        # savefile.write(str(subfolder) + '\n')
        # print(subfolder)
        for filename in filenames:
            # print(filename)
            savefile.write('\t' + str(filename) + '\n')
    savefile.close()
