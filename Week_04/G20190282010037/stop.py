hosts: 192.168.0.2
remote_user: root
  tasks:
    - name: stop nginx
      shell: nginx -s stop
    - name: start nginx
      shell: nginx 