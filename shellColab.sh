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
mv dataSetV01/trainv1text/* trainv1/
mv dataSetV02/trainv1text/* trainv2/
mv dataSetV03/trainv1text/* trainv3/
mv dataSetV04/trainv1text/* trainv4/
mv dataSetV05/trainv1text/* trainv5/
mv dataSetV06/trainv1text/* trainv6/
rm -r dataSetV01

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
cd data

python3 ../../RoadOD/generate_set.py ./obj/ obj -out obj.txt
python3 ../../RoadOD/generate_set.py ./test/ test -out test.txt

#get the weights to train
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137