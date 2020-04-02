# - hosts: all
#   tasks:
#    - name: copy package
#      copy: src=/usr/local/openresty-1.13.6.1.tar.gz dest=/usr/local/openresty-1.13.6.1.tar.gz
#    - name: tar nginx
#      shell: cd /usr/local/;tar -zxvf openresty-1.13.6.1.tar.gz
#    - name: yum install
#      yum: name={{ item }} state=latest
#      with_items:
#       - gcc
#       - gcc-c++
#       - readline-devel
#       - pcre-devel
#       - openssl-devel
#       - tcl
#       - perl
#    - name: install nginx
#      shell: cd /usr/local/openresty-1.13.6.1;./configure --prefix=/usr/local/openresty --with-http_stub_status_module --with-http_gzip_static_module --with-luajit;make && make install
#    - name: copy init
#      copy: src=/usr/local/nginx dest=/etc/rc.d/init.d/nginx
#    - name: chmod nginx_init
#      shell: chmod  /etc/rc.d/init.d/nginx