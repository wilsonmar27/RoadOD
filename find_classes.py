import os
import argparse
from glob import iglob
import yololibs

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory to search", type=str)
args = parser.parse_args()
search_dir = args.dir

label_check = {"D00", "D01", "D10", "D11", "D20", "D40", "D43", "D44", "D50"}


def check_for_wrong_labels(labels_list, label_checker):
    bad = [wrong_label for wrong_label in labels_list if wrong_label not in label_checker]
    if len(bad) == 0:
        return None
    else:
        return bad


class LabelCounter:
    def __init__(self, adir):
        self.labels = yololibs.get_labels(adir)
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
    yololibs.plot(found_labels_dict, total, empty)

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
    yololibs.plot(final_dict, total, empty)
