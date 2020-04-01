1. 启动 
ansible web -m shell -a '/usr/local/openresty/nginx/sbin/nginx -c /usr/local/openresty/nginx/conf/nginx.conf'

2. 运行 
ansible web -m shell -a 'curl http://localhost:8080/'

3. 停止 
ansible web -m shell -a 'killall nginx'