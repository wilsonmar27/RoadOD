# This script compares the result of 2 models
import os
import argparse
from yololibs import readjson

parser = argparse.ArgumentParser()
parser.add_argument("-m1", "--model1",
                    help="json file of the results from model 1, this should have the D10 Class",
                    type=str, required=True)
parser.add_argument("-m2", "--model2", help="json file of the results from model 2", type=str, required=True)
args = parser.parse_args()
model1_json = args.model1
model2_json = args.model2

model1 = readjson(model1_json)
model2 = readjson(model2_json)

if len(model1) != len(model2):
    raise Exception("Json files do not have the same image lenth," \
                    "remeber to predict on the same set of images")

model1_conf = 0
model2_conf = 0

for i in range(len(model1)):
    if len(model1[i]['objects']) == len(model2[i]['objects']):
        for obj1 in model1[i]['objects']:
            if obj1['name'] == "D10":
                print('Check {}, same amount of objects but has D10'
                      .format(os.path.split(model1[i]['filename'])[1]))
                break

        for obj1 in model1[i]['objects']:
            for obj2 in model2[i]['objects']:
                # find differnce in the center point
                x1 = obj1['relative_coordinates']['center_x']
                x2 = obj2['relative_coordinates']['center_x']
                y1 = obj1['relative_coordinates']['center_y']
                y2 = obj2['relative_coordinates']['center_y']
                xdiff = abs(x2 - x1)
                ydiff = abs(y2 - y1)
                same_label = False
                
                # if center points are less then 18 pixel away, then the object is the same
                if xdiff or ydiff > 0.03:
                    same_label = True
                if obj1['name'] == obj2['name'] and same_label:
                    if obj1['confidence'] > obj2['confidence']:
                        model1_conf += 1
                    if obj1['confidence'] < obj2['confidence']:
                        model2_conf += 1
                    else:
                        model2_conf += 1
                        model1_conf += 1
    else:
        print('Check {}'.format(os.path.split(model1[i]['filename'])[1]))

print('\nMore confidence in Model1: {}'.format(model1_conf))
print('More confidence in Model2: {}'.format(model2_conf))