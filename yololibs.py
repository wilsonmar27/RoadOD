import os
import re
from json import loads

def fix_path(path):
    new_path = path.replace("\\", "/")
    return new_path


def get_immediate_subdirectories(a_dir):
    dirs = [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
    if not dirs:
        return None
    else:
        return dirs
    
# get lines in a file and place in a list
def get_lines(file_path):
    file_2read = open(file_path, 'r')
    lines = [w.replace('\n', '') for w in file_2read.readlines()]
    file_2read.close()
    return lines

# get labels from the _darknet.labels files
def get_labels(in_dir):
    darknet_lables_file = open(os.path.join(in_dir, "_darknet.labels"), 'r')
    labels_in_dir = [w.replace('\n', '') for w in darknet_lables_file.readlines()]
    darknet_lables_file.close()
    return labels_in_dir

# adds two dictionaries where the key is a label and the key values are ints.
def add_dict(dict1, dict2, label_checker):
    dict1_p1 = list(dict1)
    dict1_p2 = list(dict1.values())
    dict2_p1 = list(dict2)
    dict2_p2 = list(dict2.values())

    for i in range(len(dict2_p1)):
        for j in range(len(dict1_p1)):
            if dict2_p1[i] == dict1_p1[j]:
                dict1_p2[j] = int(dict1_p2[j]) + int(dict2_p2[i])
        if dict2_p1[i] not in dict1_p1 and dict2_p1[i] in label_checker:
            dict1_p1.append(dict2_p1[i])
            dict1_p2.append(int(dict2_p2[i]))
    out_dict = {dict1_p1[k]: dict1_p2[k] for k in range(len(dict1_p1))}
    return out_dict


def if_file_exists(output_file):
    if os.path.exists(output_file):
        print(output_file)
        cond = input("[WARNING] This file already exists, and could cause to overwrite and "
                    "PERMANENTLY lose file \n Do you wish to continue Yes, No? [Y,N]: ")
        if cond == "N":
            raise ValueError("File already exists!")


def new_lines(files_list):
    for i in range(len(files_list)):
        files_list[i] = files_list[i] +'\n'
    return files_list


def output_file(manage_out, files):
    out_dir = manage_out
    if_file_exists(out_dir)
    files = new_lines(files)

    with open(manage_out, 'w') as out2:
        out2.writelines(files)
        out2.close


def readjson(json_path):
    with open(json_path, 'r') as f:
        contents = f.read()
        contents = loads(contents)
    return contents