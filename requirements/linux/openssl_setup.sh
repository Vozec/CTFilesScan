wget http://www.openssl.org/source/openssl-1.0.1g.tar.gz;
tar -xvzf openssl-1.0.1g.tar.gz;
rm openssl-1.0.1g.tar.gz;
cd openssl-1.0.1g;
./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl;
make;
make install_sw;
rm -r ../openssl-1.0.1g;
