# 服务端安装ansible，配置ssh无密码登录
#
# 客户端安装openresty，添加nginx环境变量

#停止
ansible all -a 'nginx -s stop'
#启动
ansible all -a 'nginx'
