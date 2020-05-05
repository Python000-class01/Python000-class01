ssh-keygen -t rsa

ssh-copy-id root@192.168.18.130

vim /etc/ansible/hosts//

nginx] //目标主机组

192.168.18.130 //目标主机的ip地址

192.168.18.134 //目标主机的ip地址

ansible nginx -m ping

nginx.yml

ansible-playbook --syntax-check nginx.yml

ansible.playbook nginx.yml

访问目标主机地址