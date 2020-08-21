# clone darknet repository 
git clone https://github.com/AlexeyAB/darknet

# change makefile to have GPU and OPENCV enabled
cd darknet
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

# compile darknet
make

# upload the .cfg file for the pryect
cp /INPUT_DIR/yolov4-obj.cfg ./cfg

#obtain the dataset, not sure if we can use wget with google drive
cp -r /INPUT_DIR/test ./data
cp -r /INPUT_DIR/obj ./data

#obtain the image lists 
cp /INPUT_DIR/test.txt ./data
cp /INPUT_DIR/obj.txt ./data

#get the weights to train
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137

cp /INPUT_DIR/obj.names ./data
cp /INPUT_DIR/obj.data ./data

# Train the object detector
# Its recommendable to train 1000 iterations with 1 GPU then stop and 
# start training again with multiple GPUs after 1000
# We dont know how to do this. Profe no sabemos hacer que pare de entrenar despues de los mil y empiece de nuevo 
# con los pesos que se encuentran en el OUTPUT_DIR
./darknet detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137 -dont_show -map >> /OUTPUT_DIR/history.log

# -gpus 0,1 enabels 2 gpus
./darknet detector train data/obj.data cfg/yolov4-obj.cfg /OUTPUT_DIR/backup/yolov4_1000.weights -dont_show -map -gpus 0,1 >> /OUTPUT_DIR/history2.log
