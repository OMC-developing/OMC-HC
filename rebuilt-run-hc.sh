#!/bin/sh

cd /home/makzzz/OMC/OMC-HC/
sudo docker build --no-cache -t omc-hc .
sudo docker run -p 6880:6880 -v /var/run/docker.sock:/docker.sock -v /usr/local/OMC/:/usr/local/OMC -d omc-hc
