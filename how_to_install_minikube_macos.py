#!/usr/bin/python
import os
import subprocess
import time
import cmd
#pre-req :- 
    # 	Make sure hypervisor also installed #Can be checked by running this command 
		#sysctl -a | grep -E --color machdep.cpu.features|VMX'
    #   Make sure kubectl is instablled 
    #   Make sure kubelet also installed
    #   minikube start --vm-driver=none # If you are installing inside a VM
    # 	minikube start --vm-driver=virtualbox # If you are starting using a virtual machine e.g vagrant
    # 	https://minikube.sigs.k8s.io/docs/drivers/virtualbox/

# Install Minikube
    # * Stop Minikube
    # * Remove minikube
    # * Install Minikube
    # * Start Minikube 
        # * if you are starting minikube on a host machine use - sudo minikube start
        # * if running on virtualBox having an ubuntu VM on it start like this - sudo minikube start --vm-driver=none
    # * Give kubectl access to non-root user
        # * chown -R $USER $HOME/.kube
        # * sudo chgrp -R $USER $HOME/.kube
    # * Give minikube to non-root user
        # * sudo chown -R $USER $HOME/.minikube
        # * sudo chgrp -R $USER $HOME/.minikube
    #*************** If we get bellow error *****************
    # The connection to the server 10.0.2.15:8443 was refused - did you specify the right host or port?    
    #*************** Try bellow 
    # * Change the path of the config file
        # * kubectl stop
        # * kubectl config use-context minikube
        # * kubectl start

def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print(p.stdout)
print ("Installing minikube....")

subprocess_cmd('sysctl -a | grep -E --color "machdep.cpu.features|VMX" ; brew update ; brew install minikube; sudo mv minikube /usr/local/bin ; which minikube ; minikube version; kubeadmin version ; kubectl version ; kubelet version ; minikube status ; sudo chown -R $USER $HOME/.minikube ; minikube start --vm-driver=virtualbox; minikube status ')

#subprocess_cmd('sudo minikube stop; sudo apt-get update ; sudo apt-get -y autoremove kubeadm kubectl kubelet; sudo apt-get -y install curl ; curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add ; sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"; sudo apt-get -y install kubeadm kubelet kubectl ; kubeadm version ; kubectl version ; kubelet version ; sudo rm -rf /usr/local/bin/minikube; curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.28.2/minikube-linux-amd64 ; chmod +x minikube ; sudo mv minikube /usr/local/bin/ ; minikube status; minikube version; sudo minikube start --vm-driver=none ; sudo kubectl config view ; chown -R $USER $HOME/.kube ; sudo chgrp -R $USER $HOME/.kube; sudo chown -R $USER $HOME/.minikube ; sudo chgrp -R $USER $HOME/.minikube; sudo minikube stop; sudo kubectl config use-context minikube ; sudo minikube start ')
