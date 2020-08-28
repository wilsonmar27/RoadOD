import os
from yololibs import fix_path, get_immediate_subdirectories
from glob import iglob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory to search", type=str)
args = parser.parse_args()
search_dir = args.dir


def delTxt (adir):
    filelist = [fix_path(file_path) for file_path in iglob(os.path.join(adir, "*.txt"))]
    for f in filelist:
        os.remove(f)
   

print("[INFO] Searching for text files")
if get_immediate_subdirectories(search_dir) is None:
    print("[INFO] Deleting text files")
    delTxt(search_dir)

else:
    sub_dir = get_immediate_subdirectories(search_dir)
    for folder in sub_dir:
        new_search = os.path.join(search_dir, folder)
        print("[INFO] Deleting text files in {}".format(new_search))
        delTxt(new_search)