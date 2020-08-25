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
parser.add_argument("dir", help="path to text files or subdirs", type=str)
args = parser.parse_args()
search_path = args.dir
key_path = args.key
names_path = args.names


def read_key(key_dir):
    keys = dict()
    key_list = yololibs.get_lines(key_dir)
    for k in range(len(key_list)):
        key_list[k] = str(key_list[k]).split(':')
    
    