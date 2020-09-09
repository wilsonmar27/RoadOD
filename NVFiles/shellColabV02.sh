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

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1cSwWf_7wEKYzYEWC1bC_oi2IBPzJld0s' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1cSwWf_7wEKYzYEWC1bC_oi2IBPzJld0s" -O G2datasetIMG.zip && rm -rf /tmp/cookies.txt
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=143AnCRIsE7kSjBDybc6-1QOkk4ZoI02v' -O G2dataSetV02.zip
unzip G2dataSetV02.zip
unzip G2datasetIMG.zip

# restore dataset with original organization
mv dataSetV02/ road/
cd road
mv dataSetV02/trainv1text/* trainv1/
mv dataSetV02/trainv2text/* trainv2/
mv dataSetV02/trainv3text/* trainv3/
mv dataSetV02/trainv4text/* trainv4/
mv dataSetV02/trainv5text/* trainv5/
mv dataSetV02/trainv6text/* trainv6/
rm -r dataSetV02

#Place dataset all in one folder
cd ..
mv road/trainv1/* road/
mv road/trainv2/* road/
mv road/trainv3/* road/
mv road/trainv4/* road/
mv road/trainv5/* road/
mv road/trainv6/* road/

rm -r road/trainv1/
rm -r road/trainv2/
rm -r road/trainv3/
rm -r road/trainv4/
rm -r road/trainv5/
rm -r road/trainv6/

#split dataset train and val with 20% images to validation
cd road
python3 ../../../RoadOD/split.py ./ 20
cd ../
zip -r roadV02.zip road/

#Go to darknet dir
cd ../
mv data/road/obj/ data/
mv data/road/test/ data/

python3 ../RoadOD/generate_set.py data/obj/ -out ./data/obj.txt
python3 ../RoadOD/generate_set.py data/test/ -out ./data/test.txt

#get the weights to train
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137