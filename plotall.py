import re
import os
import argparse
from yololibs import if_file_exists

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
    epocas = []
    csv_lines =['iter, mAP\n']
    
    for i in range(len(lines)):
        if "avg loss" in lines[i]:
            loss = str(re.search(', (.+?) avg loss', lines[i]).group(1))
            loss = loss + "\n"
            total_loss.append(loss)
        if "mean_average_precision" in lines[i]:
            for k in range(3000):
                p = i - k
                if "avg loss" in lines[p]:
                    epocas.append(str(lines[p][1:5]))
                    break
            mAP = str(re.search('= (.+?) \n', lines[i]).group(1))     
            total_mAP.append(mAP)

    for j in range(len(total_mAP)):
        csv_line = epocas[j] + "," + total_mAP[j] + "\n"
        csv_lines.append(csv_line)
    return total_loss, csv_lines


if_file_exists(out_txt)
if_file_exists(out_csv)

txt, csv = find(log_file)

ftxt = open(out_txt, 'w')
ftxt.writelines(txt)
ftxt.close()

fcsv = open(out_csv, 'w')
fcsv.writelines(csv)
fcsv.close()
