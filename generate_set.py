import os
import re
import argparse
from glob import iglob
from yololibs import output_file, fix_path

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="directory thats has imgs you want to list", type=str, required=True)
parser.add_argument("-out", "--output", help="output file, default out.txt", type=str)
args = parser.parse_args()
search_dir = args.dir
output = args.output

if output is None:
    output = "out.txt"

objFiles = [fix_path(file_path) for file_path in iglob(os.path.join(search_dir, "*.jpg"))]
output_file(output, objFiles)
