
# 作业一：

# 使用 Ansible 结合 ssh 远程控制 OpenResty 软件的启动和停止。


- hosts:192.168.210.124
  remote_user:root
  tasks:
  - name:Start openresty
    shell: /usr/local/openresty/nginx/sbin/nginx
  - name: stop nginx
    shell: /usr/local/openresty/nginx/sbin/nginx -s stop