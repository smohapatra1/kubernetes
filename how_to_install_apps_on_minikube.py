#!/usr/bin/python
import os
import subprocess
import time
import cmd
#pre-req :- 
    #   Make sure minikube installed 

# Install Minikube
    # * Install an echoserver - kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.10
    # * Expose the app to service - kubectl expose deployment hello-minikube --type=NodePort --port=8080
    # * Get pods - kubectl get pods
    # * Get the URL - minikube service hello-minikube --url
    # * Delete the service - kubectl delete services hello-minikube
    # * Delete the deployment - kubectl delete deployment hello-minikube
    # * Get pods post delete - kubectl get pods 

def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print(p.stdout)
print ("Installing an app on kubernetes through minikube....")

subprocess_cmd('kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.10 ; kubectl expose deployment hello-minikube --type=NodePort --port=8080 ; kubectl get pods ; minikube service hello-minikube --url; kubectl delete services hello-minikube ; kubectl delete deployment hello-minikube ; kubectl get pods ')

