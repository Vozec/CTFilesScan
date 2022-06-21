sudo apt-get install libboost-all-dev
git clone https://github.com/danielcardeenas/AudioStego.git
cd AudioStego
mkdir build
cd build
cmake ..
make
ls
mv ./hideme ../../../modules/resources/hideme
rm -r ../../AudioStego