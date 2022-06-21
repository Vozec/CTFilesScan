git clone https://github.com/AppLeU0/chainbreaker.git
cd chainbreaker
python -m pip install hexdump
chmod +x chainbreaker.py; \
sudo cp chainbreaker.py /usr/local/bin/chainbreaker;
sudo cp pbkdf2.py /usr/local/bin/pbkdf2.py;
sudo cp pyDes.py /usr/local/bin/pyDes.py;
sudo cp Schema.py /usr/local/bin/Schema.py;
rm -r ../chainbreaker