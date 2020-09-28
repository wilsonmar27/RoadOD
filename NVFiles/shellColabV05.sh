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

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=18aGyZVwD_7JnUsoO6_boXbyG5dH9obrn' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=18aGyZVwD_7JnUsoO6_boXbyG5dH9obrn" -O G2datasetIMGV02.zip && rm -rf /tmp/cookies.txt
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1hUeVHLVEGa7cWQRMMIq9YkPWrcXyVpE_' -O G2dataSetV05.zip
unzip G2dataSetV05.zip
unzip G2datasetIMGV02.zip

# restore dataset with original organization
mv dataSetV05/ road/
cd road
mv dataSetV05/trainv1text/* trainv1/
mv dataSetV05/trainv2text/* trainv2/
mv dataSetV05/trainv3text/* trainv3/
mv dataSetV05/trainv4text/* trainv4/
mv dataSetV05/trainv5text/* trainv5/
mv dataSetV05/trainv6text/* trainv6/
mv dataSetV05/trainv7NVtext/* trainv7NV/
rm -r dataSetV05

#Place dataset all in one folder
cd ..
mv road/trainv1/* road/
mv road/trainv2/* road/
mv road/trainv3/* road/
mv road/trainv4/* road/
mv road/trainv5/* road/
mv road/trainv6/* road/
mv road/trainv7NV/* road/

rm -r road/trainv1/
rm -r road/trainv2/
rm -r road/trainv3/
rm -r road/trainv4/
rm -r road/trainv5/
rm -r road/trainv6/
rm -r road/trainv7NV/

#split dataset train and val with 20% images to validation
cd road
python3 ../../../RoadOD/split.py ./ 20
cd ../
zip -r roadV05.zip road/

#Go to darknet dir
cd ../
mv data/road/obj/ data/
mv data/road/test/ data/

python3 ../RoadOD/generate_set.py data/obj/ -out ./data/obj.txt
python3 ../RoadOD/generate_set.py data/test/ -out ./data/test.txt

#get the weights to train
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137