#!/bin/sh

cd /home/makzzz/OMS/OMC-HC/
sudo docker build -t omc-hc .

# delete old build
sudo docker rm omc-hc

# deattach from tty
sudo docker run --name omc-hc -p 6880:6880 -v /var/run/docker.sock:/var/run/docker.sock -v /usr/local/OMC/:/usr/local/OMC -d omc-hc

# intercative mode
#sudo docker run --name omc-hc -p 6880:6880 -v /var/run/docker.sock:/var/run/docker.sock -v /usr/local/OMC/:/usr/local/OMC -ti omc-hc
