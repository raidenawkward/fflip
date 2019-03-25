from fileextswitcher import FileExtSwitcher

def printhelp():
    print("usage: fflip dirname orisuffix dstsuffix")

def main():
    import sys, os
    if len(sys.argv) < 4:
        printhelp()
        return

    dirname = sys.argv[1]
    orisuffix = sys.argv[2]
    dstsuffix = sys.argv[3]

    if not os.path.isdir(dirname):
        print("dirname is not a dir")
        return

    count = FileExtSwitcher().setDir(dirname) \
        .setOriSuffix(orisuffix) \
        .setDstSuffix(dstsuffix) \
        .setIsRecursive(False) \
        .start()

    print('file(s) flipped: ' + str(count))



if __name__ == '__main__':
    main()