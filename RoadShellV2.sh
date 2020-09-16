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

#obtain proyect repo
git clone https://strafe:ed141fea880130bcef18ca0b543cfdeb480236b6@github.com/wilsonmar27/RoadOD.git

cp RoadOD/Shell/shellv01.sh V01/
cp RoadOD/Shell/shellv02.sh V02/
cp RoadOD/Shell/shellv03.sh V03/
cp RoadOD/Shell/shellv04.sh V04/
cp RoadOD/Shell/shellv05.sh V05/
cp RoadOD/Shell/shellv06.sh V06/

cd V01
bash shellv01.sh
cd ..

cd V02
bash shellv02.sh
cd ..

cd V03
bash shellv03.sh
cd ..

cd V04
bash shellv04.sh
cd ..

cd V05
bash shellv05.sh
cd ..

cd V06
bash shellv06.sh
cd ..
