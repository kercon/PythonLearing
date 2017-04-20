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

