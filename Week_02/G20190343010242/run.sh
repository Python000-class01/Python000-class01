#! /bin/bash

set -x

python_venv=$1
username=$2

if [[ -z $python_venv || -z $username ]]; then
    echo "Invalid arguments."
    exit 1
fi

which python3
if [ $? != 0 ]; then
    echo "Python3.x is not installed on your system."
    exit 1
fi

if [[ ! -d $python_venv ]]; then
    python3 -m venv $python_venv
    source ${PWD}/$python_venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source ${PWD}/$python_venv/bin/activate
fi

python week02_0242_app.py $username

