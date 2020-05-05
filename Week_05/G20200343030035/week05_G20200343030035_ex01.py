host: 192.168.199.130
  remote_user: root
  tasks:
     name: start nginx
     shell: /usr/local/openresty/nginx/sbin/nginx
     name: stop nginx
     shell: /usr/local/openresty/nginx/sbin/nginx -s stop