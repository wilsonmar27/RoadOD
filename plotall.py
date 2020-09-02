import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("log_file", help="path to log file", type=str)
parser.add_argument("out_txt", help="path to output txt file", type=str)
parser.add_argument("out_csv", help="path to output csv file", type=str)
args = parser.parse_args()
log_file = args.log_file
out_txt = args.out_txt
out_csv = args.out_csv


def find(log_path):
    f = open(log_path, 'r')
    lines = f.readlines()
    f.close()
    total_loss = []
    total_mAP = []
    csv_lines =['mAP,iter\n']
    
    for i in range(len(lines)):
        if "avg loss" in lines[i]:
            loss = str(re.search(', (.+?) avg loss', lines[i]).group(1))
            loss = loss + "\n"
            total_loss.append(loss)
        if "mean_average_precision" in lines[i]:
            mAP = str(re.search('= (.+?) \n', lines[i]).group(1))     
            total_mAP.append(mAP)
    
    for i in range(len(total_mAP)):
        num = 1000 + i*100
        csv_line = str(num) + "," + total_mAP[i] + "\n"
        csv_lines.append(csv_line)
    return total_loss, csv_lines


def if_file_exists(output_file):
    if os.path.exists(output_file):
        print(output_file)
        cond = input("[WARNING] This file already exists, and could cause to overwrite and "
                    "PERMANENTLY lose file \n Do you wish to continue Yes, No? [Y,N]: ")
        if cond == "N":
            raise ValueError("File already exists!")

if_file_exists(out_txt)
if_file_exists(out_csv)

txt, csv = find(log_file)

ftxt = open(out_txt, 'w')
ftxt.writelines(txt)
ftxt.close()

fcsv = open(out_csv, 'w')
fcsv.writelines(csv)
fcsv.close()
