import os
import re
import argparse
from glob import iglob
from yololibs import output_file, fix_path

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory list imgs", type=str)
parser.add_argument("-out", "--output_dir", help="output file, default out.txt", type=str)
args = parser.parse_args()
search_dir = args.dir
output = args.output_dir

if output is None:
    output = "out.txt"

objFiles = [fix_path(file_path) for file_path in iglob(os.path.join(search_dir, "*.jpg"))]
output_file(output, objFiles)
