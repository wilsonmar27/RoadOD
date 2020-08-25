import os
import numpy as np
import matplotlib.pyplot as plt

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
    
# get lines in a file and place in a list
def get_lines(file_path):
    file_2read = open(file_path, 'r')
    lines = [w.replace('\n', '') for w in file_2read.readlines()]
    file_2read.close()
    return lines

# get labels from the _darknet.labels files
def get_labels(in_dir):
    darknet_lables_file = open(os.path.join(in_dir, "_darknet.labels"), 'r')
    labels_in_dir = [w.replace('\n', '') for w in darknet_lables_file.readlines()]
    darknet_lables_file.close()
    return labels_in_dir

# adds two dictionaries where the key is a label and the key values are ints.
def add_dict(dict1, dict2, label_checker):
    dict1_p1 = list(dict1)
    dict1_p2 = list(dict1.values())
    dict2_p1 = list(dict2)
    dict2_p2 = list(dict2.values())

    for i in range(len(dict2_p1)):
        for j in range(len(dict1_p1)):
            if dict2_p1[i] == dict1_p1[j]:
                dict1_p2[j] = int(dict1_p2[j]) + int(dict2_p2[i])
        if dict2_p1[i] not in dict1_p1 and dict2_p1[i] in label_checker:
            dict1_p1.append(dict2_p1[i])
            dict1_p2.append(int(dict2_p2[i]))
    out_dict = {dict1_p1[k]: dict1_p2[k] for k in range(len(dict1_p1))}
    return out_dict


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


