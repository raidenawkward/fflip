
class FileExtSwitcher:
    def __init__(self):
        self._dirname = '.'
        self._orisuffix = None
        self._dstsuffix = ''
        self._isrecursive = False
        self._excludelist = []

    def setDir(self, dirname):
        self._dirname = dirname
        return self

    def setOriSuffix(self, orisuffix):
        self._orisuffix = orisuffix
        return self

    def setDstSuffix(self, dstsuffix):
        self._dstsuffix = dstsuffix
        return self

    def addExcludeFile(self, excludefile):
        self._excludelist.append(excludefile)
        return self

    def addExcludeFiles(self, excludefiles):
        self._excludelist.extend(excludefiles)
        return self

    def setIsRecursive(self, recursive):
        self._isrecursive = recursive
        return self

    def _isFileExcluded(self, filename):
        if filename is None:
            return False
        return self._excludelist.count(filename) > 0

    def _generateNewName(self, oldname):
        if oldname is None:
            return None
        if oldname.endswith(self._orisuffix):
            return oldname[0 : oldname.rindex(self._orisuffix)] + self._dstsuffix
        else:
            return oldname

    def _renamefile(self, oripath, newpath):
        import os
        try:
            os.rename(oripath, newpath)
        except:
            return False
        return True

    def start(self):
        import os
        count = -1

        if not os.path.isdir(self._dirname):
            return count

        count = 0
        for root, subdirs, files in os.walk(self._dirname):
            for f in files:
                if f.endswith(self._orisuffix):
                    if self._isFileExcluded(f):
                        continue
                    oripath = os.path.join(root, f)
                    newname = self._generateNewName(f)
                    if newname is None:
                        continue
                    newpath = os.path.join(root, newname)
                    if self._renamefile(oripath, newpath):
                        count = count + 1

            if not self._isrecursive:
                break

        return count


if __name__ == '__main__':
    count = FileExtSwitcher().setDir('.') \
        .setOriSuffix('txt') \
        .setDstSuffix('x') \
        .setIsRecursive(False) \
        .start()
    print('file(s) flipped: ' + str(count))
