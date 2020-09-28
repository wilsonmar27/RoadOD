#!/bin/bash

# Profe puedes empezar desde el work/
mkdir G2yolo
cd G2yolo

# Hacer un dir por cada version
mkdir V01/
mkdir V02/
mkdir V03/
mkdir V04/
mkdir V05/
mkdir V06/

mkdir V01/data/
mkdir V02/data/
mkdir V03/data/
mkdir V04/data/
mkdir V05/data/
mkdir V06/data/

mkdir V01/cfg/
mkdir V02/cfg/
mkdir V03/cfg/
mkdir V04/cfg/
mkdir V05/cfg/
mkdir V06/cfg/

mkdir V01/backup/
mkdir V02/backup/
mkdir V03/backup/
mkdir V04/backup/
mkdir V05/backup/
mkdir V06/backup/

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

# compile V06
make

# back to G2yolo/
cd ..


# Hacer la V01
cd V01
# obtener pesos 
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1jAdquEHQw0hcPLEvUnERyIvqTc85xMfP' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1jAdquEHQw0hcPLEvUnERyIvqTc85xMfP" -O yolov4-obj_1000.weights && rm -rf /tmp/cookies.txt

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1DJmLHYCEyDah8g2E6n0f6NVTUPxu7wbs' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1DJmLHYCEyDah8g2E6n0f6NVTUPxu7wbs" -O roadV01.zip && rm -rf /tmp/cookies.txt

unzip roadV01.zip
rm roadV01.zip

cd ..
mv data/road/obj data/
mv data/road/test data/
rm -r data/road/

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/NVFiles/objV01.data V01/data/
cp RoadOD/RoadCFG/4C_yolov4-obj.cfg V01/cfg/
cp RoadOD/NVFiles/objV01.names V01/data/

mv V01/cfg/4C_yolov4-obj.cfg V01/cfg/yolov4-obj.cfg
mv V01/data/objV01.data V01/data/obj.data
mv V01/data/objV01.names V01/data/obj.names


# Hacer la V02
cd V02
# obtener pesos 
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-327cBY-n7KAPYSQeKfedPijW1a6gaRu' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-327cBY-n7KAPYSQeKfedPijW1a6gaRu" -O yolov4-obj_1000.weights && rm -rf /tmp/cookies.txt

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-1CzrS5Lcz0UmWh0Yt4DlkP8hsWdtZvw' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-1CzrS5Lcz0UmWh0Yt4DlkP8hsWdtZvw" -O roadV02.zip && rm -rf /tmp/cookies.txt

unzip roadV02.zip
rm roadV02.zip
cd ..

mv data/road/obj data/
mv data/road/test data/
rm -r data/road/

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/NVFiles/objV02.data V02/data/
cp RoadOD/RoadCFG/3C_yolov4-obj.cfg V02/cfg/
cp RoadOD/NVFiles/objV02.names V02/data/

mv V02/cfg/3C_yolov4-obj.cfg V02/cfg/yolov4-obj.cfg
mv V02/data/objV02.data V02/data/obj.data
mv V02/data/objV02.names V02/data/obj.names


# Hacer la V03
cd V03
# obtener pesos 
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-5JAxlK6TDqR7O9Ldl_D7ci7PYWZUDBA' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-5JAxlK6TDqR7O9Ldl_D7ci7PYWZUDBA" -O yolov4-obj_1000.weights && rm -rf /tmp/cookies.txt

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1MuK1BRTovKkm9KdpY1w_IO9uibZ6oyj5' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1MuK1BRTovKkm9KdpY1w_IO9uibZ6oyj5" -O roadV03.zip && rm -rf /tmp/cookies.txt

unzip roadV03.zip
rm roadV03.zip
cd ..

mv data/road/obj data/
mv data/road/test data/
rm -r data/road/

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/NVFiles/objV03.data V03/data/
cp RoadOD/RoadCFG/3C_yolov4-obj.cfg V03/cfg/
cp RoadOD/NVFiles/objV03.names V03/data/

mv V03/cfg/3C_yolov4-obj.cfg V03/cfg/yolov4-obj.cfg
mv V03/data/objV03.data V03/data/obj.data
mv V03/data/objV03.names V03/data/obj.names

