[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/wilsonmar27/RoadOD/blob/master/LICENSE)

# RoadOD (Object Detection)

![logo](https://flowimage.flow.page/resize?img=https%3A%2F%2Fcdn.flowpage.com%2Fimages%2F88b8ee58-42ab-4d71-8c6c-d9f33160012b-profile-picture%3Fm%3D1603915459&w=130)

RoadOD is the GitHub Repo of the project *Real-Time Detection of Irregularities on the Road.*

# Abstract

Road conditions caused 34% of all the traffic accidents recorded in Costa Rica during the years 2015 through 2017. There are prevention systems like Anti-lock Braking System (ABS) and Electronic Stability Program (ESP) that reduce the severity of a loss of control on a vehicle. However, these systems alone may not be enough to prevent these catastrophes nor increase road safety. In addition to these systems, a device that acts sooner by warning the driver before an irregularity is present on the road may significantly reduce accidents caused by these malformations and thus making travel safer. We trained an object detector using the state of the art YOLOv4 framework to achieve real-time detection of risky road conditions. The dataset used to train a Deep Learning model influences the accuracy and precision of the model; consequently, we created six different datasets based on the Dataset for Global Road Damage Detection Challenge 2020 and images of our own. As a result, we trained the most efficient YOLOv4 object detector for the given set of images. A program that uses the developed computer model and collaboratively shares the location and data of risky road conditions with other users may significantly reduce road accidents caused solely by road conditions. This data may also be shared with authorities to increase road maintenance efficiency. Most research in the field aims to obtain the most accurate computer vision model, leaving behind detection speed. However, our model detects in real-time with a small decrease in accuracy.

## A detection of our model

![Example of detection](https://raw.githubusercontent.com/wilsonmar27/RoadOD/master/DataSet_info/Czech_000396.jpg)

## Built with

* [Darknet (YOLOv4)](https://github.com/AlexeyAB/darknet)
* [Dataset for Global Road Damage Detection Challenge 2020 (RDD 2020)](https://github.com/sekilab/RoadDamageDetector/)

# Usage

This project was developed in [Google Collaboratory](https://colab.research.google.com), and specifically for RDD 2020. However, the developed code can be used for any project that uses Darknet and needs image dataset manipulation.

We recommend the use of a conda environment

## View contents in dataset

[find_classes.py](https://github.com/wilsonmar27/RoadOD/blob/master/find_classes.py)

Edit in [line 26](https://github.com/wilsonmar27/RoadOD/blob/master/find_classes.py#L26), and add the classes you will be analyzing, then run:

```bash
python3 find_classes.py [dir of dataset] --names [names file]
```

After execution, a window of a matplotlib plot will show, example:

![dataset](https://raw.githubusercontent.com/wilsonmar27/RoadOD/master/DataSet_info/ORG_DS.png)

For optional arguments please run:

```bash
python3 find_classes.py -h
```

## Delete labels and leave only images

```bash
python3 delTxt.py [dir of dataset]
```

## Manipulate labels in dataset

Write a .names file that contains the labels you want to have.

Write a key that contains the instructions on what to do with the dataset with the following format.

The program will keep the label if it doesn't appear on the fix.txt file and it is in the .names file

Keys:

* label:del => this means delete the annotation
* label1:label2 => this means convert label1 to label2

### Example of usage

Suppose you have a dataset that has labels of cats, lizards, Huskies and Dobermans and you want to remove lizards due to underrepresentation. You also want to merge Dobermans and Huskies into a Dog class.

Your .names file will look like this:

```text
Cat
Dog
```

Your key file will look like this:

```text
Lizard:del
Husky:Dog
Doberman:Dog
```

Terminal comand:

```bash
python3 fix_labels.py -k [key] -n [names file] -i [dir of dataset] -out [output folder]
```

## Split dataset into a training and validation set

[split.py](https://github.com/wilsonmar27/RoadOD/blob/master/split.py)

Given directory of images and labels it will output a folder with the training set and a folder with the validation set.

```text
python3 split.py [dir of dataset] [percentage of images for validation (0-100)]
```

## Generate a list of images from dataset

Generates a text file containing a list of image paths from images in a directory.

```bash
python3 generate_set.py -i [dir containing the images you want to list] --output [output file name (optional, default "out.txt")]
```

## Training

To train each version of the dataset we used the shell scripts found in [NVFiles]( https://github.com/wilsonmar27/RoadOD/tree/master/NVFiles), this would also generate a zip file containing the version of the dataset for further training.

* [Colab notebook example](https://colab.research.google.com/drive/1pvkrWGjh1RgB9nj5n2hHeMaze6D8AiFq?usp=sharing)
* [Further training example](https://colab.research.google.com/drive/1SlnqZOPlLb6kz5Ke0VSx-L1zidyD6rr2?usp=sharing)

## Data analysis

To analyze the log file the training returned, use [readLog.py]( https://github.com/wilsonmar27/RoadOD/blob/master/readLog.py)

It will output a text file where each line is the average loss for each iteration and a csv file with the mAP values at the given iteration.

```text
python3 readLog.py [log file path] [text file output (loss)] [csv file output (mAP)]
```

When making predictions on a directory of images, the darknet framework outputs a json file containing the predictions. To display these predictions in the images use [boxImg.py](https://github.com/wilsonmar27/RoadOD/blob/master/boxImg.py)

Change [line 8](https://github.com/wilsonmar27/RoadOD/blob/master/boxImg.py#L8) with your parameters.

```bash
python3 boxImage.py -j [json file] -out [output dir to place annotated images]
```

# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

