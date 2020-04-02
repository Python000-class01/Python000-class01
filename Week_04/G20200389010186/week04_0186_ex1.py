定义组
# cat /etc/ansible/hosts
[www]
192.168.1.100


创建yml文件
# cat test.yml
---
- hosts: www
  user: root
  tasks:
  - name: start openresty
    action: service name=openresty state=started
  - name: stop openresty
    action: service name=openresty state=stopped

执行任务
# ansible-playbook test.yml -u root -T 1
