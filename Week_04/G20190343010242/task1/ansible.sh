#! /bin/bash

set -e

action=$1
imageName=$2
imageVersion=$3

if [[ -z $action || -z $imageName || -z $imageVersion ]]; then
    echo "Invalid arguments."
    exit 1
fi

if [[ $action != "start" && $action != "stop" && $action != "clean" ]]; then
    echo "Invalid action $action"
    exit 1
fi

imageId=$(docker images $imageName:v$imageVersion -q)
if [ ! -f ${PWD}/container ]; then
    touch ${PWD}/container
fi
containerId=$(cat ${PWD}/container)
if [ $action == "start" ]; then
    if [ -z $imageId ]; then
        echo "Image does not exit, start building..."
        docker build -t $imageName:v$imageVersion ${PWD}/
        imageId=$(docker images $imageName:v$imageVersion -q)
    fi
    if [ -z $containerId ]; then
        echo "Start new container.."
        containerId=$(docker run -d $imageName:v$imageVersion tail -f /dev/null)
        echo $containerId > ${PWD}/container
    else
        docker inspect -f '{{.State.Running}}' $containerId
        if [ $? != 0 ]; then
            echo "Clean stopped container $containerId"
            docker rm $containerId
            echo "Start new container.."
            containerId=$(docker run -d $imageName:v$imageVersion tail -f /dev/null)
            echo $containerId > ${PWD}/container
        fi
    fi
    docker exec -it $containerId ansible-playbook /tmp/playbooks/nginx.yaml --connection=local
    if [ $? == 0 ]; then
        echo "Nginx started."
    else
        echo "Nginx failed to start."
        exit 1
    fi
elif [ $action == "stop" ]; then
    if [ -z $containerId ]; then
        echo "Container is not started"
        exit 1
    else
        docker inspect -f '{{.State.Running}}' $containerId
        if [ $? != 0 ]; then
            echo "Container $containerId has been stopped."
            exit 1
        fi
    fi
    docker exec -it $containerId ansible-playbook /tmp/playbooks/nginx_stop.yaml --connection=local
    if [ $? == 0 ]; then
        echo "Nginx stopped."
    else
        echo "Nginx failed to stop."
        exit 1
    fi
else
    if [[ -z $containerId || -z $imageId ]]; then
        echo "Container or image is not found."
        exit 1
    fi
    docker inspect -f '{{.State.Running}}' $containerId
    if [ $? == 0 ]; then
        docker stop $containerId
    fi
    docker rm $containerId
    docker rmi $imageId
    rm -f ${PWD}/container
fi

exit 0