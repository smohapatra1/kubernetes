#!/usr/bin/python
#How to install k8s
#   * Install docker 
#   * Install the k8 key 
#   * Add k8s reporsitoary 
#   * Add kubeadm
#   * Print Version
import os
import subprocess
import cmd
import time

#import pdb; pdb.set_trace() # Running script in debug mode 
#Install docker 
#sudo brew update
#Uninstall the docker if its installed
#sudo brew remove docker docker-engine docker.io
#sudo apt autoremove docker docker-engine docker.io # To remove all dependancies 
#Install Docker 
#sudo apt install docker.io
#Enable Docker 
#sudo systemctl enable docker
#Bellow steps to unmask docker
#If you get the this error - Failed to start docker.service: Unit docker.service is masked.
# sudo systemctl list-unit-files | grep docker
# sudo systemctl unmask docker.service
# sudo systemctl unmask docker.socket
#Start Docker 
#sudo systemctl start docker
#OR
#sudo systemctl start docker.service
# The above will start the docker service
#Check the version - should retrun the docker version e.g Docker version 18.09.7, build 2d0083d
#docker --version 
def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print (p.stdout)
print ("Installing docker....")
subprocess_cmd('sudo brew update ; sudo brew -y autoremove docker docker-engine docker.io ; sudo brew -y autoremove kubeadm ; sudo brew -y install docker.io ; sudo systemctl enable docker ; sudo systemctl unmask docker.service ; sudo systemctl unmask docker.socket ; sudo systemctl start docker ; docker --version ; sudo brew -y install curl ; curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo brew-key add ; sudo brew-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"; sudo brew -y install kubeadm; kubeadm version ') 
