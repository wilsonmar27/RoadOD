import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("log_file", help="path to log file", type=str)
parser.add_argument("out", help="path to output file", type=str)
args = parser.parse_args()
log_file = args.log_file
output_file = args.out

train = [ line for line in open(log_file, 'r') if "mean_average_precision" in line ]

if os.path.exists(output_file):
    print(output_file)
    cond = input("[WARNING] This file already exists, and could cause to overwrite and "
                 "PERMANENTLY lose file \n Do you wish to continue Yes, No? [Y,N]: ")
    if cond == "N":
        raise ValueError("File already exists!")


total_mAP = []
for line in train:
    mAP = str(re.search('= (.+?) \n', line).group(1))
    mAP = mAP + "\n"
    total_mAP.append(mAP)

open(output_file,'w').writelines([ number for number in total_mAP])



