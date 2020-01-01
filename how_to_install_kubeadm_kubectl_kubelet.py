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

def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print (p.stdout)
print ("Installing kubeadm - kubectl - kubelet ....")
subprocess_cmd('sudo apt-get update ; docker --version ; sudo apt-get -y autoremove kubeadm kubectl kubelet; sudo apt-get -y install curl ; curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add ; sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"; sudo apt-get -y install kubeadm kubelet kubectl ; kubeadm version ; kubectl version ; kubelet version') 
