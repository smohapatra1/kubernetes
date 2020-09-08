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
def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print(p.stdout)
print ("Installing kubectl....")

#subprocess_cmd('curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl ; chmod +x ./kubectl ; sudo mv .kubectl /usr/local/bin/kubectl ; kubectl version ; kubectl version --client')

#Using homebrew version

subprocess_cmd('brew remove kubectl ; brew install kubectl ; brew install kubernetes-cli ; kubectl version --client')

#; curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - ; sudo touch /etc/apt/sources.list.d/kubernetes.list ; echo \"deb http://apt.kubernetes.io/ kubernetes-xenial main\" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list ; sudo brew update ; sudo brew install kubectl ; kubectl version ')
