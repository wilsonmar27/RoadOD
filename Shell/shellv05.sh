#!/bin/bash

# clone darknet repository
git clone https://github.com/AlexeyAB/darknet
#obtain proyect repo
git clone https://github.com/wilsonmar27/RoadOD.git

# change makefile to have GPU and OPENCV enabled
cd darknet
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

# compile darknet
make

# obtener pesos 
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-CRYiYINtKRgJqM567tAps2pmtAI9iuJ' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-CRYiYINtKRgJqM567tAps2pmtAI9iuJ" -O yolov4-obj_1000.weights && rm -rf /tmp/cookies.txt

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1DjnEr_jCn3Jw0ZZV0JC9tzyyQzGo_Qgk' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1DjnEr_jCn3Jw0ZZV0JC9tzyyQzGo_Qgk" -O roadV05.zip && rm -rf /tmp/cookies.txt
unzip roadV05.zip

rm roadV05.zip
cd ..

mv data/road/obj data/
mv data/road/test data/
rm -r data/road/

cp ../RoadOD/dataFiles/V05/obj.txt data/
cp ../RoadOD/dataFiles/V05/test.txt data/

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/RoadCFG/3C_obj.data darknet/data/
cp RoadOD/RoadCFG/3C_yolov4-obj.cfg darknet/cfg/
cp RoadOD/NVFiles/objV05.names darknet/data/

mv darknet/cfg/3C_yolov4-obj.cfg darknet/cfg/yolov4-obj.cfg
mv darknet/data/3C_obj.data darknet/data/obj.data
mv darknet/data/objV05.names darknet/data/obj.names
