git clone https://github.com/ribt/dtmf-decoder.git; \
cd dtmf-decoder/; \
sudo python3 -m pip install -r requirement.txt --upgrade; \
chmod +x dtmf.py; \
sudo cp dtmf.py /usr/local/bin/dtmf;
rm -r ../dtmf-decoder