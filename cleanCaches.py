import os
import shutil



print("Start serach...")
print("............................")

DirIs = ""
for i in os.environ.keys():
    if i == "HOME":
        DirIs = "{}/Library/Caches/".format(os.environ.get(i))
        print("The dir is = {}".format(DirIs))
        for Path,NameFolder,NameFile in os.walk(DirIs):
            for x in NameFolder:
                url = "{}{}".format(Path,x)
                if os.path.isfile(url):
                    print("* Try to delete {}".format(url))
                    os.remove(url)
                elif os.path.isdir(url):
                    print("* Try to delete {}".format(url))
                    try:
                        shutil.rmtree(url)
                    except:
                        print("** Some thing is wrong **")
                print(url)

