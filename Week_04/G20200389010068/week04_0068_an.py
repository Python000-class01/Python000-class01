- hosts:192.168.210.124
  remote_user:root
  tasks:
  - name:Start openresty
    shell: /usr/local/openresty/nginx/sbin/nginx
  - name: stop nginx
    shell: /usr/local/openresty/nginx/sbin/nginx -s stop