# Hacer la V04
cd V04
# obtener pesos 
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-8K9BEr-lJ9m2pWGIFXn1FU7ChshwBzK' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-8K9BEr-lJ9m2pWGIFXn1FU7ChshwBzK" -O yolov4-obj_1000.weights && rm -rf /tmp/cookies.txt

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1XqgdPqpyJausQe8MwSbzMjO0QpSpGl_E' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1XqgdPqpyJausQe8MwSbzMjO0QpSpGl_E" -O roadV04.zip && rm -rf /tmp/cookies.txt

unzip roadV04.zip
rm roadV04.zip
cd ..

mv data/road/obj data/
mv data/road/test data/
rm -r data/road/

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/NVFiles/objV04.data V04/data/
cp RoadOD/RoadCFG/4C_yolov4-obj.cfg V04/cfg/
cp RoadOD/NVFiles/objV04.names V04/data/

mv V04/cfg/4C_yolov4-obj.cfg V04/cfg/yolov4-obj.cfg
mv V04/data/objV04.data V04/data/obj.data
mv V04/data/objV04.names V04/data/obj.names


# Hacer la V05
cd V05
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

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/NVFiles/objV05.data V05/data/
cp RoadOD/RoadCFG/3C_yolov4-obj.cfg V05/cfg/
cp RoadOD/NVFiles/objV05.names V05/data/

mv V05/cfg/3C_yolov4-obj.cfg V05/cfg/yolov4-obj.cfg
mv V05/data/objV05.data V05/data/obj.data
mv V05/data/objV05.names V05/data/obj.names


# Hacer la V06
cd V06
# obtener pesos 
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-kvlBAox8rZdpoTAUZdaF9tPq5k9a-Sv' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-kvlBAox8rZdpoTAUZdaF9tPq5k9a-Sv" -O yolov4-obj_1000.weights && rm -rf /tmp/cookies.txt

#obtain the dataset
cd data
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-OlYBWKdrWcHs62COmVAbC5P-_vXXh2R' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-OlYBWKdrWcHs62COmVAbC5P-_vXXh2R" -O roadV06.zip && rm -rf /tmp/cookies.txt

unzip roadV06.zip
rm roadV06.zip
cd ..

mv data/road/obj data/
mv data/road/test data/
rm -r data/road/

cd ..
# obtener los cfg files (tiene que modificar el obj.data )
cp RoadOD/NVFiles/objV06.data V06/data/
cp RoadOD/RoadCFG/3C_yolov4-obj.cfg V06/cfg/
cp RoadOD/NVFiles/objV06.names V06/data/

mv V06/cfg/3C_yolov4-obj.cfg V06/cfg/yolov4-obj.cfg
mv V06/data/objV06.data V06/data/obj.data
mv V06/data/objV06.names V06/data/obj.names

cd darknet
python ../RoadOD/generate_set.py ../V01/data/test/ -out ../V01/data/test.txt
python ../RoadOD/generate_set.py ../V01/data/obj/ -out ../V01/data/obj.txt

python ../RoadOD/generate_set.py ../V02/data/test/ -out ../V02/data/test.txt
python ../RoadOD/generate_set.py ../V02/data/obj/ -out ../V02/data/obj.txt

python ../RoadOD/generate_set.py ../V03/data/test/ -out ../V03/data/test.txt
python ../RoadOD/generate_set.py ../V03/data/obj/ -out ../V03/data/obj.txt

python ../RoadOD/generate_set.py ../V04/data/test/ -out ../V04/data/test.txt
python ../RoadOD/generate_set.py ../V04/data/obj/ -out ../V04/data/obj.txt

python ../RoadOD/generate_set.py ../V05/data/test/ -out ../V05/data/test.txt
python ../RoadOD/generate_set.py ../V05/data/obj/ -out ../V05/data/obj.txt

python ../RoadOD/generate_set.py ../V06/data/test/ -out ../V06/data/test.txt
python ../RoadOD/generate_set.py ../V06/data/obj/ -out ../V06/data/obj.txt
