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
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=12vAw4lTbmqHzu-f_5oMTJn5RW4ic2VmV' -O G2dataSetV01.zip
unzip G2dataSetV01.zip
unzip G2datasetIMG.zip

# restore dataset with original organization
mv dataSetV01/ RoadDataSet/
cd RoadDataSet
mv dataSetV01/trainv1text/ trainv1/trainv1text
mv dataSetV01/trainv2text/ trainv2/trainv2text
mv dataSetV01/trainv3text/ trainv3/trainv3text
mv dataSetV01/trainv4text/ trainv4/trainv4text
mv dataSetV01/trainv5text/ trainv5/trainv5text
mv dataSetV01/trainv6text/ trainv6/trainv6text
rm -r dataSetV01

mv trainv1/trainv1text/*.txt trainv1/
mv trainv2/trainv2text/*.txt trainv2/
mv trainv3/trainv3text/*.txt trainv3/
mv trainv4/trainv4text/*.txt trainv4/
mv trainv5/trainv5text/*.txt trainv5/
mv trainv6/trainv6text/*.txt trainv6/

rm -r trainv1/trainv1text/
rm -r trainv2/trainv2text/
rm -r trainv3/trainv3text/
rm -r trainv4/trainv4text/
rm -r trainv5/trainv5text/
rm -r trainv6/trainv6text/

#Place dataset all in one folder
cd ..
mv RoadDataSet/trainv1/* RoadDataSet/
mv RoadDataSet/trainv2/* RoadDataSet/
mv RoadDataSet/trainv3/* RoadDataSet/
mv RoadDataSet/trainv4/* RoadDataSet/
mv RoadDataSet/trainv5/* RoadDataSet/
mv RoadDataSet/trainv6/* RoadDataSet/

rm -r trainv1/
rm -r trainv2/
rm -r trainv3/
rm -r trainv4/
rm -r trainv5/
rm -r trainv6/

#split dataset train and val with 20% images to validation
python3 ../../RoadOD/split.py RoadDataSet/ 20
zip RoadDataSet RoadDataSetV1.zip

cd ..
mv data/RoadDataSet/obj/ data/
mv data/RoadDataSet/test/ data/

python3 ../RoadOD/generate_set.py ./data/obj/ obj -out ./data/obj.txt
python3 ../RoadOD/generate_set.py ./data/test/ test -out ./data/test.txt

#get the weights to train
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137