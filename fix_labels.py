from glob import iglob
import argparse
import sys
import os
import yololibs

flag = "\nNote on the key flag:\nPath to text file containing instructions (fix.txt)\n" \
       "keep if it doesn't appear on the fix.txt file and it is in the .names file\n" \
       "label:del =>this means delete the annotation\n" \
       "label1:label2 =>this means convert label1 to label2\n\n" \
       "Example of a fix.txt file:\n" \
       "Lizard:del\nHusky:Dog\nDoberman:Dog\n"

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(flag)

parser = argparse.ArgumentParser()
parser.add_argument("key", help="See note above", type=str)
parser.add_argument("names", help="path to the .names file containing desired output labels", type=str)
parser.add_argument("dir", help="path to text files or subdirs with txt files", type=str)
parser.add_argument("-out", "--output_dir", help="output directory", type=str)
args = parser.parse_args()
search_dir = args.dir
key_path = args.key
names_path = args.names
output_dir = args.output_dir  # None if no argument specified


def read_key(key_dir):
    keys = dict()
    key_list = yololibs.get_lines(key_dir)
    
    for k1 in range(len(key_list)):
        key_list[k1] = str(key_list[k1]).split(':')
    for k2 in range(len(key_list)):
        keys[str(key_list[k2][0])] = str(key_list[k2][1])
        
    return keys

def manage_output(output):
    out_dir = ""
    if output is None:
        out_dir = "labels_output"
        if not os.listdir(out_dir): 
            os.makedirs(out_dir)
        else: 
            print(output)
            cond = input("[WARNING] This directory is not empty\nDo you wish to continue Yes, No? [Y,N]: ")
            if cond == "N" or "n":
                raise ValueError("Specified output dir is not empty!")
            elif cond == "Y" or "y":
                os.makedirs(out_dir)
    else:
        if os.path.exists(output) and not os.path.isfile(output): 
            # Checking if the directory is empty or not 
            if not os.listdir(output):
                out_dir = output
                os.makedirs(out_dir)
            else: 
                print(output)
                cond = input("[WARNING] This directory is not empty\nDo you wish to continue Yes, No? [Y,N]: ")
                if cond == "N" or "n":
                    raise ValueError("Specified output dir is not empty!")
                elif cond == "Y" or "y":
                    os.makedirs(out_dir)
        else: 
            raise ValueError("The path is either for a file or not valid")
    
    return out_dir


class fixLabels:
    def __init__(self, adir:str):
        self.labels = yololibs.get_labels(adir)
        self.files = [yololibs.fix_path(file_path) for file_path in iglob(os.path.join(adir, "*.txt"))]
    
    def new_version(self, akey:dict, target_names:list, out_path:str):
        for path in self.files:
            if os.path.getsize(path) != 0:  # if file is empty pass
                f = open(path, 'r')
                lines = f.readlines()
                f.close()
                for line in lines:
                    for label in self.labels:
                        if self.labels[int(line[0])] == label:
                            pass      


key = read_key(key_path)
names = yololibs.get_lines(names_path)
output = manage_output(output_dir)

print("[INFO] Searching for text files")
if yololibs.get_immediate_subdirectories(search_dir) is None:
    out_folder = manage_output(output_dir)

else:
    out_folder = manage_output(output_dir)
    sub_dir = yololibs.get_immediate_subdirectories(search_dir)
    for folder in sub_dir:
        new_search = os.path.join(search_dir, folder)

        print("[INFO] Searching for labels in text files in {}".format(new_search))
