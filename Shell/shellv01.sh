#!/bin/bash

# clone darknet repository
git clone https://github.com/AlexeyAB/darknet
#obtain proyect repo
git clone https://strafe:ed141fea880130bcef18ca0b543cfdeb480236b6@github.com/wilsonmar27/RoadOD.git

# change makefile to have GPU and OPENCV enabled
cd darknet
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

# compile darknet
make

# obtener pesos 
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1jAdquEHQw0hcPLEvUnERyIvqTc85xMfP' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1jAdquEHQw0hcPLEvUnERyIvqTc85xMfP" -O yolov4-obj_1000.weights && rm -rf /tmp/cookies.txt

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1DJmLHYCEyDah8g2E6n0f6NVTUPxu7wbs' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1DJmLHYCEyDah8g2E6n0f6NVTUPxu7wbs" -O roadV01.zip && rm -rf /tmp/cookies.txt
unzip roadV01.zip
cd ..

mv data/road/obj data/
mv data/road/test data/
rm -r data/road/

cp ../RoadOD/dataFiles/V01/obj.txt data/
cp ../RoadOD/dataFiles/V01/test.txt data/

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/RoadCFG/4C_obj.data darknet/data/
cp RoadOD/RoadCFG/4C_yolov4-obj.cfg darknet/cfg/
cp RoadOD/NVFiles/objV01.names darknet/data/

mv darknet/cfg/4C_yolov4-obj.cfg darknet/cfg/yolov4-obj.cfg
mv darknet/data/4C_obj.data darknet/data/obj.data
mv darknet/data/objV01.names darknet/data/obj.names

cd darknet
./darknet detector train data/obj.data cfg/yolov4-obj.cfg yolov4-obj_1000.weights -dont_show -map -gpus 0,1 >> OUTPUT/historyV01_2.log