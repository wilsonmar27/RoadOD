import os
import math
import shutil
import random
import argparse
from glob import iglob
from yololibs import fix_path

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory to split in validation and test", type=str)
parser.add_argument("percent", help="percent of images to go to validation (1-100)", type=int)
args = parser.parse_args()
search_dir = args.dir
percent = int(args.percent)


def collect_names(adir):
    filelist = [fix_path(file_path)[:-4] for file_path in iglob(os.path.join(adir, "*.txt"))]
    return filelist

#percent asigned to valid ej (0.20) is 20%
def split(somedir: str, percent: float):
    filesList = collect_names(somedir)
    validQ = math.floor(len(filesList) * percent)
    validN = random.sample(range(0, len(filesList) - 1), validQ)
    valid_txt = []
    valid_jpg = []
    
    for i in range(len(validN)):
        valid_element = filesList[validN[i]]
        valid_txt.append(valid_element + '.txt')
        valid_jpg.append(valid_element + '.jpg')
    
    os.mkdir('test')
    os.mkdir('obj')
    
    if len(valid_jpg) != len(valid_txt):
        raise ValueError("Length of jpg list does not match length of txt list")
    
    for j in range(len(valid_txt)):
        shutil.move(valid_jpg[j], './test/')
        shutil.move(valid_txt[j], './test/')
    
    objP = collect_names(search_dir)
    for path in objP:
        obj_txt = path + '.txt'
        obj_jpg = path + '.jpg'
        shutil.move(obj_txt, './obj/')
        shutil.move(obj_jpg, './obj/')



split(search_dir, percent)
