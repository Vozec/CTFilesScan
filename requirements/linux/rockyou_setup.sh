cd /tmp;
wget https://github.com/praetorian-inc/Hob0Rules/raw/master/wordlists/rockyou.txt.gz;
gzip -d rockyou.txt.gz;
mv rockyou.txt /usr/share/wordlists/rockyou.txt;
rm rockyou.txt.gz