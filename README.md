# Automated Deployment and Container Orchestration with Ansible, Docker, and Kubernetes

This repository demonstrates how to use Ansible for automating the build, push, and deployment of a Dockerized web application to Kubernetes.

## Prerequisites

Before running the Ansible playbooks, make sure you have the following installed and configured:

### 1. Install Docker and Docker Hub CLI
Ensure Docker is installed on your system. You can install Docker by following the [Docker installation guide](https://docs.docker.com/get-docker/).

Also, ensure you have logged in to Docker Hub using the command:
```bash
docker login
```
### 2. Install Kubernetes and kubectl

Ensure Kubernetes is installed and running. You can install minikube or connect to your existing Kubernetes cluster. Follow the Kubernetes installation guide for installation.

Also, install kubectl for managing Kubernetes clusters:

```bash

sudo apt-get install -y kubectl
```
### 3. Install Python and Required Ansible Modules

Make sure you have Python installed and the necessary Ansible collections for Docker and Kubernetes.

Install Python if it's not already installed:

```bash

sudo apt-get install python3 python3-pip
```
Install the required Ansible collections:

```bash

ansible-galaxy collection install community.docker
ansible-galaxy collection install kubernetes.core
```
Install Python modules for Kubernetes:

```bash

pip install kubernetes
```
### 4. Configure Kubernetes Namespace

Ensure the Kubernetes namespace you are deploying to exists. You can create a namespace by running:

```bash

kubectl create namespace default  # or replace 'default' with any namespace
```
### 5. Minikube Tunnel

If you are using Minikube for Kubernetes, you need to create a tunnel to expose services. Run the following command:

```bash

minikube tunnel
```
## Usage
### 1. Clone the Repository

Clone the repository to your local machine:

```bash

git clone https://github.com/JAZWii/Automated-Deployment-and-Container-Orchestration.git
cd Automated-Deployment-and-Container-Orchestration
```
### 2. Build and Push Docker Image

Use Ansible to build the Docker image and push it to Docker Hub.

Run the following command:

```bash

ansible-playbook -i inventory build-and-push.yaml
```
This playbook will:

    Build the Docker image from the ../app/ directory.
    Push the image to Docker Hub.

### 3. Deploy to Kubernetes

Once the Docker image is pushed, use Ansible to deploy it to your Kubernetes cluster.

Run the following command:

```bash

ansible-playbook -i inventory deploy-to-k8s.yaml
```
This playbook will:

    Apply the Kubernetes deployment configuration from ../k8s/deployment.yaml.
    Apply the Kubernetes service configuration from ../k8s/service.yaml.

### 4. Run the Entire Workflow

If you want to run the entire build, push, and deployment process with a single command, use the following:

```bash

ansible-playbook -i inventory ansible/playbook.yml
```
This command will execute both Docker and Kubernetes tasks sequentially.

### 5. Verify Deployment

You can verify the deployment by running:

```bash

kubectl get pods -n default
kubectl get services -n default
```
This will show the status of the deployed pods and services.
### Project Structure

```bash

.
├── README.md                 # Project documentation
├── ansbile                   # Ansible inventory file
│   ├── docker.yml            # Ansible playbook for building and pushing the Docker image
│   ├── kubernetes.yml        # Ansible playbook for deploying the application to Kubernetes
│   └── playbook.yml          # Ansible main playbook
├── k8s
│   ├── deployment.yaml        # Kubernetes deployment file
│   └── service.yaml           # Kubernetes service file
└── app
    ├── Dockerfile            # Dockerfile for building the Docker image
    ├── app.py                # Application files
    └── requirements.txt      # Application files
```
