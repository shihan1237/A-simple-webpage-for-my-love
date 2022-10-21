import os
import shutil

dirName = './letters'
destPic = './asd.png'


def dfs(path: str):

    dirs = os.listdir(path)
    for dir in dirs:
        if os.path.isdir(os.path.join(path, dir)):
            dfs(os.path.join(path, dir))
        else:
            if (dir.lower().endswith(('.bmp', '.dib', '.png', '.jpg',
                                      '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))):
                dir = os.path.join(path, dir)
                newPic = shutil.copy(destPic, path)
                os.remove(dir)
                os.rename(newPic, dir)


if __name__ == '__main__':
    root = os.path.abspath('')

    destPic = os.path.join(root, destPic[2:])
    dirName = os.path.join(root, dirName[2:])
    dfs(os.path.abspath(dirName))
