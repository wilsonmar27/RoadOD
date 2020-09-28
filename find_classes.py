import os
import argparse
import yololibs
import numpy as np
from glob import iglob
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory to search", type=str)
parser.add_argument("--names", help="directory to names file if not analizing .labels", type=str)
parser.add_argument("--left", help="if 1, the text box displays on the left; default right 0", type=int)
parser.add_argument("--size", help="Bar size. Value in ]0,1[, default 0.4", type=float)
parser.add_argument("--fontsize", "-fs", help="Font size of text box, default 9", type=int)
parser.add_argument("--y_limit_bottom", "-ylimb", help="Y axis bottom limit, default 0", type=int)
parser.add_argument("--y_limit_top", "-ylimt", help="Y axis top limit", type=int)
args = parser.parse_args()
search_dir = args.dir
names_path = args.names
ylimb = args.y_limit_bottom
ylimt = args.y_limit_top
size = args.size
left = args.left
fontsize = args.fontsize
ylimList = [ylimb, ylimt]

label_check = {"D00", "D01", "D10", "D11", "D20", "D40", "D43", "D44", "D50"}

if left is None or left == 0:
    left = 0.5
else:
    left = 0.05

if size is None or size == 0.4:
    size = 0.4

if fontsize is None or fontsize == 9:
    fontsize = 9

ylim = True
if ylimb is None or ylimt is None:
    ylim = False


def check_for_wrong_labels(labels_list, label_checker):
    bad = [wrong_label for wrong_label in labels_list if wrong_label not in label_checker]
    if len(bad) == 0:
        return None
    else:
        return bad


def plot(labels_dict, total_files, empty_files):
    found_labels = list(labels_dict)
    found_labels_val = list(labels_dict.values())  # this gets the value from the dictoinary
    not_empty = total_files - empty_files

    x = np.arange(len(found_labels))  # the label locations
    width = size  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(found_labels, found_labels_val, width)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Cantidad')
    ax.set_xlabel('Tipo de defecto (Etiqueta)')
    ax.set_xticks(x)
    if ylim:
        ax.set_ylim(ylimList)
    ax.set_xticklabels(found_labels)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height - 5),
                        xytext=(0, 1),  # 3 points vertical offset
                        fontsize=9,
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)

    textstr = "Total de Fotos: {}\nFotos sin Etiquetas: {}\nFotos con Etiquetas: {}".format(total_files, empty_files, not_empty)

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)

    # place a text box in upper left in axes coords
    ax.text(left, 0.95, textstr, transform=ax.transAxes, fontsize=fontsize,
            verticalalignment='top', bbox=props)

    plt.show()


class LabelCounter:
    def __init__(self, adir):
        self.labels = ""
        if names_path is None:
            self.labels = yololibs.get_labels(adir)
        else:
            self.labels = yololibs.get_lines(names_path)
        self.files = [yololibs.fix_path(file_path) for file_path in iglob(os.path.join(adir, "*.txt"))]
        self.total_files = len(self.files)

        # create a dict where keys are from the list labels and all the values are 0
        self.label_dict = dict.fromkeys(self.labels, 0)
        self.empty_files = 0
        self.bad_labels = None
        if check_for_wrong_labels(self.labels, label_check) is not None:
            self.bad_labels = set(check_for_wrong_labels(self.labels, label_check))

    def count(self):
        if self.bad_labels is None:
            for path in self.files:
                if os.path.getsize(path) == 0:  # if file is empty pass
                    self.empty_files += 1
                else:
                    f = open(path, 'r')
                    lines = f.readlines()
                    f.close()
                    for line in lines:
                        for label in self.labels:
                            if self.labels[int(line[0])] == label:
                                self.label_dict[label] += 1
        else:
            for path in self.files:
                if os.path.getsize(path) == 0:  # if file is empty pass
                    self.empty_files += 1
                else:
                    f = open(path, 'r')
                    lines = f.readlines()
                    f.close()
                    for line in lines:
                        for label in self.labels:
                            if self.labels[int(line[0])] == label and self.labels[int(line[0])] not in self.bad_labels:
                                self.label_dict[label] += 1
                        if self.labels[int(line[0])] in self.bad_labels:
                            print("[WARNING] label {} not in ditionary found in file {}"
                                  .format(self.labels[int(line[0])], path))

        return self.label_dict


print("[INFO] Searching for text files")

if yololibs.get_immediate_subdirectories(search_dir) is None:
    find_label = LabelCounter(search_dir)

    print("[INFO] Searching for labels in text files")
    found_labels_dict = find_label.count()

    total = find_label.total_files
    empty = find_label.empty_files

    print("[INFO] Ploting data")
    plot(found_labels_dict, total, empty)

else:
    sub_dir = yololibs.get_immediate_subdirectories(search_dir)
    total = 0
    empty = 0
    final_dict = dict()
    for folder in sub_dir:
        new_search = os.path.join(search_dir, folder)
        find_label = LabelCounter(new_search)

        print("[INFO] Searching for labels in text files in {}".format(new_search))
        found_labels_dict = find_label.count()
        total = total + find_label.total_files
        empty = empty + find_label.empty_files
        final_dict = yololibs.add_dict(final_dict, found_labels_dict, label_check)

    print("[INFO] Ploting data")
    plot(final_dict, total, empty)
