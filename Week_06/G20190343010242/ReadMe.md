## Week06 Assignment

See [here](https://u.geekbang.org/lesson/8?article=201469) for details of requirements of the task.

The whole task is run in the Kubernetes cluster. The project is managed by [skaffold](https://skaffold.dev/).
You can have build runtime on AWS EKS, GCP(Google Cloud Platform) GKE, local environment, etc.
The task here is run on local environment.

### Project Structure

- sentiment: This folder stores the [helm chart](https://helm.sh/docs/topics/charts/), which includes the 
configuration and kubernetes templates.

- src: Include backend and frontend. The backend is used to create models, interact with database, and create 
business logic. It provides the APIs for the frontend. The frontend is used to render the web pages, call the backend APIs and implement 
the web logic.

- skaffold.yaml: Skaffold configuration file. See [doc](https://skaffold.dev/docs/references/yaml/) here.

Skaffold will create images for backend and frontend respectively, and they will talk each other within the Kubernetes cluster.

### Prerequisites

You need to get below applications installed before kicking off the app.

- [Docker desktop(windows or MacOS)](https://www.docker.com/products/docker-desktop). 
- [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) and [docker(Linux)](https://docs.docker.com/engine/install/)

** Recommend to install docker desktop for Windows or MacOS. If you install docker desktop, make sure you get Kubernetes enabled. 
- [skaffold](https://skaffold.dev/docs/install/)
- [helm3](https://helm.sh/docs/intro/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [docker hub](https://hub.docker.com/) account or accounts on other popular public container registry which hosts most common images, like [gcr(Google)](https://cloud.google.com/container-registry), [ecr(Amazon)](https://aws.amazon.com/ecr/).
- Python3.7 and pip (Best tested). This is only required if you need to run from IDE without using skaffold.

### Setup and Run

a) Setup local container registry.
```bash
$ docker run -d -p 5000:5000 --name registry registry:2
```
You can have your own port and registry name. Once it's setup, go to 
http://localhost:5000/v2/_catalog to see all your repositories.
If you need to stop and remove it, run
```bash
$ docker stop registry
$ docker rm registry
```
If you prefer using other public registry instead, this step can be skipped.

b) Create new namespace in Kubernetes cluster. This step is recommended to isolate the environment.
```bash
$ kubectl create namespace <your namespace>
```
In my assignment, I created a namespace called 'week06'.

c) Go to the project directory which has skaffold.yaml file. Replace the namespace you created in above step under section 'deploy/helm/releases'.
Also, replace the "container_repo" property under file ./sentiment/values.yaml with your container registry path that the images are pushed to.

In my case, it is "localhost:5000/week06"

d) Run application
```bash
$ skaffold run -d <your container registry path>
```
In my case, it is "localhost:5000/week06". Once it's successfully installed and up running, go to
http://localhost to access the page. In case your port 80 is occupied by other application on your computer,
modify 'frontendPort' property in sentiment/values.yaml file. Likewise, you can update your local host mysql port by modifying 
'mysqlPort' property if it conflicts with your default mysql port.

e) Stop application
```bash
$ skaffold delete
```

### Troubleshooting

- Monitor all resources under your namespace.
```bash
$ kubectl get all -n <namespace>
```
- Run application as debug or development mode

dev
```bash
$ skaffold dev -d <your container registry path>
``` 
debug
```bash
$ skaffold debug -d <your container registry path>
```
- See logs or describe a particular pod
```bash
$ kubectl logs <pod id> -n <namespace>
```
```bash
$ kubectl describe pod/<pod id> -n <namespace>
```
- Login to particular pod to interact with it
```bash
$ kubectl exec -it <pod id> -n <namespace> -- bash 
```
- You may encounter the situation that mysql fails to initialize the database. If that's the case,
go to the mysql pod by running command below:
```bash
kubectl exec -it mysql-0 -n <namespace> -- bash
```
then load initdb.sql to initialize the database.
```bash
mysql -uroot -p < ./docker-entrypoint-initdb.d/initdb.sql
```
enter the password, then the database will be initialized.

** You may need to restart the application by stopping and running application again.

### Debug on IDE

I will take [PyCharm](https://www.jetbrains.com/pycharm/) as an example.

a) Install [cloud code](https://cloud.google.com/code) plugin which is also available for VS Code.

b) Load the source code into a new project. You can create a new run configuration to 
run/debug the Cloud Code application. In the configuration, you can input your 
container registry url in 'Image options' section. Then you can run/debug the application like others.

cloud code will keep watching your changes, and automatically sync your changes to containers.

VS Code is quite similar, here is a [quickstart](https://cloud.google.com/code/docs/vscode/quickstart) doc from google cloud.

