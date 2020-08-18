import os
import argparse
import numpy as np
from glob import iglob
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory to search", type=str)
args = parser.parse_args()
search_dir = args.dir

label_check = {"D00", "D01", "D10", "D11", "D20", "D40", "D43", "D44", "D50"}


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


def plot(labels_dict, total_files, empty_files):
    found_labels = list(labels_dict)
    found_labels_val = list(labels_dict.values())  # this gets the value from the dictoinary
    not_empty = total_files - empty_files

    x = np.arange(len(found_labels))  # the label locations
    width = 0.6  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(found_labels, found_labels_val, width)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Cantidad')
    ax.set_xlabel('Tipo de defecto (Etiqueta)')
    ax.set_xticks(x)
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

    textstr = "Fotos: {}\nSin Etiquetas: {}\nCon Etiquetas: {}".format(total_files, empty_files, not_empty)

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)

    # place a text box in upper left in axes coords
    ax.text(0.65, 0.95, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)

    plt.show()


def get_labels(in_dir):
    darknet_lables_file = open(os.path.join(in_dir, "_darknet.labels"), 'r')
    labels_in_dir = [w.replace('\n', '') for w in darknet_lables_file.readlines()]
    darknet_lables_file.close()
    return labels_in_dir


def check_for_wrong_labels(labels_list):
    bad = [wrong_label for wrong_label in labels_list if wrong_label not in label_check]
    if len(bad) == 0:
        return None
    else:
        return bad


def add_dict(dict1, dict2):
    dict1_p1 = list(dict1)
    dict1_p2 = list(dict1.values())
    dict2_p1 = list(dict2)
    dict2_p2 = list(dict2.values())

    for i in range(len(dict2_p1)):
        for j in range(len(dict1_p1)):
            if dict2_p1[i] == dict1_p1[j]:
                dict1_p2[j] = int(dict1_p2[j]) + int(dict2_p2[i])
        if dict2_p1[i] not in dict1_p1 and dict2_p1[i] in label_check:
            dict1_p1.append(dict2_p1[i])
            dict1_p2.append(int(dict2_p2[i]))
    out_dict = {dict1_p1[k]: dict1_p2[k] for k in range(len(dict1_p1))}
    return out_dict


class LabelCounter:
    def __init__(self, adir):
        self.labels = get_labels(adir)
        self.files = [fix_path(file_path) for file_path in iglob(os.path.join(adir, "*.txt"))]
        self.total_files = len(self.files)

        # create a dict where keys are from the list labels and all the values are 0
        self.label_dict = dict.fromkeys(self.labels, 0)
        self.empty_files = 0
        self.bad_labels = None
        if check_for_wrong_labels(self.labels) is not None:
            self.bad_labels = set(check_for_wrong_labels(self.labels))

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

if get_immediate_subdirectories(search_dir) is None:
    find_label = LabelCounter(search_dir)

    print("[INFO] Searching for labels in text files")
    found_labels_dict = find_label.count()

    total = find_label.total_files
    empty = find_label.empty_files

    print("[INFO] Ploting data")
    plot(found_labels_dict, total, empty)

else:
    sub_dir = get_immediate_subdirectories(search_dir)
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
        final_dict = add_dict(final_dict, found_labels_dict)

    print("[INFO] Ploting data")
    plot(final_dict, total, empty)
