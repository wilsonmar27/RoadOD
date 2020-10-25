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
parser.add_argument("-k", "--key", help="See note above", type=str, required=True)
parser.add_argument("-n", "--names", help="path to the .names file containing desired output labels", type=str, required=True)
parser.add_argument("-i", "--input_dir", help="path to text files or subdirs with txt files", type=str, required=True)
parser.add_argument("-out", "--output_dir", help="output directory", type=str)
args = parser.parse_args()
search_dir = args.dir
key_path = args.key
names_path = args.names
output_dir = args.output_dir  # None if no argument specified


def read_key(key_dir: str, name_path: str):
    key_list = yololibs.get_lines(key_dir)
    names_list = yololibs.get_lines(name_path)
    for k1 in range(len(key_list)):
        key_list[k1] = str(key_list[k1]).split(':')
    for k2 in range(len(names_list)):
        key_list.append([names_list[k2]])
    return key_list


def valid_names(direc:list):
    out_set = set()
    for value in direc:
        out_set.add(str(value[0]))
    return out_set


def manage_output(manage_dir):
    out_dir = ""
    if manage_dir is None:
        out_dir = "labels_output"
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        elif not os.listdir(manage_dir):
            print(manage_dir)
            cond = input("[WARNING] This directory is not empty\nDo you wish to continue Yes, No? [Y,N]: ")
            if cond == "N" or "n":
                raise ValueError("Specified output dir is not empty!")
            elif cond == "Y" or "y":
                os.makedirs(out_dir)
    else:
        out_dir = manage_dir
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        elif os.path.exists(manage_dir) and not os.path.isfile(manage_dir):
            # Checking if the directory is empty or not
            if not os.listdir(manage_dir):
                os.makedirs(out_dir)
            else:
                print(manage_dir)
                cond = input("[WARNING] This directory is not empty\nDo you wish to continue Yes, No? [Y,N]: ")
                if cond == "N" or "n":
                    raise ValueError("Specified output dir is not empty!")
                elif cond == "Y" or "y":
                    os.makedirs(out_dir)
        else:
            raise ValueError("The path is either for a file or not valid")

    return out_dir


def new_version(adir: str, out_path: str, direction: set, target_names: list, valid: set):
    labels = yololibs.get_labels(adir)
    files = [yololibs.fix_path(file_path) for file_path in iglob(os.path.join(adir, "*.txt"))]
    for path in files:
        file_name = path.split("/")[-1]
        if os.path.getsize(path) == 0:  # if file is empty write empty
            f = open(os.path.join(out_path, file_name), 'w')
            f.close()
        else:
            fIn = open(path, 'r')
            lines = fIn.readlines()
            fIn.close()
            fOut = open(os.path.join(out_path, file_name), 'w')
            for line in lines:
                label = labels[int(line[0])]
                if label in valid:
                    for element in direction:
                        if label == element[0]:
                            if len(element) == 1:
                                name_index = target_names.index(str(element[0]))
                                new_line = str(name_index) + line[1:]
                                fOut.write(new_line)
                            elif len(element) == 2 and element[1] == 'del':
                                pass
                            elif len(element) == 2 and element[1] in target_names:
                                name_index = target_names.index(str(element[1]))
                                new_line = str(name_index) + line[1:]
                                fOut.write(new_line)
                else:
                    print("[WARNING] label {} not a valid namee found in file {}"
                          .format(label, path))
            fOut.close()


directions = read_key(key_path, names_path)
validNmaes = valid_names(directions)
names = yololibs.get_lines(names_path)
output = manage_output(output_dir)

print("[INFO] Searching for text files")
if yololibs.get_immediate_subdirectories(search_dir) is None:
    new_version(search_dir, output, directions, names, validNmaes)

else:
    sub_dir = yololibs.get_immediate_subdirectories(search_dir)
    for folder in sub_dir:
        new_search = os.path.join(search_dir, folder)
        print("[INFO] Searching for labels in text files in {}".format(new_search))
        new_folder = manage_output(yololibs.fix_path(os.path.join(output, folder + "text")))
        new_version(new_search, new_folder, directions, names, validNmaes)
