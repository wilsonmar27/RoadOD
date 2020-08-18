import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("log_file", help="path to log file", type=str)
parser.add_argument("out", help="path to output file", type=str)
args = parser.parse_args()
log_file = args.log_file
output_file = args.out

train = [ line for line in open(log_file, 'r') if "avg loss" in line ]

if os.path.exists(output_file):
    print(output_file)
    cond = input("[WARNING] This file already exists, and could cause to overwrite and "
                 "PERMANENTLY lose file \n Do you wish to continue Yes, No? [Y,N]: ")
    if cond == "N":
        raise ValueError("File already exists!")

total_loss = []
for line in train:
    loss = str(re.search(', (.+?) avg loss', line).group(1))
    loss = loss + "\n"
    total_loss.append(loss)
    
open(output_file,'w').writelines([ number for number in total_loss])
