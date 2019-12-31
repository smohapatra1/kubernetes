#!/usr/bin/python
import os
import subprocess
import time
import cmd
#How to install kubectl
    # * Remove kubectl
    # * Download latest package
    # * Install the kubectl
    # * Check the version
# Install Minikube
    # * Stop Minikube
    # * Remove minikube
    # * Install Minikube
def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print(p.stdout)
print ("Installing kubectl....")

subprocess_cmd('sudo rm -rf /usr/bin/kubectl ; sudo rm -rf /usr/local/bin/kubectl ; sudo apt-get -y autoremove kubectl; curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - ; sudo touch /etc/apt/sources.list.d/kubernetes.list ; echo \"deb http://apt.kubernetes.io/ kubernetes-xenial main\" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list ; sudo apt-get update ; sudo apt-get install -y kubectl ; kubectl version ; minikube stop; rm -rf /usr/local/bin/minikube; curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.28.2/minikube-linux-amd64 ; chmod +x minikube ; sudo mv minikube /usr/local/bin/ ; minikube status; minikube start')
