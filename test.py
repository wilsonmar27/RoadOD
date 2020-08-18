label_check = {"D00", "D01", "D10", "D11", "D20", "D40", "D43", "D44", "D50"}


def check_for_wrong_labels(labels_list):
    bad = [wrong_label for wrong_label in labels_list if wrong_label not in label_check]
    if len(bad) == 0:
        return None
    else:
        return bad
    
    
print(check_for_wrong_labels(["D00", "HOLAA"]))