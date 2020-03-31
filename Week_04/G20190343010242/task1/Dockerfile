FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1

ENV ANSIBLE_VERSION 2.9.6

RUN apk add --update python py-pip openssl ca-certificates bash git sudo zip \
    && apk --update add --virtual build-dependencies python-dev libffi-dev openssl-dev build-base \
    && pip install --upgrade pip cffi \
    && echo "==== Installing Ansible ====" \
    && pip install ansible==$ANSIBLE_VERSION \
    && pip install --upgrade pycrypto pywinrm  \
    && apk add openrc \
    && apk add curl \
    && apk --update add sshpass openssh-client openssh rsync \
    && ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa \
    && echo "==== Removing package list ====" \
    && apk del build-dependencies \
    && rm -rf /var/cache/apk/*

RUN echo "==== Adding hosts ====" \
    && mkdir -p /etc/ansible \
    && echo 'localhost' > /etc/ansible/hosts

COPY nginx.yaml /tmp/playbooks/nginx.yaml
COPY nginx_stop.yaml /tmp/playbooks/nginx_stop.yaml

VOLUME ["/sys/fs/cgroup"]

EXPOSE 80/tcp

CMD ["/bin/sh"]