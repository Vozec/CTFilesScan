#!/bin/bash

FILE=./linux_installed.txt

saved=''
if test -f "$FILE"; then
    saved=$(cat $FILE)
fi

search_dir=linux
for entry in "$search_dir"/*
do

  string='linux/steganoveritas_setup.sh\nlinux/steganoveritas_setup.sh'
  if [[ $saved == *"$(echo "$entry"|tr -d '\n')"* ]]; then
    echo "$entry already installed"
  else
    echo "#######################################"
    echo "Running $entry "
    echo "#######################################"
    chmod +x $entry
    /bin/bash "$entry"
    echo $entry >> $FILE
  fi
 
done