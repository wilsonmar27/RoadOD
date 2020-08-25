import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-out", "--output_dir", help="output directory", type=str)
args = parser.parse_args()
output_dir = args.output_dir

print(output_dir)