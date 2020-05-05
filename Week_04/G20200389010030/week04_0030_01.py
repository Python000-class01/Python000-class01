- hosts: 192.168.84.250
  remote_user: root
  tasks:
  - name: Start Nginx 
    shell: /usr/local/nginx/sbin/nginx
  - name: Stop Nginx
    shell: /usr/local/nginx/sbin/nginx -s stop